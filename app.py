import streamlit as st
import datetime

# --- 1. CORE SETUP ---
st.set_page_config(page_title="SHEALTH | AI Precision Coach", page_icon="🩸", layout="wide")

# --- 2. CSS & STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #FEF2F2; font-family: 'Plus Jakarta Sans', sans-serif; }
    .logo-container { text-align: center; padding: 20px; }
    .calligraphy-title { font-family: 'Alex Brush', cursive; font-size: 5rem; color: #7F1D1D; }
    .window-container { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    .pamper-box { background: #F3E8FF; padding: 15px; border-radius: 15px; border-left: 5px solid #7E22CE; }
    </style>
""", unsafe_allow_html=True)

# --- 3. STATE INITIALIZATION ---
if 'active_window' not in st.session_state: st.session_state.active_window = 1
if 'p_name' not in st.session_state: st.session_state.p_name = "Riya Sharma"
if 'p_gender' not in st.session_state: st.session_state.p_gender = "Female Profile"

# --- 4. NEW AESTHETIC LOGO ---
st.markdown("""
    <div class='logo-container'>
        <svg width="100" height="100" viewBox="0 0 100 100" fill="none">
            <circle cx="50" cy="50" r="45" stroke="#991B1B" stroke-width="2"/>
            <path d="M50 30 C 30 20, 20 40, 50 70 C 80 40, 70 20, 50 30" fill="#F87171" opacity="0.6"/>
            <text x="50" y="55" text-anchor="middle" font-family="Arial" font-size="12" fill="white">S</text>
        </svg>
        <div class='calligraphy-title'>Shealth</div>
    </div>
""", unsafe_allow_html=True)

# --- 5. NAVIGATION ---
def jump_to_window(w):
    st.session_state.active_window = w
    st.rerun()

# --- 6. PAGE LOGIC ---
if st.session_state.active_window == 1:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("Welcome to Shealth!")
    if st.button("Start Profile"): jump_to_window(2)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 2:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.session_state.p_name = st.text_input("Name", value=st.session_state.p_name)
    st.session_state.p_gender = st.radio("Gender", ["Female Profile", "Male Profile"])
    if st.button("Continue"): jump_to_window(6)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 6:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("### Compliance & Comfort")
    if st.session_state.p_gender == "Female Profile":
        st.markdown("""
        <div class='pamper-box'>
            <h4>🌸 The Cozy Reds Pamper Kit</h4>
            <ul>
                <li>Dark Chocolate: 'Chup-chap rehne ka mann'</li>
                <li>Comfort Essentials: 'Safe-side'</li>
                <li>Hot Water Bottle: 'Pet-dard ka asli sukoon'</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    if st.button("Reset"): jump_to_window(1)
    st.markdown("</div>", unsafe_allow_html=True)
