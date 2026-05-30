import streamlit as st
import datetime

# --- 1. CONFIG & AESTHETIC STYLING ---
st.set_page_config(page_title="SHEALTH | AI Precision", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');
    .stApp { background: linear-gradient(135deg, #FDF2F8 0%, #F5F3FF 50%, #FEF2F2 100%); }
    .calligraphy-title { font-family: 'Alex Brush', cursive; font-size: 5rem; color: #7F1D1D; text-align: center; }
    .window-container { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(15px); padding: 40px; border-radius: 30px; border: 1px solid #FCA5A5; }
    .meal-box { background: white; padding: 20px; border-radius: 15px; border-left: 6px solid #F87171; margin: 10px 0; }
    div.stButton > button { background: #991B1B; color: white; border-radius: 25px; padding: 10px 40px; border: none; display: block; margin: 0 auto; }
    </style>
""", unsafe_allow_html=True)

# --- 2. SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = 1

# --- 3. LOGO & HEADER ---
st.markdown("""
    <div style='text-align:center;'>
        <svg width="100" height="100" viewBox="0 0 100 100">
            <path d="M50 85C20 60 10 40 20 25C30 10 50 15 50 30C50 15 70 10 80 25C90 40 80 60 50 85Z" fill="#991B1B"/>
            <circle cx="50" cy="40" r="12" stroke="white" stroke-width="3" fill="none"/>
            <line x1="50" y1="52" x2="50" y2="75" stroke="white" stroke-width="3"/>
            <line x1="40" y1="65" x2="60" y2="65" stroke="white" stroke-width="3"/>
        </svg>
        <h1 class='calligraphy-title'>Shealth</h1>
    </div>
""", unsafe_allow_html=True)

# --- 4. NAVIGATION PAGES ---
def nav(p): st.session_state.page = p; st.rerun()

# Page 1: Landing
if st.session_state.page == 1:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200", use_container_width=True)
    if st.button("Enter Portal"): nav(2)
    st.markdown("</div>", unsafe_allow_html=True)

# Page 2: Registration
elif st.session_state.page == 2:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
        gender = st.radio("Gender", ["Female", "Male"])
    with col2:
        age = st.number_input("Age")
        loc = st.text_input("Location (Lucknow, etc.)")
    
    if gender == "Female": st.info("Monthly Cycle Tracking Activated")
    if st.button("Continue to BMI"): nav(3)
    st.markdown("</div>", unsafe_allow_html=True)

# Page 3: BMI & AI Intake
elif st.session_state.page == 3:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("### AI Intake")
    history = st.text_area("Medical History (Thyroid/PCOS/Diabetes)")
    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (cm)")
    if st.button("Generate Diet Plan"): nav(4)
    st.markdown("</div>", unsafe_allow_html=True)

# Page 4: 30-Day Diet & Exercise
elif st.session_state.page == 4:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    day = st.slider("Select Day", 1, 30, 1)
    st.markdown(f"<div class='meal-box'><strong>Day {day} Breakfast:</strong> {'Paneer Oats Cheela' if day%2==0 else 'Sattu Porridge'}</div>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400", caption="Daily Asana")
    if st.button("Next: Trackers"): nav(5)
    st.markdown("</div>", unsafe_allow_html=True)

# Page 5: Trackers & Founder
elif st.session_state.page == 5:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.write("### Trackers")
    st.slider("Water (Glasses)", 0, 16, 8)
    st.selectbox("Mood Tracker", ["Happy", "Calm", "Moody"])
    st.write("#### 🌸 Pamper List: Chocolate, Heat-Pad, Sanitary Kits")
    st.write("📍 **Near Pharmacy:** Apollo, Lucknow.")
    st.write("---")
    st.write("#### Founder: Maihwish Rizvi | Pharmacist")
    if st.button("Reset"): nav(1)
    st.markdown("</div>", unsafe_allow_html=True)
