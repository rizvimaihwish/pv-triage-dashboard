import streamlit as st
import datetime

# --- 1. CORE SETUP ---
st.set_page_config(page_title="SHEALTH | AI Precision Coach", page_icon="🔮", layout="wide")

# --- 2. GLOBAL STYLES (Doodles & Aesthetics) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&family=Plus+Jakarta+Sans&display=swap');
    .stApp { background-image: linear-gradient(to bottom, rgba(254, 242, 242, 0.88), rgba(245, 243, 255, 0.92)); }
    .logo-container { text-align: center; padding: 20px; }
    .calligraphy-title { font-family: 'Alex Brush', cursive; font-size: 5rem; color: #7F1D1D; }
    .window-container { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(15px); padding: 30px; border-radius: 20px; border: 1px solid #FCA5A5; }
    .pamper-box { background: #F3E8FF; padding: 20px; border-radius: 15px; border-left: 5px solid #7E22CE; margin-top: 15px; }
    .meal-box { background: white; padding: 15px; border-radius: 15px; border-left: 5px solid #F87171; margin-bottom: 10px; }
    .stButton > button { background: #991B1B; color: white; border-radius: 20px; padding: 10px 25px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. STATE INITIALIZATION ---
if 'active_window' not in st.session_state: st.session_state.active_window = 1
if 'p_gender' not in st.session_state: st.session_state.p_gender = "Female Profile"
if 'p_weight' not in st.session_state: st.session_state.p_weight = 68.0

# --- 4. LOGO WITH FEMALE SIGN ---
st.markdown("""
    <div class='logo-container'>
        <svg width="100" height="100" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" stroke="#991B1B" stroke-width="2" fill="none"/>
            <circle cx="50" cy="40" r="12" stroke="#991B1B" stroke-width="3" fill="none"/>
            <line x1="50" y1="52" x2="50" y2="75" stroke="#991B1B" stroke-width="3"/>
            <line x1="40" y1="65" x2="60" y2="65" stroke="#991B1B" stroke-width="3"/>
        </svg>
        <div class='calligraphy-title'>Shealth</div>
    </div>
""", unsafe_allow_html=True)

def jump_to_window(w): st.session_state.active_window = w; st.rerun()

# --- 5. WINDOWS ---
if st.session_state.active_window == 1:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800", use_container_width=True)
    if st.button("Start My Journey"): jump_to_window(2)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 2:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.session_state.p_gender = st.radio("Profile", ["Female Profile", "Male Profile"])
    if st.button("Continue"): jump_to_window(5)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 5:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    day = st.slider("Select Day", 1, 30, 1)
    st.markdown(f"### Day {day} Meal Plan")
    st.markdown(f"""
    <div class='meal-box'><strong>Breakfast ({'Desi' if day%2==0 else 'Fusion'}):</strong> {'Paneer Oats Cheela' if day%2==0 else 'Sattu Porridge'}</div>
    <div class='meal-box'><strong>Lunch:</strong> Lentil Stew + Seasonal Veg + Bran Roti</div>
    <div class='meal-box'><strong>Dinner:</strong> Grilled Protein + Charred Broccoli</div>
    """, unsafe_allow_html=True)
    if st.button("Compliance Center"): jump_to_window(6)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_window == 6:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("### 🚨 Adherence Dashboard")
    
    # WATER TRACKER
    gl = st.slider("Glasses of water today", 0, 16, 4)
    st.progress(gl/12)
    
    # MEDICINE ALARM
    if st.checkbox("💊 Active Hormone Prescription Alarm"):
        st.success("Alarm set for IST Schedule!")
    
    # PAMPER KIT
    if st.session_state.p_gender == "Female Profile":
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
        
    if st.button("Reset Session"): jump_to_window(1)
    st.markdown("</div>", unsafe_allow_html=True)
