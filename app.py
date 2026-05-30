import streamlit as st
import datetime

# --- 1. CORE SETUP ---
st.set_page_config(page_title="SHEALTH | AI Precision Coach", page_icon="🔮", layout="wide")

# --- 2. ELITE CSS & DOODLE CANVAS ---
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
    .stButton > button { background: #991B1B; color: white; border-radius: 20px; padding: 10px 25px; border: none; }
    </style>
""", unsafe_allow_html=True)

# --- 3. STATE INITIALIZATION ---
if 'active_window' not in st.session_state: st.session_state.active_window = 1
if 'p_name' not in st.session_state: st.session_state.p_name = "Riya Sharma"
if 'p_gender' not in st.session_state: st.session_state.p_gender = "Female Profile"

# --- 4. BIOLOGICAL FEMALE LOGO ---
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

# --- 5. APP WINDOWS ---
# Window 1: Intro
if st.session_state.active_window == 1:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800", use_container_width=True)
    if st.button("Initialize Portal"): jump(2)
    st.markdown("</div>", unsafe_allow_html=True)

# Window 2: Registration
elif st.session_state.active_window == 2:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.session_state.p_name = st.text_input("Full Name", value=st.session_state.p_name)
    st.session_state.p_gender = st.radio("Gender Profile", ["Female Profile", "Male Profile"])
    if st.button("Lock Profile"): jump(3)
    st.markdown("</div>", unsafe_allow_html=True)

# Window 3: AI Scanner
elif st.session_state.active_window == 3:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("### AI Symptom Scanner")
    st.checkbox("Weight fluctuations?")
    st.checkbox("Systemic fatigue?")
    if st.button("Analyze"): jump(5)
    st.markdown("</div>", unsafe_allow_html=True)

# Window 5: Diet Plan
elif st.session_state.active_window == 5:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    day = st.slider("Select Day (1-30)", 1, 30, 1)
    st.markdown(f"### 📅 Day {day} Diet")
    st.markdown(f"<div class='meal-box'><strong>Breakfast:</strong> {'Paneer Oats Cheela' if day%2==0 else 'Sattu Porridge'}</div>", unsafe_allow_html=True)
    if st.button("Compliance Center"): jump(6)
    st.markdown("</div>", unsafe_allow_html=True)

# Window 6: Tracker & Pamper Kit
elif st.session_state.active_window == 6:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("### 🚨 Adherence & Comfort")
    st.slider("Water (Glasses)", 0, 16, 4)
    st.checkbox("💊 Medicine Alarm")
    
    if st.session_state.p_gender == "Female Profile":
        st.write("#### 🌸 Monthly Blues & Pamper")
        st.selectbox("Mood Recorder", ["😊 Happy", "😌 Calm", "😫 Tensed", "🥺 Moody"])
        st.markdown("""
        <div class='pamper-box'>
            <h4>🌸 Cozy Reds Pamper Kit</h4>
            <ul>
                <li><strong>Dark Chocolate:</strong> 'Chup-chap rehne ka mann'</li>
                <li><strong>Sanitary Essentials:</strong> 'Safe-side'</li>
                <li><strong>Hot Water Bottle:</strong> 'Pet-dard ka asli sukoon'</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    if st.button("Reset Session"): jump(1)
    st.markdown("</div>", unsafe_allow_html=True)
