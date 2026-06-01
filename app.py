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
    
    /* -------------------------------------------------------------
       CRITICAL DARK MODE OVERRIDES & ICON PROTECTION
       ------------------------------------------------------------- */
    html, body, .stApp p, .stApp div, .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 { 
        font-family: 'Plus Jakarta Sans', sans-serif !important; 
        color: #451A1A !important; 
    }
    
    /* Restore Streamlit UI Icons (Fixes the _arr overlap glitch) */
    span.material-symbols-rounded, span[class*="icon"] {
        font-family: 'Material Symbols Rounded', 'Material Icons' !important;
    }
    
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
            in_reds = st.date_input("Approximate date of your last 'Monthly Reds':", value=st.session_state.p_reds_last
