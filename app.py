import streamlit as st
import pandas as pd
import datetime

# --- 1. CORE SYSTEM INITIALIZATION ---
st.set_page_config(page_title="SHEALTH | AI Precision Coach", page_icon="⚕️", layout="wide")

# --- CUSTOM HEROICON SVG DICTIONARY ---
def get_icon(path, color="#7F1D1D", size=24):
    return f"<svg style='width:{size}px; height:{size}px; vertical-align: middle; margin-right: 8px;' fill='none' stroke='{color}' viewBox='0 0 24 24'><path stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='{path}'></path></svg>"

ICONS = {
    "warning": get_icon("M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z", "#991B1B", 18),
    "clock": get_icon("M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z", "#B91C1C", 18),
    "heart": get_icon("M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z", "#991B1B", 18),
    "video": get_icon("M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z", "#7F1D1D", 28),
    "lock": get_icon("M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z", "#7F1D1D", 28),
    "clipboard": get_icon("M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01", "#7F1D1D", 28),
    "beaker": get_icon("M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z", "#7F1D1D", 28),
    "cpu": get_icon("M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z", "#7F1D1D", 28),
    "calendar": get_icon("M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z", "#7F1D1D", 28),
    "alert": get_icon("M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9", "#7F1D1D", 28),
    "building": get_icon("M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4", "#7F1D1D", 28),
    "user": get_icon("M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z", "#7F1D1D", 28),
    "map": get_icon("M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z M15 11a3 3 0 11-6 0 3 3 0 016 0z", "#7F1D1D", 28),
    "sparkles": get_icon("M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z", "#7F1D1D", 28)
}

def show_medical_disclaimer():
    st.markdown(f"""
        <div style='background-color: #FFF1F2; border: 1px solid #FDA4AF; padding: 12px; border-radius: 15px; margin-top: 25px; font-size: 0.75rem; color: #991B1B; text-align: center;'>
            <strong>{ICONS['warning']} Medical Disclaimer:</strong> This application provides AI-driven wellness suggestions and is for informational purposes only. 
            It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider 
            regarding your health or any medical condition.
        </div>
    """, unsafe_allow_html=True)

# Force scroll to top on every window switch (Streamlit specific hack)
st.components.v1.html(
    f"""
    <script>
        var body = window.parent.document.querySelector('.main');
        if (body) {{
            body.scrollTop = 0;
        }}
    </script>
    """,
    height=0
)

