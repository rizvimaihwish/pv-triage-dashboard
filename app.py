import streamlit as st
import datetime

# --- 1. CORE SETUP ---
st.set_page_config(page_title="SHEALTH | AI Precision Coach", page_icon="🔮", layout="wide")

# --- 2. CSS & AESTHETIC DOODLES ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&family=Plus+Jakarta+Sans&display=swap');
    .stApp { background-image: linear-gradient(to bottom, #FEF2F2, #F5F3FF); }
    .stApp::before { content: ""; position: fixed; top: 10%; left: 3%; width: 120px; height: 120px; background-image: url('https://img.icons8.com/color/96/000000/pill.png'); opacity: 0.15; pointer-events: none; }
    .stApp::after { content: ""; position: fixed; bottom: 10%; right: 3%; width: 100px; height: 100px; background-image: url('https://img.icons8.com/color/96/000000/strawberry.png'); opacity: 0.15; pointer-events: none; }
    .logo-container { text-align: center; padding: 20px; }
    .calligraphy-title { font-family: 'Alex Brush', cursive; font-size: 5rem; color: #7F1D1D; }
    .window-container { background: rgba(255, 255, 255, 0.75); backdrop-filter: blur(15px); padding: 30px; border-radius: 25px; border: 1px solid #FCA5A5; }
    .pamper-box { background: #F3E8FF; padding: 20px; border-radius: 15px; border-left: 5px solid #7E22CE; margin-top: 15px; }
    .meal-box { background: white; padding: 15px; border-radius: 15px; border-left: 5px solid #F87171; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. STATE & DATA ---
if 'active_window' not in st.session_state: st.session_state.active_window = 1
if 'user_data' not in st.session_state: st.session_state.user_data = {"name": "", "weight": 68.0, "height": 162.0, "history": ""}
if 'p_gender' not in st.session_state: st.session_state.p_gender = "Female Profile"

# --- 4. FEMALE LOGO ---
st.markdown("""
    <div class='logo-container'>
        <svg width="80" height="80" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" stroke="#991B1B" stroke-width="2" fill="none"/>
            <circle cx="50" cy="40" r="12" stroke="#991B1B" stroke-width="3" fill="none"/>
            <line x1="50" y1="52" x2="50" y2="75" stroke="#991B1B" stroke-width="3"/>
            <line x1="40" y1="65" x2="60" y2="65" stroke="#991B1B" stroke-width="3"/>
        </svg>
        <div class='calligraphy-title'>Shealth</div>
    </div>
""", unsafe_allow_html=True)

def jump(w): st.session_state.active_window = w; st.rerun()

# --- 5. WINDOWS ---
if st.session_state.active_window == 1:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800")
    if st.button("Start Journey"): jump(2)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 2:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("### User Registration")
    st.session_state.user_data['name'] = st.text_input("Name")
    st.session_state.p_gender = st.radio("Gender", ["Female Profile", "Male Profile"])
    st.session_state.user_data['weight'] = st.number_input("Weight (kg)", value=68.0)
    if st.button("Save Profile"): jump(3)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 3:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("### AI Symptom Scanner")
    st.checkbox("1. Weight fluctuations?")
    st.checkbox("2. Systemic fatigue?")
    st.checkbox("3. Hormonal cycles delay?")
    if st.button("Analyze Results"): jump(4)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 4:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write(f"### BMI Check for {st.session_state.user_data['name']}")
    bmi = st.session_state.user_data['weight'] / ((162/100)**2)
    st.write(f"Your BMI is: {bmi:.1f}")
    if st.button("Next: View Diet Plan"): jump(5)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 5:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    day = st.slider("Select Day (1-30)", 1, 30, 1)
    st.markdown("### 📅 30-Day Diet Plan")
    st.markdown(f"<div class='meal-box'><strong>Day {day} Breakfast:</strong> {'Paneer Oats Cheela' if day%2==0 else 'Sattu Porridge'}</div>", unsafe_allow_html=True)
    if st.button("Compliance Center"): jump(6)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 6:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("### 🚨 Adherence Dashboard")
    # Tracker
    gl = st.slider("Water Intake (Glasses)", 0, 16, 4)
    st.progress(gl/12)
    st.checkbox("💊 Medicine Alarm")
    
    if st.session_state.p_gender == "Female Profile":
        st.write("#### 📝 Monthly Blues & Pamper")
        st.selectbox("Mood Recorder", ["😊 Happy", "😌 Calm", "😫 Tensed", "🥺 Moody"])
        st.markdown("""
        <div class='pamper-box'>
            <h4>🌸 The 'Cozy Reds' Pamper Kit</h4>
            <ul>
                <li><strong>Dark Chocolate:</strong> 'Chup-chap rehne ka mann'</li>
                <li><strong>Sanitary Essentials:</strong> 'Safe-side'</li>
                <li><strong>Hot Water Bottle:</strong> 'Pet-dard ka asli sukoon'</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    if st.button("Reset Session"): jump(1)
    st.markdown("</div>", unsafe_allow_html=True)
