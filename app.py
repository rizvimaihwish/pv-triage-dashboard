import streamlit as st
import datetime

# --- 1. CORE SETUP ---
st.set_page_config(page_title="SHEALTH | AI Precision Coach", page_icon="🔮", layout="wide")

# --- 2. CSS WITH MORE DOODLES (PILLS, FRUITS, LAVENDER) ---
st.markdown("""
    <style>
    .stApp { background-image: linear-gradient(to bottom, #FEF2F2, #F5F3FF); }
    /* Doodles everywhere */
    .stApp::before { content: ""; position: fixed; top: 10%; left: 5%; width: 80px; height: 80px; 
                     background-image: url('https://img.icons8.com/color/96/000000/pill.png'); opacity: 0.15; pointer-events: none; }
    .stApp::after { content: ""; position: fixed; bottom: 10%; right: 5%; width: 80px; height: 80px; 
                    background-image: url('https://img.icons8.com/color/96/000000/strawberry.png'); opacity: 0.15; pointer-events: none; }
    .window-container { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(10px); padding: 30px; border-radius: 25px; border: 1px solid #FCA5A5; }
    .pamper-box { background: #F3E8FF; padding: 20px; border-radius: 15px; border-left: 5px solid #7E22CE; margin-top: 15px; }
    .meal-box { background: white; padding: 15px; border-radius: 15px; border-left: 5px solid #F87171; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. LOGO WITH BIOLOGICAL FEMALE SIGN ---
st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <svg width="80" height="80" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" stroke="#991B1B" stroke-width="2" fill="none"/>
            <circle cx="50" cy="40" r="12" stroke="#991B1B" stroke-width="3" fill="none"/>
            <line x1="50" y1="52" x2="50" y2="75" stroke="#991B1B" stroke-width="3"/>
            <line x1="40" y1="65" x2="60" y2="65" stroke="#991B1B" stroke-width="3"/>
        </svg>
        <h1 style='font-family: "Alex Brush", cursive; color: #7F1D1D; font-size: 3rem;'>Shealth</h1>
    </div>
""", unsafe_allow_html=True)

if 'active_window' not in st.session_state: st.session_state.active_window = 1
def jump_to_window(w): st.session_state.active_window = w; st.rerun()

# --- 4. WINDOWS ---
if st.session_state.active_window == 1:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800", use_container_width=True)
    if st.button("Start My Journey"): jump_to_window(2)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 2:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.session_state.p_gender = st.radio("Gender", ["Female Profile", "Male Profile"])
    if st.button("Lock Profile"): jump_to_window(5)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 5:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("### 📅 30-Day Aesthetic Diet Plan")
    day = st.slider("Select Day", 1, 30, 1)
    st.markdown(f"""<div class='meal-box'><strong>Day {day} Breakfast:</strong> {'Paneer Oats Cheela' if day%2==0 else 'Sattu Porridge'}</div>""", unsafe_allow_html=True)
    if st.button("Go to Compliance"): jump_to_window(6)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 6:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("### 🚨 Adherence & Monthly Blues")
    
    # SPECIAL MONTHLY BLUES CHECKLIST
    if st.session_state.p_gender == "Female Profile":
        st.write("#### 📝 Monthly Blues Checklist")
        st.checkbox("Hydration Goal (3L)")
        st.checkbox("Mood Journaling")
        st.checkbox("Magnesium Rich Snack")
        
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
        
    if st.button("Reset"): jump_to_window(1)
    st.markdown("</div>", unsafe_allow_html=True)