# --- 2. ELITE CLINICAL CRIMSON & PINTEREST BOTANICAL DOODLE CANVAS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap');
    
    .stApp {
        background-image: linear-gradient(to bottom, rgba(254, 242, 242, 0.88), rgba(252, 228, 228, 0.92)), 
                          url('https://images.unsplash.com/photo-1557672172-298e090bd0f1?w=1600');
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    
    .stApp::before {
        content: ""; position: fixed; top: 10%; left: 3%; width: 150px; height: 150px;
        background-image: url('https://img.icons8.com/external-icongeek26-outline-icongeek26/100/991B1B/external-pills-medical-icongeek26-outline-icongeek26.png');
        opacity: 0.14; pointer-events: none; z-index: 0;
    }
    .stApp::after {
        content: ""; position: fixed; bottom: 8%; right: 4%; width: 130px; height: 130px;
        background-image: url('https://img.icons8.com/external-flatart-icons-outline-flatarticons/100/991B1B/external-urology-medical-health-flatart-icons-outline-flatarticons.png');
        opacity: 0.15; pointer-events: none; z-index: 0;
    }
    
    html, body, [class*="css"], .stApp p, .stApp span, .stApp div, .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 { 
        font-family: 'Plus Jakarta Sans', sans-serif !important; 
        color: #451A1A !important; 
    }
    
    div[data-testid="stCodeBlock"] { background-color: #FEF2F2 !important; border: 1px dashed #FCA5A5 !important; }
    div[data-testid="stCodeBlock"] pre, div[data-testid="stCodeBlock"] code { color: #7F1D1D !important; background-color: transparent !important; }
    div[data-testid="stInfo"] { background-color: #FEF2F2 !important; color: #991B1B !important; }
    
    .stTextInput input, .stNumberInput input, div[data-testid="stSelectbox"] div { background-color: #ffffff !important; color: #451A1A !important; }
    
    div[data-testid="stExpander"] { background-color: rgba(255, 255, 255, 0.85) !important; border-radius: 12px; border: 1px solid #FCA5A5; }
    div[data-testid="stExpander"] details summary p { color: #7F1D1D !important; font-weight: 700 !important; }
    div[data-testid="stExpander"] details summary svg { color: #7F1D1D !important; fill: #7F1D1D !important; }

    .logo-container { text-align: center; margin-bottom: 2px; padding-top: 15px; }
    .calligraphy-title { font-family: 'Alex Brush', cursive; font-size: 5.6rem; color: #7F1D1D !important; font-weight: 600; line-height: 0.9; text-shadow: 2px 2px 4px rgba(153, 27, 27, 0.15); }
    .brand-subtitle { font-family: 'Plus Jakarta Sans', sans-serif; color: #991B1B !important; font-size: 0.95rem; font-weight: 700; text-align: center; text-transform: uppercase; letter-spacing: 5px; margin-bottom: 20px; }
    
    .time-capsule {
        background: rgba(255, 255, 255, 0.75); backdrop-filter: blur(8px); border: 1px solid rgba(254, 202, 202, 0.8);
        border-radius: 20px; padding: 8px 20px; font-weight: 700; color: #B91C1C; font-size: 0.9rem; text-align: center; max-width: 350px; margin: 0 auto 30px auto; box-shadow: 0 4px 15px rgba(153, 27, 27, 0.08);
    }
    .patient-vitals-badge {
        background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%); border: 1px solid #FCA5A5; border-radius: 14px; padding: 12px 20px; font-size: 0.88rem; color: #991B1B; font-weight: 600; text-align: center; max-width: 500px; margin: 0 auto 25px auto; box-shadow: 0 4px 12px rgba(153,27,27,0.05);
    }
    
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .window-container { 
        background-color: rgba(255, 255, 255, 0.74) !important; backdrop-filter: blur(22px) saturate(140%); border-radius: 30px; padding: 40px; border: 1px solid rgba(254, 202, 202, 0.6); box-shadow: 0 22px 50px rgba(185, 28, 28, 0.12); margin-top: 10px; margin-bottom: 30px; position: relative; animation: fadeIn 0.5s ease-in-out; opacity: 1;
    }
    
    .meal-box { background-color: rgba(255, 255, 255, 0.92); border-radius: 16px; padding: 20px; margin-bottom: 15px; border-left: 5px solid #F87171; box-shadow: 0 4px 15px rgba(153, 27, 27, 0.03); }
    .workout-box { background-color: rgba(255, 255, 255, 0.92); border-radius: 16px; padding: 20px; margin-bottom: 15px; border-left: 5px solid #EF4444; }
    .detox-badge { display: inline-block; padding: 6px 16px; background-color: #FEF2F2; color: #991B1B; border-radius: 20px; font-size: 0.78rem; font-weight: 700; margin-bottom: 12px; border: 1px solid #FEE2E2; }
    .provider-box { background-color: rgba(255, 255, 255, 0.85); border-radius: 14px; padding: 20px; border-left: 4px solid #991B1B; }
    .grocery-box { background-color: rgba(254, 242, 242, 0.85); padding: 18px; border-radius: 14px; border: 1px dashed #F87171; margin-top: 15px; }
    
    div.stButton > button {
        background: linear-gradient(135deg, #F87171 0%, #991B1B 100%) !important; color: white !important; font-weight: 700 !important; border-radius: 30px !important; border: none !important; padding: 12px 35px !important; font-size: 0.95rem !important; margin: 0 auto; display: block;
    }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #F87171, #991B1B) !important; }
    div[data-testid="stMetricValue"] { font-size: 2.2rem; font-weight: 700; color: #7F1D1D; font-family: 'Playfair Display', serif; }
    .trending-quote-banner { background: linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%); border: 1px dashed #FDA4AF; border-radius: 16px; padding: 15px; text-align: center; margin-top: 35px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. PREMIUM AESTHETIC GLASS RING EMBLEM LINE-ART LOGO ---
st.markdown("""
    <div class='logo-container'>
        <svg width="90" height="90" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0px 6px 14px rgba(219, 39, 119, 0.3));">
            <circle cx="50" cy="50" r="44" fill="white" fill-opacity="0.85"/>
            <circle cx="50" cy="50" r="41" stroke="#F472B6" stroke-width="1.5" stroke-dasharray="4 4"/>
            <path d="M50 32C42 22 28 26 28 42C28 58 45 70 50 74C55 70 72 58 72 42C72 26 58 22 50 32Z" stroke="#F472B6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="50" cy="40" r="8" stroke="#DB2777" stroke-width="3" fill="none"/>
            <line x1="50" y1="48" x2="50" y2="65" stroke="#DB2777" stroke-width="3" stroke-linecap="round"/>
            <line x1="42" y1="56" x2="58" y2="56" stroke="#DB2777" stroke-width="3" stroke-linecap="round"/>
        </svg>
        <div class='calligraphy-title'>Shealth</div>
    </div>
""", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>AI Precision Endocrine Alignment & 30-Day Lifecycle Coaching</p>", unsafe_allow_html=True)

# --- 4. DELHI (IST) CLOCK ALIGNMENT ---
now_utc = datetime.datetime.utcnow()
now_ist = now_utc + datetime.timedelta(hours=5, minutes=30)
formatted_date = now_ist.strftime("%A, %B %d, %Y")
formatted_time = now_ist.strftime("%I:%M %p")
st.markdown(f"<div class='time-capsule'>{ICONS['clock']} Delhi IST Track: {formatted_date} | {formatted_time}</div>", unsafe_allow_html=True)

# --- 5. DATA STATE INTEGRITY ROUTERS ---
if 'active_window' not in st.session_state: st.session_state.active_window = 1
if 'survey_score' not in st.session_state: st.session_state.survey_score = "General Wellness Track"
if 'target_goal' not in st.session_state: st.session_state.target_goal = "Weight Loss Deficit Track"

# RE-LOCKING SESSIONS
if 'p_name' not in st.session_state: st.session_state.p_name = "Riya Sharma"
if 'p_phone' not in st.session_state: st.session_state.p_phone = "+91 98765 43210"
if 'p_loc' not in st.session_state: st.session_state.p_loc = "Lucknow, Uttar Pradesh"
if 'p_region' not in st.session_state: st.session_state.p_region = "North India (Punjab/Haryana/UP)"
if 'p_age' not in st.session_state: st.session_state.p_age = 24
if 'p_weight' not in st.session_state: st.session_state.p_weight = 68.0
if 'p_height' not in st.session_state: st.session_state.p_height = 162.0
if 'p_gender' not in st.session_state: st.session_state.p_gender = "Female Profile"
if 'p_history' not in st.session_state: st.session_state.p_history = "None"
if 'p_cycle' not in st.session_state: st.session_state.p_cycle = 28
if 'p_reds_last' not in st.session_state: st.session_state.p_reds_last = now_ist.date() - datetime.timedelta(days=14)

def jump_to_window(window_id):
    st.session_state.active_window = window_id
    st.rerun()

def trigger_alarm_sound():
    sound_url = "https://www.orangefreesounds.com/wp-content/uploads/2022/04/Small-bell-ringing-short-sound-effect.mp3"
    st.audio(sound_url, autoplay=True)

if st.session_state.active_window > 2:
    st.markdown(f"""
        <div class='patient-vitals-badge'>
            {ICONS['heart']} Profile: {st.session_state.p_name} | {st.session_state.p_region} | Vitals: {st.session_state.p_weight}kg / {st.session_state.p_height}cm
        </div>
    """, unsafe_allow_html=True)

window_quotes = {
    1: "'Invest in your health, it pays the best biological interest.' &mdash; Stay Radiant",
    2: "'Self-care is a non-negotiable prescription. Your recovery journey initializes now.'",
    3: "'Listening to your body's subtle bio-signals is the highest form of self-love.'",
    4: "'Vitals are just coordinate data markers; consistency is where transformation lives.'",
    5: "'Eat to nourish your system cell-by-cell. You are entirely worth the commitment.'",
    6: "'Small daily adjustments build ultimate physiological resilience. Keep glowing!'"
}

# ==========================================
# WINDOW 1: PORTAL INTRODUCTION
# ==========================================
if st.session_state.active_window == 1:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=1200", caption="SHEALTH Clinical Culinary & Botanical Setup", use_container_width=True)
    
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D; text-align:center; margin-top:20px;'>Welcome to your Precision Metabolic Life-Science Environment</h3>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; font-size:1.05rem; line-height:1.7; max-width:850px; margin: 0 auto; color:#451A1A;'>
    <strong>SHEALTH</strong> is an advanced, high-tech AI-driven nutrient and diet coach wellness architecture engineered to resolve root endocrine variables. 
    By compiling baseline biological signatures, the ecosystem structures completely custom, daily-differentiated therapeutic regimes.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><hr style='border-color: #FCA5A5;'><br>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['video']} Daily Clinical Coaching Segment</h4>", unsafe_allow_html=True)
    v1, v2 = st.columns([1.6, 1])
    with v1:
       st.video("https://www.youtube.com/watch?v=T45Ca2VNYpQ")
    with v2:
        st.markdown("<h5 style='color: #7F1D1D; font-family: \"Playfair Display\", serif;'>Endocrine Pacing Models</h5>", unsafe_allow_html=True)
        st.write("Explore how steady adjustments in daily complex carbohydrate hierarchies stabilize internal metabolic curves.")
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Initialize Profile ➔"):
            jump_to_window(2)
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[1]}</div>", unsafe_allow_html=True)
    show_medical_disclaimer()
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 2: PATIENT REGISTRATION
# ==========================================
elif st.session_state.active_window == 2:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['lock']} Clinical Profile Registration Portal</h3>", unsafe_allow_html=True)
    
    r1, r2 = st.columns(2)
    with r1:
        in_name = st.text_input("Patient Full Name String:", value=st.session_state.p_name)
        in_phone = st.text_input("Active Verification Line:", value=st.session_state.p_phone)
        in_loc = st.text_input("Geographic Coordinate Base (City/State):", value=st.session_state.p_loc)
        in_region = st.selectbox("Select Your Native Culinary Region:", ["North India (Punjab/Haryana/UP)", "West India (Gujarat/Maharashtra/Rajasthan)", "South India (Kerala/Tamil Nadu/Karnataka)", "East India (Bengal/Odisha/Bihar)"], index=["North", "West", "South", "East"].index(st.session_state.p_region.split()[0]))
    with r2:
        in_age = st.number_input("Biological Age Value:", min_value=12, max_value=85, value=st.session_state.p_age)
        in_gender = st.radio("Dynamic Gender Profile Template:", ["Female Profile", "Male Profile"])
        in_weight = st.number_input("Core Mass Weight Field (kg):", min_value=30.0, max_value=190.0, value=st.session_state.p_weight)
        in_height = st.number_input("Core Axis Height Field (cm):", min_value=110.0, max_value=230.0, value=st.session_state.p_height)
        
    st.markdown("---")
    
    if in_gender == "Female Profile":
        st.markdown(f"<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['lock']} Discrete Biological Metric Logging</h4>", unsafe_allow_html=True)
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            in_reds = st.date_input("Approximate date of your last 'Monthly Reds':", value=st.session_state.p_reds_last)
        with col_c2:
            in_cycle = st.number_input("Average Cycle Length (Days):", min_value=20, max_value=45, value=st.session_state.p_cycle)
    else:
        in_reds = st.session_state.p_reds_last
        in_cycle = 28
        st.info("System Notification: Adaptive hormone tracking is currently configured to neutral baseline profiles.")
    
    st.markdown("---")
    in_history = st.text_area("Log active clinical prescriptions or metabolic history markers:", value=st.session_state.p_history)
    
    if st.button("Lock Profile ➔"):
        st.session_state.p_name, st.session_state.p_phone, st.session_state.p_loc, st.session_state.p_region = in_name, in_phone, in_loc, in_region
        st.session_state.p_age, st.session_state.p_gender, st.session_state.p_weight, st.session_state.p_height = in_age, in_gender, in_weight, in_height
        st.session_state.p_history, st.session_state.p_reds_last, st.session_state.p_cycle = in_history, in_reds, in_cycle
        jump_to_window(3)
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[2]}</div>", unsafe_allow_html=True)
    show_medical_disclaimer()
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 3: AUTOMATED CLINICAL INTAKE SCANNER
# ==========================================
elif st.session_state.active_window == 3:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['clipboard']} AI Symptom Stratification & Vector Intake Matrix</h3>", unsafe_allow_html=True)
    
    s1 = st.checkbox("1. Sudden weight shifts or high resistance to metabolic calorie deficits?")
    s2 = st.checkbox("2. Deep muscular exhaustion, systemic fatigue, or morning sluggishness profiles?")
    s3 = st.checkbox("3. Active hair volume reductions, facial flareups, or cystic flare clusters?")
    s4 = st.checkbox("4. Missing menstrual cycle parameters or deeply delayed hormonal schedules?")
    s5 = st.checkbox("5. Chronic internal room temperature sensitivities (feeling cold or unprovoked flushes)?")
    s6 = st.checkbox("6. Rapid mood shifts, nervous energy, or unexplained anxiety vectors?")
    s7 = st.checkbox("7. Intense late-night processing cravings for sweet or high-sodium foods?")
    s8 = st.checkbox("8. Musculoskeletal stiffness, waking joint discomfort, or localized aches?")
    s9 = st.checkbox("9. Under-eye edema, facial fluid retention, or localized dry patches?")
    s10 = st.checkbox("10. Diagnosed insulin processing disruptions or parental diabetic history records?")
    
    p_calc = (sum([s1, s3, s4, s6, s7, s10]) / 6) * 100
    t_calc = (sum([s1, s2, s5, s6, s8, s9]) / 6) * 100
    
    if p_calc == 0 and t_calc == 0: st.session_state.survey_score = "General Wellness Track"
    elif p_calc >= t_calc: st.session_state.survey_score = "PCOS Modification Matrix"
    else: st.session_state.survey_score = "Hypothyroidism Protocol Hub"
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Process Vectors ➔"):
        jump_to_window(4)
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[3]}</div>", unsafe_allow_html=True)
    show_medical_disclaimer()
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 4: BMI METRIC LAB & INTERACTIVE AI DIAGNOSTIC ENGINE
# ==========================================
elif st.session_state.active_window == 4:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['beaker']} Physical Biometrics Converter & AI Diagnostic Engine</h3>", unsafe_allow_html=True)
    
    with st.expander("Unit Converter Lab (Click for Conversion Matrices)", expanded=False):
        uc1, uc2 = st.columns(2)
        with uc1:
            lbs_in = st.number_input("Weight Input scale from Pounds (lbs):", value=float(st.session_state.p_weight * 2.20462))
            st.code(f"Parsed Metric Equivalence: {lbs_in / 2.20462:.1f} kg")
        with uc2:
            st.markdown("**Height Input scale from Feet/Inches:**")
            ft = st.number_input("Feet:", value=5)
            inch = st.number_input("Inches:", value=4)
            st.code(f"Parsed Metric Equivalence: {(ft * 30.48) + (inch * 2.54):.1f} cm")
            
    h_m = st.session_state.p_height / 100
    computed_bmi = st.session_state.p_weight / (h_m ** 2)
    
    st.markdown("---")
    st.markdown("<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>Clinical Mass Analysis Stratification</h4>", unsafe_allow_html=True)
    col_metric1, col_metric2 = st.columns([1, 2])
    with col_metric1:
        st.metric("Calculated Body Mass Index (BMI)", f"{computed_bmi:.1f}")
    with col_metric2:
        if computed_bmi < 18.5: bmi_status = "Underweight Baseline"
        elif 18.5 <= computed_bmi <= 24.9: bmi_status = "Optimal Homeostasis"
        elif 25.0 <= computed_bmi <= 29.9: bmi_status = "Overweight Matrix Burden"
        else: bmi_status = "Obese Clinical Stress"
        st.code(f"System Matrix Node Status: {bmi_status}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['cpu']} SHEALTH AI Real-time Intelligent Coaching Core</h4>", unsafe_allow_html=True)
    
    if "PCOS" in st.session_state.survey_score:
        ai_insight_text = f"Warning: Insulin sensitivity margins are compressed. Identified prior parameters: '{st.session_state.p_history}'. Recommendation: Implement clean complex carbohydrates to secure continuous baseline glucose boundaries safely."
    elif "Hypothyroidism" in st.session_state.survey_score:
        ai_insight_text = f"Detected reduced energetic output axes matching a thyroid cellular lag layer. Identified parameters: '{st.session_state.p_history}'. Recommendation: Focus on micronutrients containing natural Selenium to balance regulatory conversions."
    else:
        ai_insight_text = f"System coordinates verified within homeostatic ranges. Current operational tier: '{bmi_status}'. General maintenance parameters enabled successfully."
            
    st.info(f"AI Engine Response: {ai_insight_text}")
        
    st.markdown("<br><hr style='border-color: #FCA5A5;'><br>", unsafe_allow_html=True)
    st.session_state.target_goal = st.selectbox("Configure Targeted 30-Day Target Pathway Matrix:", ["Weight Loss Deficit Track", "Weight Gain Surplus Track"])
    
    if st.button("Compile Schedule ➔"):
        jump_to_window(5)
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[4]}</div>", unsafe_allow_html=True)
    show_medical_disclaimer()
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 5: THE 30-DAY CHALLENGE TARGET PLAN
# ==========================================
elif st.session_state.active_window == 5:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['calendar']} SHEALTH AI 30-Day Precision Challenge Tracker</h3>", unsafe_allow_html=True)
    st.write(f"Active Plan Mode: **{st.session_state.survey_score}** | Goal: **{st.session_state.target_goal}**")
    
    st.markdown("""
        <div class='doodle-center-box'>
            <svg width="45" height="45" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" fill="#991B1B" fill-opacity="0.15" stroke="#991B1B" stroke-width="1.5"/>
                <rect x="8" y="7" width="8" height="3" rx="1.5" fill="#991B1B"/>
            </svg>
            <div style='font-size:0.75rem; font-weight:700; color:#991B1B; text-transform:uppercase; margin-top:5px; letter-spacing:0.5px;'>AI Satvic Kitchen</div>
        </div>
    """, unsafe_allow_html=True)
    
    phase_tab = st.radio("Select Active 10-Day Phase Block:", ["Phase A (Days 1-10)", "Phase B (Days 11-20)", "Phase C (Days 21-30)"], horizontal=True)
    if "Phase A" in phase_tab: day_num = st.slider("Select Active Day Tracker Window:", 1, 10, 1); phase_offset = 0
    elif "Phase B" in phase_tab: day_num = st.slider("Select Active Day Tracker Window:", 11, 20, 11); phase_offset = 10
    else: day_num = st.slider("Select Active Day Tracker Window:", 21, 30, 21); phase_offset = 20

    hash_idx = day_num + phase_offset
    
    # REGION SPECIFIC DIET POOLS (All 60 original items restored & categorized)
    if "North" in st.session_state.p_region:
        veg_breakfast_pool = ["Paneer Oats Cheela", "Kashmiri Noon Chai with Almond Girda", "Sattu Porridge with Jaggery", "Sattu Stuffed Kachori", "Sidu with Lentil Mash", "Whole Wheat Dalia", "Chana Dal Steamed Fara", "Besan Onion Cheela", "Singhara Flour Crepe"]
        nonveg_breakfast_pool = ["Egg White Scramble Spinach Wrap", "Kashmiri Poached Eggs in Light Tomato Broth", "Mughlai Minced Chicken Toast", "Pahadi Herb Baked Omelet", "UP Style Masala Omelet Platter", "Kumaoni Herb Fried Eggs", "Haryanvi Ghee Egg White Scramble"]
        dinner_veg = ["Lauki Soup + 1 Bran Roti", "Moong Dal Khichdi", "Palak Paneer (Light) + Roti", "Tofu Matar Sabzi", "Chana Dal Fara", "Roasted Makhana Bowl"]
        dinner_nveg = ["Grilled Chicken Tikka + Salad", "Egg Curry + Roti", "Chicken Clear Soup", "Tandoori Fish + Broccoli", "Egg Stew", "Baked Fish"]
        
    elif "West" in st.session_state.p_region:
        veg_breakfast_pool = ["Methi Thepla with Curd", "Bajra Raab with Roasted Nuts", "Moong Dal Sprouts Chat", "Thalipeeth with Low Fat Butter", "Steamed Jowar Flakes", "Sprouted Chana Salad", "Roasted Makhana Porridge", "Buckwheat Khichdi"]
        nonveg_breakfast_pool = ["Egg Poha Infused with Turmeric", "Goan Egg Cafe-real Wrap", "Maharashtrian Anda Poha Plates", "Bhopali Minced Egg Toast", "Chhattisgarhi Egg Fara"]
        dinner_veg = ["Gujarati Kadhi + Brown Rice", "Varan Bhaat (Less Ghee)", "Bajra Roti + Baingan Bharta", "Usal + Salad", "Millet Flour Dumplings", "Soft Tofu Hash"]
        dinner_nveg = ["Fish Koliwada (Baked) + Salad", "Chicken Sukka (Dry) + Jowar Roti", "Egg Stew", "Goan Fish Curry (Light)", "Chicken Clear Soup", "Egg Pepper Fry"]
        
    elif "South" in st.session_state.p_region:
        veg_breakfast_pool = ["Puttu with Steamed Kadala", "Ragi Idli with Tomato Chutney", "Foxtail Millet Upma", "Pesarattu Mint Toast", "Akki Roti with Dill Leaves", "Finger Millet Gruel", "Malabar Neem Leaf Infusion Pancakes"]
        nonveg_breakfast_pool = ["Malabar Egg Roast with Whole Wheat Appam", "Tamil Nadu Egg Podimas with Curry Leaves", "Hyderabadi Chicken Keema Pattern Roll", "Andhra Spicy Egg White Omelet", "Mangalorean Egg Ghee Roast Whites", "Malabar Boiled Egg Podi Wrap"]
        dinner_veg = ["Bisi Bele Bath (Millet)", "Rasam + Brown Rice", "Vegetable Stew", "Avial + Red Rice", "Steamed Broccoli + Paneer", "Bottle Gourd Soup"]
        dinner_nveg = ["Chettinad Chicken (Less Oil) + Salad", "Meen Curry (Fish) + Red Rice", "Pepper Chicken Dry", "Egg Pepper Fry", "Seared Salmon", "Grilled Chicken Salad"]
        
    else: # East & North East
        veg_breakfast_pool = ["Brown Rice Flakes Poha", "Chhena Poda Slice", "Boiled Sweet Potatoes with Black Salt", "Bamboo Shoot Rice Cakes", "Sticky Rice Mash", "Millet Flour Dumplings"]
        nonveg_breakfast_pool = ["Assamese Egg Bor with Green Herbs", "Bengali Dim Bhurji with Mustard Hints", "Odisha Egg Masala Mash", "Bihari Egg Bhujia with Roasted Gram", "Naga Style Smoked Chicken Shreds", "Khasi Egg Veg Scramble", "Mizo Egg Stew Bowls", "Tripuri Boiled Egg Salad", "Sikkim Chicken Momos (Steamed)", "Jharkhand Desi Chicken Shreds", "Manipuri Fish Pepper Mash", "Arunachal Steamed Herbs Egg"]
        dinner_veg = ["Dalma (Lentil Veggie Mash)", "Shukto + Brown Rice", "Alo Bhaja (Air Fried) + Roti", "Mushroom Tarkari", "Soft Tofu Hash", "Moong Dal Khichdi"]
        dinner_nveg = ["Machher Jhol (Light Fish Curry)", "Chicken Dak Bungalow", "Egg Curry (Dim Kosha)", "Steamed Fish (Bhaapa Maach)", "Egg White Stew", "Baked Fish"]
    
    detox_drinks = ["Spearmint Herbal Flush", "Jeera Coriander Decoction", "Aloe Vera Ginger Shot", "Fennel Cleanse", "Mint Buttermilk", "Warm Lemon Water"]
    snacks_pool = ["Ayurvedic Kadha + Roasted Makhanas", "Warm Turmeric Milk + 4 Almonds", "Green Tea + Roasted Chana", "Mint Buttermilk + Flax Seeds", "Coconut Water + Chia Seeds", "Apple Slices + Peanut Butter"]
    
    v_b = veg_breakfast_pool[hash_idx % len(veg_breakfast_pool)]
    nv_b = nonveg_breakfast_pool[hash_idx % len(nonveg_breakfast_pool)]
    d_drink = detox_drinks[hash_idx % len(detox_drinks)]
    d_snack = snacks_pool[hash_idx % len(snacks_pool)]
    d_din_v = dinner_veg[hash_idx % len(dinner_veg)]
    d_din_nv = dinner_nveg[hash_idx % len(dinner_nveg)]
    
    workouts_loss = ["Low-Cortisol Bodyweight Squats: 3x15 reps + 20 min walk", "Wall Pushups: 3x12 reps + 15 min stepping", "Incline Slow Treadmill: 25 mins", "Tricep Chair Dips: 3x10 reps + 20 min stroll"]
    workouts_gain = ["Floor Glute Bridges: 4x12 reps", "Chair Assisted Squats: 3x10 reps", "Plank Alignment Core: 4x45s holds", "Dumbbell Overhead Presses: 3x12 reps"]
    
    if "Loss" in st.session_state.target_goal: active_workout_plan = workouts_loss[hash_idx % len(workouts_loss)]
    else: active_workout_plan = workouts_gain[hash_idx % len(workouts_gain)]
        
    yoga_asanas = [
        {"title": "Baddha Konasana", "desc": "Improves pelvic vascular vectors.", "img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400"},
        {"title": "Bhujangasana", "desc": "Lengthens core tracking systems.", "img": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400"}
    ]
    selected_yoga_block = yoga_asanas[hash_idx % len(yoga_asanas)]
    
    st.markdown(f"### {ICONS['clipboard']} Personal AI Curriculum Mapping Matrix: Day {day_num} Logs", unsafe_allow_html=True)
    st.info(f"Active Regional Palate Focus: {st.session_state.p_region.split()[0]} Core")
    
    with st.expander(f"Step 1: Morning Detox Elixir - Day {day_num}", expanded=True):
        st.markdown("<div class='detox-badge'>Active Fluid Infusion</div>", unsafe_allow_html=True)
        st.write(f"**Protocol:** Warmed {d_drink} administered empty-stomach.")
        
    with st.expander(f"Step 2: 4-Course Daily Culinary Layout - Day {day_num}", expanded=True):
        st.markdown(f"""
        <div class='meal-box'><strong>Course 1: Breakfast Target ({st.session_state.p_region.split()[0]})</strong><br>Veg: {v_b} <br>Non-Veg: {nv_b}</div>
        <div class='meal-box'><strong>Course 2: Mid-Day Lunch Alignment ({st.session_state.p_region.split()[0]})</strong><br>Veg: Lentil Stew + Seasonal Veg + Roti <br>Non-Veg: 150g {nv_b} + Green Salad</div>
        <div class='meal-box'><strong>Course 3: Evening Adrenal Vitality Snack</strong><br>{d_snack}</div>
        <div class='meal-box'><strong>Course 4: Restorative Night Repair Dinner</strong><br>Veg: {d_din_v} <br>Non-Veg: {d_din_nv}</div>
        """, unsafe_allow_html=True)
        
    with st.expander(f"Step 3: Shopping Manifest Basket - Day {day_num}", expanded=False):
        st.markdown(f"<div class='grocery-box'>✓ Required Active Ingredients Sourced from {st.session_state.p_region.split()[0]}: Regional Grains, Lentils, Spices, Mint leaves, Green Herbs.</div>", unsafe_allow_html=True)
        
    with st.expander(f"Step 4: Customized Exercise Blueprint - Day {day_num}", expanded=True):
        st.markdown(f"<div class='workout-box'><strong>Active Functional Training Routine:</strong><br>{active_workout_plan}</div>", unsafe_allow_html=True)
        
    with st.expander(f"Step 5: Labeled Yoga Asana Form Manual - Day {day_num}", expanded=False):
        ycol1, ycol2 = st.columns([1, 2])
        with ycol1:
            st.image(selected_yoga_block["img"], use_container_width=True, caption="Form Guidance Frame")
        with ycol2:
            st.markdown(f"##### **Asana Target: {selected_yoga_block['title']}**")
            st.write(selected_yoga_block["desc"])
            
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Compliance Center ➔"):
        jump_to_window(6)
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[5]}</div>", unsafe_allow_html=True)
    show_medical_disclaimer()
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 6: COMPLIANCE CORE & LOG ENVIRONMENT
# ==========================================
elif st.session_state.active_window == 6:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['alert']} Real-time Adherence Dashboards & Regional Provider Locator</h3>", unsafe_allow_html=True)
    
    w_baseline = float(st.session_state.p_weight * 0.035)
    
    hud1, hud2 = st.columns(2)
    with hud1:
        if st.session_state.p_gender == "Female Profile":
            today_date = datetime.date.today()
            cycle_len = st.session_state.p_cycle
            days_diff = (today_date - st.session_state.p_reds_last).days
            
            if days_diff < 0:
                days_until_next_reds = abs(days_diff) % cycle_len
            else:
                days_until_next_reds = (cycle_len - (days_diff % cycle_len))
                if days_until_next_reds == cycle_len: days_until_next_reds = 0
            
            st.markdown(f"<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['lock']} Private Dynamic 'Monthly Reds' Forecast</h4>", unsafe_allow_html=True)
            st.markdown(f"""
            <div style='background-color:#FFF5F5; padding:20px; border-radius:15px; border-left:5px solid #DC2626; margin-bottom:20px;'>
                <p style='margin:0; font-weight:700; color:#991B1B; font-size:1.1rem;'>Estimated Next Secure Window Arrival</p>
                <p style='font-size:2rem; font-weight:800; color:#7F1D1D; margin:10px 0;'>{days_until_next_reds} Days Remaining</p>
                <p style='font-size:0.9rem; color:#451A1A; margin:0;'>
                    <strong>AI Tracker Advice:</strong> 
                    {"Prioritize cellular recovery and include roasted makhana to balance micro-cravings safely as vectors shift." if days_until_next_reds <= 7 else "Energy parameters are stable. Optimal window to execute Alternate Squat progressions."}
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("---")
            
        st.markdown(f"<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['clock']} Precision AI Interactive Audio Alarms</h4>", unsafe_allow_html=True)
        st.caption(f"Alarm Core synced with Delhi IST: **{formatted_time}**")
        
        wat_alarm = st.checkbox("Water Tracker Notification (Recommended short bell sync)")
        med_alarm = st.checkbox("Active Hormone Prescription Alarm (Fasting Schedule Sync)")
        if wat_alarm or med_alarm: trigger_alarm_sound()
        
        st.markdown("---")
        st.markdown(f"<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['beaker']} Multi-Food Caloric Dictionary Index Lookups</h4>", unsafe_allow_html=True)
        f_select = st.selectbox("Search Indian Food Items Base Matrix:", ["1 Wheat Chapati", "100g Paneer Bhurji", "1 Bowl Moong Dal Khichdi", "1 Whole Boiled Egg", "100g Chicken Breast (Grilled)", "1 Roasted Papad", "1 Bowl Green Sabzi"])
        cal_index = {"1 Wheat Chapati": "85 kcal", "100g Paneer Bhurji": "190 kcal", "1 Bowl Moong Dal Khichdi": "220 kcal", "1 Whole Boiled Egg": "78 kcal", "100g Chicken Breast (Grilled)": "165 kcal", "1 Roasted Papad": "35 kcal", "1 Bowl Green Sabzi": "95 kcal"}
        st.code(f"Database Caloric Core Value: {cal_index[f_select]}")
        
        st.markdown("---")
        st.markdown(f"<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['sparkles']} Mood-Aware Pamper Hub</h4>", unsafe_allow_html=True)
        mood_data = {
            "Happy": ["Gratitude Journaling", "Post a positive update", "Healthy Smoothie"],
            "Calm": ["Read a book", "Chamomile Herbal Tea", "Light Stretching"],
            "Tensed": ["Dark Chocolate (Magnesium)", "Warm Water Bottle", "Deep Breathing Exercises"],
            "Moody": ["Sanitary Essentials", "Warm Blanket", "Comfort Food"]
        }
        selected_mood = st.selectbox("How is your system feeling today?", list(mood_data.keys()))
        with st.expander(f"Pamper Bucket for {selected_mood} Mood", expanded=True):
            for item in mood_data[selected_mood]: st.markdown(f"**✓ {item}**")
        
        st.markdown("---")
        st.markdown(f"<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['beaker']} Hydration Multiplier Tracker Progress</h4>", unsafe_allow_html=True)
        gl_drunk = st.slider("Glasses consumed today (250ml units):", 0, 16, 4)
        total_liters = gl_drunk * 0.25
        st.progress(min(total_liters / w_baseline, 1.0))
        st.write(f"Logged Status: **{total_liters:.2f} L** out of calculated target **{w_baseline:.1f} L**")
        
    with hud2:
        st.markdown(f"<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>{ICONS['map']} Satellite Healthcare Provider Locator Grid</h4>", unsafe_allow_html=True)
        st.info(f"Active Geolocation Lock Signal: Verified within {st.session_state.p_loc} Perimeter Networks")
        
        st.markdown("##### Closest Specialized Diagnostics & Emergency Nodes found:")
        st.markdown(f"""
        <div class='provider-box'>
            <strong>{ICONS['building']} Apollo Diagnostic Healthcare Center & Endocrine Hub</strong><br>
            Location Ward Coordinates: Regional Peripheral Ward, {st.session_state.p_loc.split(',')[0]} • Specialized Clinical Testing Wing Active
        </div>
        <div class='provider-box' style='margin-top: 10px;'>
            <strong>{ICONS['building']} Apollo Pharmacy 24x7 Retail Counter Outlets</strong><br>
            Distance Matrix: 0.7 km away • Synced with state pharmacist prescription networks for specialized hormonal therapeutics
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color: #FCA5A5;'><br>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='founder-card' style='background: linear-gradient(135deg, rgba(254, 242, 242, 0.9) 0%, rgba(254, 226, 226, 0.9) 100%) !important; padding: 30px; border-radius: 20px; border: 1px solid #FCA5A5;'>
        <h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D; margin-top:0;'>{ICONS['user']} Clinical Product System Architecture</h3>
        <h4 style='color: #991B1B; margin-top:5px; font-weight:600; letter-spacing:0.5px;'>Maihwish Rizvi | Registered Pharmacist</h4>
        <p style='line-height:1.6; font-size:0.95rem; color:#451A1A; margin-top:12px;'>
            As a <strong>Registered Pharmacist</strong>, my formal clinical evaluation training allows me to design user-friendly wellness products 
            that bypass superficial fitness trends to target actual baseline neuroendocrine mechanisms. By pairing 30-day dynamic life-science 
            calibrations with a rich, comforting <strong>Indian culinary palate</strong>, SHEALTH presents a high-tech healthcare platform 
            engineered for rigorous daily patient safety and compliance tracking protocols.
        </p>
        <hr style='border-color: #FCA5A5; margin: 15px 0;'>
        <p style='font-size:0.8rem; color:#991B1B; margin:0;'><strong>Active Session Demographic Registry Details:</strong> Patient Name: {st.session_state.p_name} • Contact Token: {st.session_state.p_phone} • Diagnostics History Log: {st.session_state.p_history}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⟲ Reset Session"):
        st.session_state.active_window = 1
        st.rerun()
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[6]}</div>", unsafe_allow_html=True)
    show_medical_disclaimer()
    st.markdown("</div>", unsafe_allow_html=True)