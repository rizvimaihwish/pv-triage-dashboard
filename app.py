import streamlit as st
import pandas as pd
import datetime

# --- 1. CORE SYSTEM INITIALIZATION ---
st.set_page_config(page_title="SHEALTH | AI Precision Coach", page_icon="🩸", layout="wide")

# --- 2. ELITE MEDICAL CRIMSON & BOTANICAL GLASSMORPHIC STYLE SHEET ---
st.markdown("""
    <style>
    @import url('https://fonts.unsplash.com/css2?family=Alex+Brush&family=Playfair+Display:ital,wght=0,400..900;1,400..900&family=Plus+Jakarta+Sans:ital,wght=0,200..800;1,200..800&display=swap');
    
    /* Immersive Crimson & Rose Mist Clinical Wallpaper Canvas */
    .stApp {
        background-image: linear-gradient(to bottom, rgba(254, 242, 242, 0.88), rgba(252, 228, 228, 0.92)), 
                          url('https://images.unsplash.com/photo-1557672172-298e090bd0f1?w=1600');
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    
    /* Precision Pharmacological & Anatomical Doodles Watermarks */
    .stApp::before {
        content: ""; position: fixed; top: 12%; left: 4%; width: 140px; height: 140px;
        background-image: url('https://img.icons8.com/external-flatart-icons-outline-flatarticons/100/991B1B/external-urology-medical-health-flatart-icons-outline-flatarticons.png');
        opacity: 0.12; pointer-events: none; z-index: 0;
    }
    .stApp::after {
        content: ""; position: fixed; bottom: 10%; right: 5%; width: 120px; height: 120px;
        background-image: url('https://img.icons8.com/external-icongeek26-outline-icongeek26/100/991B1B/external-pills-medical-icongeek26-outline-icongeek26.png');
        opacity: 0.15; pointer-events: none; z-index: 0;
    }
    
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; color: #451A1A; }
    
    /* Calligraphed Luxury HEADING - SHEALTH Crimson Gold Branding */
    .logo-container { text-align: center; margin-bottom: 2px; padding-top: 15px; }
    .calligraphy-title { font-family: 'Alex Brush', cursive; font-size: 5.6rem; color: #7F1D1D; font-weight: 600; line-height: 0.9; text-shadow: 2px 2px 4px rgba(153, 27, 27, 0.15); }
    .brand-subtitle { font-family: 'Plus Jakarta Sans', sans-serif; color: #991B1B; font-size: 0.95rem; font-weight: 700; text-align: center; text-transform: uppercase; letter-spacing: 5px; margin-bottom: 20px; }
    
    /* Live IST Time Badge Style */
    .time-capsule {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(254, 202, 202, 0.8);
        border-radius: 20px; padding: 8px 20px; font-weight: 700; color: #B91C1C; font-size: 0.9rem; text-align: center; max-width: 350px; margin: 0 auto 30px auto;
        box-shadow: 0 4px 15px rgba(153, 27, 27, 0.08);
    }

    /* Patient Vitals Micro Badge */
    .patient-vitals-badge {
        background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
        border: 1px solid #FCA5A5; border-radius: 14px; padding: 12px 20px;
        font-size: 0.88rem; color: #991B1B; font-weight: 600; text-align: center;
        max-width: 500px; margin: 0 auto 25px auto; box-shadow: 0 4px 12px rgba(153,27,27,0.05);
    }
    
    /* Frosted Amethyst-Garnet Glassmorphic Core Panels */
    .window-container { 
        background-color: rgba(255, 255, 255, 0.74) !important; 
        backdrop-filter: blur(22px) saturate(140%); 
        border-radius: 30px; padding: 40px; 
        border: 1px solid rgba(254, 202, 202, 0.6); 
        box-shadow: 0 22px 50px rgba(185, 28, 28, 0.12); 
        margin-bottom: 30px; position: relative;
    }
    
    .window-container::after {
        content: ""; position: absolute; top: 20px; right: 25px; width: 50px; height: 50px;
        background-image: url('https://img.icons8.com/ios/50/991B1B/thyroid.png');
        opacity: 0.12; pointer-events: none;
    }

    /* Cute Micro Aesthetic Center Doodle Layout */
    .doodle-center-box {
        text-align: center; margin: 15px auto 25px auto; padding: 15px;
        background: rgba(255, 255, 255, 0.6); border-radius: 20px; max-width: 180px;
        border: 1px solid rgba(254, 202, 202, 0.5);
    }

    /* Girly Trending Quote Banner */
    .trending-quote-banner {
        background: linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%);
        border: 1px dashed #FDA4AF; border-radius: 16px; padding: 15px;
        font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.05rem;
        color: #9F1239; text-align: center; margin-top: 35px; box-shadow: 0 4px 12px rgba(225,29,72,0.04);
    }
    
    .meal-box { background-color: rgba(255, 255, 255, 0.92); border-radius: 16px; padding: 20px; margin-bottom: 15px; border-left: 5px solid #F87171; box-shadow: 0 4px 15px rgba(153, 27, 27, 0.03); }
    .workout-box { background-color: rgba(255, 255, 255, 0.92); border-radius: 16px; padding: 20px; margin-bottom: 15px; border-left: 5px solid #EF4444; box-shadow: 0 4px 15px rgba(153, 27, 27, 0.03); }
    .detox-badge { display: inline-block; padding: 6px 16px; background-color: #FEF2F2; color: #991B1B; border-radius: 20px; font-size: 0.78rem; font-weight: 700; margin-bottom: 12px; letter-spacing: 0.5px; text-transform: uppercase; border: 1px solid #FEE2E2; }
    .provider-box { background-color: rgba(255, 255, 255, 0.85); border-radius: 14px; padding: 20px; border-left: 4px solid #991B1B; }
    .grocery-box { background-color: rgba(254, 242, 242, 0.85); padding: 18px; border-radius: 14px; border: 1px dashed #F87171; margin-top: 15px; }
    
    /* Sleek, Compact Action Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #F87171 0%, #991B1B 100%) !important;
        color: white !important; font-weight: 700 !important; border-radius: 30px !important;
        border: none !important; padding: 12px 30px !important; font-size: 0.95rem !important; letter-spacing: 0.5px;
        box-shadow: 0 6px 20px rgba(153, 27, 27, 0.25) !important; transition: all 0.3s ease !important;
        display: block; margin: 0 auto; width: auto; max-width: 280px; text-align: center;
        white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }
    div.stButton > button:hover { transform: translateY(-2px) scale(1.01) !important; box-shadow: 0 10px 25px rgba(153, 27, 27, 0.4) !important; }
    
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #F87171, #991B1B) !important; }
    div[data-testid="stMetricValue"] { font-size: 2.2rem; font-weight: 700; color: #7F1D1D; font-family: 'Playfair Display', serif; }
    div[data-testid="stMetricLabel"] { font-size: 0.85rem; font-weight: 700; color: #991B1B; text-transform: uppercase; letter-spacing: 1px; }
    div[data-testid="stMetric"] { background-color: rgba(255, 255, 255, 0.88) !important; backdrop-filter: blur(6px); border-radius: 18px; padding: 18px; border: 1px solid rgba(254,202,202,0.4); }
    </style>
""", unsafe_allow_html=True)

# --- 3. INLINE SVG LOGO EMBLEM DESIGN LAYER ---
st.markdown("""
    <div class='logo-container'>
        <svg width="95" height="95" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0px 5px 12px rgba(153,27,27,0.3));">
            <rect x="8" y="8" width="84" height="84" rx="26" fill="white" fill-opacity="0.8"/>
            <rect x="11" y="11" width="78" height="78" rx="23" stroke="url(#crimson_grad)" stroke-width="2" stroke-dasharray="5 3"/>
            <path d="M50 24C44 32 32 38 32 54C32 64 40 72 50 72C60 72 68 64 68 54C68 38 56 32 50 24Z" fill="url(#crimson_grad)" fill-opacity="0.15" stroke="url(#crimson_grad)" stroke-width="1.5"/>
            <path d="M42 46C46 44 54 44 58 46M40 54C45 52 55 52 60 54" stroke="#991B1B" stroke-width="2.5" stroke-linecap="round"/>
            <rect x="44" y="48" width="12" height="6" rx="3" fill="#7F1D1D"/>
            <circle cx="50" cy="40" r="3" fill="#B91C1C"/>
            <defs>
                <linearGradient id="crimson_grad" x1="0" y1="0" x2="100" y2="100" gradientUnits="userSpaceOnUse">
                    <stop offset="0%" stop-color="#F87171"/>
                    <stop offset="50%" stop-color="#EF4444"/>
                    <stop offset="100%" stop-color="#991B1B"/>
                </linearGradient>
            </defs>
        </svg>
        <div class='calligraphy-title'>Shealth</div>
    </div>
""", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>AI Precision Endocrine Alignment & 30-Day Lifecycle Coaching</p>", unsafe_allow_html=True)

# --- 4. REAL-TIME CALIBRATED DELHI IST TIME STAMP CORE ---
now_utc = datetime.datetime.utcnow()
now_ist = now_utc + datetime.timedelta(hours=5, minutes=30)
formatted_date = now_ist.strftime("%A, %B %d, %Y")
formatted_time = now_ist.strftime("%I:%M %p")
st.markdown(f"<div class='time-capsule'>⏱️ Delhi IST Track: {formatted_date} | {formatted_time}</div>", unsafe_allow_html=True)

# --- 5. PLATFORM CORE ARCHITECTURE STATES ---
if 'active_window' not in st.session_state: st.session_state.active_window = 1
if 'survey_score' not in st.session_state: st.session_state.survey_score = "General Wellness Track"
if 'target_goal' not in st.session_state: st.session_state.target_goal = "Weight Loss Deficit Track"

# PERMANENT SURVEILLANCE DATA CACHE CORES
if 'p_name' not in st.session_state: st.session_state.p_name = "Riya Sharma"
if 'p_phone' not in st.session_state: st.session_state.p_phone = "+91 98765 43210"
if 'p_loc' not in st.session_state: st.session_state.p_loc = "Lucknow, Uttar Pradesh"
if 'p_age' not in st.session_state: st.session_state.p_age = 24
if 'p_weight' not in st.session_state: st.session_state.p_weight = 68.0
if 'p_height' not in st.session_state: st.session_state.p_height = 162.0
if 'p_gender' not in st.session_state: st.session_state.p_gender = "Female Profile"
if 'p_history' not in st.session_state: st.session_state.p_history = "None"
if 'p_reds_last' not in st.session_state: st.session_state.p_reds_last = datetime.date.today() - datetime.timedelta(days=14)

def jump_to_window(window_id):
    st.session_state.active_window = window_id
    st.rerun()

def trigger_alarm_sound():
    sound_url = "https://www.orangefreesounds.com/wp-content/uploads/2022/04/Small-bell-ringing-short-sound-effect.mp3"
    st.audio(sound_url, autoplay=True)

# ACTIVE PROFILE USER HEADS-UP CARD RENDER
if st.session_state.active_window > 2:
    st.markdown(f"""
        <div class='patient-vitals-badge'>
            &nbsp;🩺 Profile Ledger: {st.session_state.p_name} | Axis: {st.session_state.p_gender} | Vitals: {st.session_state.p_weight}kg / {st.session_state.p_height}cm
        </div>
    """, unsafe_allow_html=True)

# Static window tracking quotes database list
window_quotes = {
    1: "🌸 'Invest in your health, it pays the best biological interest.' &mdash; Stay Radiant",
    2: "✨ 'Self-care is a non-negotiable prescription. Your recovery journey initializes now.'",
    3: "🔮 'Listening to your body's subtle bio-signals is the highest form of self-love.'",
    4: "📏 'Vitals are just coordinate data markers; consistency is where transformation lives.'",
    5: "🍱 'Eat to nourish your system cell-by-cell. You are entirely worth the commitment.'",
    6: "⏰ 'Small daily alarms build ultimate physiological resilience. Keep glowing, queen!'"
}

# ==========================================
# WINDOW 1: PORTAL INTRODUCTION
# ==========================================
if st.session_state.active_window == 1:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200", use_container_width=True)
    
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D; text-align:center;'>Welcome to your Precision Metabolic Life-Science Environment</h3>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; font-size:1.05rem; line-height:1.7; max-width:850px; margin: 0 auto; color:#451A1A;'>
    <strong>SHEALTH</strong> is an advanced, high-tech AI-driven nutrient and diet coach wellness architecture engineered to resolve root endocrine variables. 
    By compiling baseline biological signatures, the ecosystem structures completely custom, daily-differentiated therapeutic regimes and 
    low-impact functional workouts adapted beautifully for your recovery parameters.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><hr style='border-color: #FCA5A5;'><br>", unsafe_allow_html=True)
    st.markdown("<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>🎥 Daily Clinical Coaching Segment</h4>", unsafe_allow_html=True)
    v1, v2 = st.columns([1.6, 1])
    with v1:
        st.video("https://www.youtube.com/watch?v=ScZs7L0_S38")
    with v2:
        st.markdown("<h5 style='color: #7F1D1D; font-family: \"Playfair Display\", serif;'>Endocrine Pacing Models</h5>", unsafe_allow_html=True)
        st.write("Explore how steady adjustments in daily complex carbohydrate hierarchies stabilize internal metabolic curves. Learn to map low-impact skeletal movements to safely process high system loads without inducing central fatigue lines.")
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("✨ Initialize Profile"):
            jump_to_window(2)
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[1]}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 2: PATIENT REGISTRATION WITH FILTER LOCKS
# ==========================================
elif st.session_state.active_window == 2:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>🔒 Clinical Profile Registration Portal</h3>", unsafe_allow_html=True)
    
    r1, r2 = st.columns(2)
    with r1:
        in_name = st.text_input("Patient Full Name String:", value=st.session_state.p_name)
        in_phone = st.text_input("Active Verification Line:", value=st.session_state.p_phone)
        in_loc = st.text_input("Geographic Coordinate Base (City/State):", value=st.session_state.p_loc)
    with r2:
        in_age = st.number_input("Biological Age Value:", min_value=12, max_value=85, value=st.session_state.p_age)
        in_gender = st.radio("Dynamic Gender Profile Template:", ["Female Profile", "Male Profile"])
        in_weight = st.number_input("Core Mass Weight Field (kg):", min_value=30.0, max_value=190.0, value=st.session_state.p_weight)
        in_height = st.number_input("Core Axis Height Field (cm):", min_value=110.0, max_value=230.0, value=st.session_state.p_height)
        
    st.markdown("---")
    
    if in_gender == "Female Profile":
        st.markdown("<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>🔒 Discrete Biological Metric Logging</h4>", unsafe_allow_html=True)
        in_reds = st.date_input("Select the approximate anchor date of your last 'Monthly Reds' window sequence:", value=st.session_state.p_reds_last)
    else:
        in_reds = st.session_state.p_reds_last
        st.info("System Notification: Adaptive hormone tracking is currently configured to neutral baseline profiles.")
    
    st.markdown("---")
    st.markdown("<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>📋 Prior Diagnoses & Medication Overlays</h4>", unsafe_allow_html=True)
    in_history = st.text_area("Log active clinical prescriptions or metabolic history markers:", value=st.session_state.p_history)
    
    if st.button("🚀 Lock Profile"):
        st.session_state.p_name = in_name
        st.session_state.p_phone = in_phone
        st.session_state.p_loc = in_loc
        st.session_state.p_age = in_age
        st.session_state.p_gender = in_gender
        st.session_state.p_weight = in_weight
        st.session_state.p_height = in_height
        st.session_state.p_history = in_history
        st.session_state.p_reds_last = in_reds
        jump_to_window(3)
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[2]}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 3: AUTOMATED CLINICAL INTAKE SCANNER
# ==========================================
elif st.session_state.active_window == 3:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>📋 AI Symptom Stratification & Vector Intake Matrix</h3>", unsafe_allow_html=True)
    
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
    if st.button("✨ Process Vectors"):
        jump_to_window(4)
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[3]}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 4: BMI METRIC LAB & INTERACTIVE AI DIAGNOSTIC ENGINE
# ==========================================
elif st.session_state.active_window == 4:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>📐 Physical Biometrics Converter & AI Diagnostic Engine</h3>", unsafe_allow_html=True)
    
    with st.expander("🔄 Unit Converter Lab (Push Up/Down for Conversion Matrices)", expanded=False):
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
        st.metric("Your Calculated Body Mass Index (BMI)", f"{computed_bmi:.1f}")
    with col_metric2:
        if computed_bmi < 18.5: bmi_status = "Underweight Baseline"
        elif 18.5 <= computed_bmi <= 24.9: bmi_status = "Optimal Homeostasis"
        elif 25.0 <= computed_bmi <= 29.9: bmi_status = "Overweight Matrix Burden"
        else: bmi_status = "Obese Clinical Stress"
        st.code(f"System Matrix Node Status: {bmi_status}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>🤖 SHEALTH AI Real-time Intelligent Coaching Core</h4>", unsafe_allow_html=True)
    
    if "PCOS" in st.session_state.survey_score:
        ai_insight_text = f"Warning: Insulin sensitivity margins are compressed. Identified prior parameters: '{st.session_state.p_history}'. Recommendation: Implement clean complex carbohydrates to secure continuous baseline glucose boundaries safely."
    elif "Hypothyroidism" in st.session_state.survey_score:
        ai_insight_text = f"Detected reduced energetic output axes matching a thyroid cellular lag layer. Identified parameters: '{st.session_state.p_history}'. Recommendation: Focus on micronutrients containing natural Selenium to balance regulatory conversions."
    else:
        ai_insight_text = f"System coordinates verified within homeostatic ranges. Current operational tier: '{bmi_status}'. General maintenance parameters enabled successfully."
            
    st.info(f"✨ **AI Engine Response:** {ai_insight_text}")
        
    st.markdown("<br><hr style='border-color: #FCA5A5;'><br>", unsafe_allow_html=True)
    st.session_state.target_goal = st.selectbox("Configure Targeted 30-Day Target Pathway Matrix:", ["Weight Loss Deficit Track", "Weight Gain Surplus Track"])
    
    if st.button("🎯 Compile Schedule"):
        jump_to_window(5)
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[4]}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 5: THE 30-DAY CHALLENGE TARGET PLAN (100% Unique Indian Regional Dishes Fixed)
# ==========================================
elif st.session_state.active_window == 5:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>📅 SHEALTH AI 30-Day Precision Challenge Tracker</h3>", unsafe_allow_html=True)
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
    
    st.markdown("##### 📍 Phase 1: Select Active Tracking Coordinate Day")
    phase_tab = st.radio("Select Active 10-Day Phase Block:", ["Phase A (Days 1-10)", "Phase B (Days 11-20)", "Phase C (Days 21-30)"], horizontal=True)
    
    if "Phase A" in phase_tab:
        day_num = st.slider("Select Active Day Tracker Window:", 1, 10, 1)
        phase_offset = 0
    elif "Phase B" in phase_tab:
        day_num = st.slider("Select Active Day Tracker Window:", 11, 20, 11)
        phase_offset = 10
    else:
        day_num = st.slider("Select Active Day Tracker Window:", 21, 30, 21)
        phase_offset = 20

    hash_idx = day_num + phase_offset
    
    # 100% Unique Datapool matrices mapping different regions of India across all 30 variations
    indian_regions = [
        "Punjab Region", "Kerala Coastline", "Gujarat Plains", "Assam Hills", "Kashmir Valley", 
        "Rajasthan Desert", "West Bengal Delta", "Tamil Nadu Plains", "Goan Coast", "Hyderabad Matrix",
        "Maharashtra Coast", "Andhra Ghats", "Odisha Delta", "Bihar Plains", "Karnataka Plateau",
        "Himachal Ranges", "Nagaland Hills", "Meghalaya Plateaus", "Uttar Pradesh Plains", "Madhya Heartlands",
        "Mizoram Slopes", "Tripura Valleys", "Sikkim Peaks", "Jharkhand Woodlands", "Chhattisgarh Wilds",
        "Uttarakhand Valleys", "Haryana Plains", "Manipur Valleys", "Arunachal Heights", "Malabar Coast"
    ]
    
    veg_breakfast_pool = [
        "Paneer Oats Cheela", "Puttu with Steamed Kadala", "Methi Thepla with Curd", "Brown Rice Flakes Poha", "Kashmiri Noon Chai with Almond Girda",
        "Bajra Raab with Roasted Nuts", "Sattu Porridge with Jaggery", "Ragi Idli with Tomato Chutney", "Foxtail Millet Upma", "Moong Dal Sprouts Chat",
        "Thalipeeth with Low Fat Butter", "Pesarattu Mint Toast", "Chhena Poda Slice", "Sattu Stuffed Kachori", "Akki Roti with Dill Leaves",
        "Sidu with Lentil Mash", "Boiled Sweet Potatoes with Black Salt", "Steamed Jowar Flakes", "Whole Wheat Dalia", "Sprouted Chana Salad",
        "Bamboo Shoot Rice Cakes", "Sticky Rice Mash", "Millet Flour Dumplings", "Roasted Makhana Porridge", "Chana Dal Steamed Fara",
        "Finger Millet Gruel", "Besan Onion Cheela", "Singhara Flour Crepe", "Buckwheat Khichdi", "Malabar Neem Leaf Infusion Pancakes"
    ]

    nonveg_breakfast_pool = [
        "Egg White Scramble Spinach Wrap", "Malabar Egg Roast with Whole Wheat Appam", "Egg Poha Infused with Turmeric", "Assamese Egg Bor with Green Herbs", "Kashmiri Poached Eggs in Light Tomato Broth",
        "Mughlai Minced Chicken Toast", "Bengali Dim Bhurji with Mustard Hints", "Tamil Nadu Egg Podimas with Curry Leaves", "Goan Egg Cafe-real Wrap", "Hyderabadi Chicken Keema Patties",
        "Maharashtrian Anda Anda Poha", "Andhra Spicy Egg White Omelet", "Odisha Egg Masala Mash", "Bihari Egg Bhujia with Roasted Gram", "Mangalorean Egg Ghee Roast Whites",
        "Pahadi Herb Omelet", "Naga Style Smoked Chicken Shreds", "Khasi Egg Scramble", "UP Style Masala Omelet", "Bhopali Minced Egg Toast",
        "Mizo Egg Stew", "Tripuri Boiled Egg Salad", "Sikkim Chicken Momos (Steamed)", "Jharkhand Desi Chicken Shreds", "Chhattisgarhi Egg Fara",
        "Kumaoni Herb Fried Eggs", "Haryanvi Ghee Egg White Scramble", "Manipuri Fish Pepper Mash", "Arunachal Steamed Herbs Egg", "Malabar Boiled Egg Podi Wrap"
    ]

    v_region = indian_regions[(hash_idx - 1) % len(indian_regions)]
    v_b = veg_breakfast_pool[(hash_idx - 1) % len(veg_breakfast_pool)]
    nv_b = nonveg_breakfast_pool[(hash_idx - 1) % len(nonveg_breakfast_pool)]
    
    detox_drinks = ["Spearmint Infused Herbal Flush", "Jeera Coriander Warm Decoction", "Aloe Vera Ginger Anti-inflammatory Shot", "Sun-warmed Fennel Cleanse", "Salted Mint Buttermilk"]
    workouts_loss = ["Low-Cortisol Bodyweight Squats: 3 sets x 15 reps + 20 mins walk", "Wall Pushups: 3 sets x 12 reps + 15 mins steady stepping", "Incline Slow Treadmill Pace: 25 mins continuous steady track", "Tricep Chair Dips: 3 sets x 10 reps + 20 mins post-meal stroll"]
    workouts_gain = ["Floor Glute Bridges: 4 sets x 12 reps (Hold peak 2 seconds)", "Chair Assisted Squats: 3 sets x 10 reps (Very slow 3-sec drop descent)", "Plank Alignment Core Holds: 4 sets x 45 seconds holds", "Dumbbell Overhead Presses: 3 sets x 12 reps (Strength density pace)"]
    
    d_drink = detox_drinks[hash_idx % len(detox_drinks)]
    
    if "Loss" in st.session_state.target_goal:
        active_workout_plan = workouts_loss[hash_idx % len(workouts_loss)]
    else:
        active_workout_plan = workouts_gain[hash_idx % len(workouts_gain)]
        
    selected_yoga_block = yoga_asanas[hash_idx % len(yoga_asanas)]
    
    st.markdown(f"### 📋 Personal AI Curriculum Mapping Matrix: **Day {day_num} Logs**")
    st.info(f"🗺️ Active Regional Palate Focus: **{v_region} Special Core**")
    
    with st.expander(f"🥤 Step 1: Morning Detox Elixir - Day {day_num} (Click to Pull Up/Down)", expanded=True):
        st.markdown("<div class='detox-badge'>Active Fluid Infusion</div>", unsafe_allow_html=True)
        st.write(f"**Therapeutic Protocol:** Warmed {d_drink} administered empty-stomach to settle cellular targets.")
        
    with st.expander(f"🍱 Step 2: 4-Course Daily Culinary Layout - Day {day_num} (Click to Pull Up/Down)", expanded=True):
        st.markdown(f"""
        <div class='meal-box'><strong>🍳 Course 1: Breakfast Target ({v_region})</strong><br>Veg Choice: {v_b} prepared clean. <br>Non-Veg Choice: {nv_b} with high bio-available clean protein macros.</div>
        <div class='meal-box'><strong>🍛 Course 2: Mid-Day Lunch Alignment ({v_region})</strong><br>Veg Path: 1 Bowl Lentil Stew + 1 cup stir-fried seasonal vegetables + 1 Bran Roti. <br>Non-Veg Path: 150g Lemon Grilled Chicken Breast served alongside fresh green leafy salad.</div>
        <div class='meal-box'><strong>🥗 Course 3: Evening Adrenal Vitality Snack</strong><br>1 Cup Spiced Ayurvedic Kadha Tea paired with a small palmful of roasted crunchy Makhanas.</div>
        <div class='meal-box'><strong>🌙 Course 4: Restorative Night Repair Dinner</strong><br>Veg Path: Soft textured tofu vegetable hash cooked in minimal ghee. <br>Non-Veg Path: 120g Seared salmon fish paired with charred broccoli strings.</div>
        """, unsafe_allow_html=True)
        
    with st.expander(f"🛒 Step 3: Shopping Manifest Basket - Day {day_num} (Click to Pull Up/Down)", expanded=False):
        st.markdown(f"<div class='grocery-box'>✓ Required Active Ingredients Sourced from {v_region}: Oats, Whole Wheat, Lentils, Spices, Mint leaves, Green Herbs.</div>", unsafe_allow_html=True)
        
    with st.expander(f"🏋️‍♀️ Step 4: Customized Exercise Blueprint - Day {day_num} (Click to Pull Up/Down)", expanded=True):
        st.markdown(f"<div class='workout-box'><strong>Active Functional Training Routine:</strong><br>{active_workout_plan}</div>", unsafe_allow_html=True)
        
    with st.expander(f"🧘‍♂️ Step 5: Labeled Yoga Asana Form Manual - Day {day_num} (Click to Pull Up/Down)", expanded=False):
        ycol1, ycol2 = st.columns([1, 2])
        with ycol1:
            st.image(selected_yoga_block["img"], use_container_width=True, caption="Form Guidance Frame")
        with ycol2:
            st.markdown(f"##### **Asana Target: {selected_yoga_block['title']}**")
            st.write(selected_yoga_block["desc"])
            
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔒 Compliance Center"):
        jump_to_window(6)
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[5]}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 6: COMPLIANCE CORE & GENDER FILTERED TRACKER
# ==========================================
elif st.session_state.active_window == 6:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>🚨 Real-time Adherence Dashboards & Regional Provider Locator</h3>", unsafe_allow_html=True)
    
    w_baseline = float(st.session_state.p_weight * 0.035)
    
    hud1, hud2 = st.columns(2)
    with hud1:
        if st.session_state.p_gender == "Female Profile":
            today_date = datetime.date.today()
            days_since_last_reds = (today_date - st.session_state.p_reds_last).days
            days_until_next_reds = (28 - (days_since_last_reds % 28)) % 28
            
            st.markdown("<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>🔒 Private Dynamic 'Monthly Reds' Forecast</h4>", unsafe_allow_html=True)
            st.markdown(f"""
            <div style='background-color:#FFF5F5; padding:20px; border-radius:15px; border-left:5px solid #DC2626; margin-bottom:20px;'>
                <p style='margin:0; font-weight:700; color:#991B1B; font-size:1.1rem;'>🗓️ Estimated Next Secure Window Arrival</p>
                <p style='font-size:2rem; font-weight:800; color:#7F1D1D; margin:10px 0;'>{days_until_next_reds} Days Remaining</p>
                <p style='font-size:0.9rem; color:#451A1A; margin:0;'>
                    <strong>AI Tracker Advice:</strong> 
                    {"Prioritize cellular recovery and include roasted Makhana to balance micro-cravings safely as vectors shift." if days_until_next_reds <= 7 else "Energy parameters are stable. Optimal window to execute Alternate Squat progressions."}
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("---")
            
        st.markdown("<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>⏰ Precision AI Interactive Audio Alarms</h4>", unsafe_allow_html=True)
        st.caption(f"🕒 Alarm Core synced with Delhi IST: **{formatted_time}**")
        
        wat_alarm = st.checkbox("🔔 Water Tracker Notification (Recommended short bell sync)")
        med_alarm = st.checkbox("💊 Active Hormone Prescription Alarm (Fasting Schedule Sync)")
        
        if wat_alarm or med_alarm:
            trigger_alarm_sound()
        
        st.markdown("---")
        st.markdown("<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>🍎 Multi-Food Caloric Dictionary Index Lookups</h4>", unsafe_allow_html=True)
        f_select = st.selectbox("Search Indian Food Items Base Matrix:", ["1 Wheat Chapati", "100g Paneer Bhurji", "1 Bowl Moong Dal Khichdi", "1 Whole Boiled Egg", "100g Chicken Breast (Grilled)", "1 Roasted Papad", "1 Bowl Green Sabzi"])
        cal_index = {"1 Wheat Chapati": "85 kcal", "100g Paneer Bhurji": "190 kcal", "1 Bowl Moong Dal Khichdi": "220 kcal", "1 Whole Boiled Egg": "78 kcal", "100g Chicken Breast (Grilled)": "165 kcal", "1 Roasted Papad": "35 kcal", "1 Bowl Green Sabzi": "95 kcal"}
        st.code(f"Database Caloric Core Value: {cal_index[f_select]}")
        
        st.markdown("---")
        st.markdown("<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>🥛 Hydration Multiplier Tracker Progress</h4>", unsafe_allow_html=True)
        gl_drunk = st.slider("Glasses consumed today (250ml units):", 0, 16, 4)
        total_liters = gl_drunk * 0.25
        st.progress(min(total_liters / w_baseline, 1.0))
        st.write(f"Logged Status: **{total_liters:.2f} L** out of calculated target **{w_baseline:.1f} L**")
        
    with h2:
        st.markdown("<h4 style='font-family: \"Playfair Display\", serif; color: #7F1D1D;'>📍 Satellite Healthcare Provider Locator Grid</h4>", unsafe_allow_html=True)
        st.info(f"🛰️ Active Geolocation Lock Signal: Verified within **{st.session_state.p_loc}** Perimeter Networks")
        
        st.markdown("##### Closest Specialized Diagnostics & Emergency Nodes found:")
        st.markdown(f"""
        <div class='provider-box'>
            <strong>🏥 Apollo Diagnostic Healthcare Center & Endocrine Hub</strong><br>
            Location Ward Coordinates: Regional Peripheral Ward, {st.session_state.p_loc.split(',')[0]} • Specialized Clinical Testing Wing Active
        </div>
        <div class='provider-box'>
            <strong>💊 Apollo Pharmacy 24x7 Retail Counter Outlets</strong><br>
            Distance Matrix: 0.7 km away • Synced with state pharmacist prescription networks for specialized hormonal therapeutics
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color: #FCA5A5;'><br>", unsafe_allow_html=True)
    
    # --- EXECUTIVE FOUNDER AUTHENTICITY BLOCK ---
    st.markdown(f"""
    <div class='founder-card' style='background: linear-gradient(135deg, rgba(254, 242, 242, 0.9) 0%, rgba(254, 226, 226, 0.9) 100%) !important; padding: 30px; border-radius: 20px; border: 1px solid #FCA5A5;'>
        <h3 style='font-family: \"Playfair Display\", serif; color: #7F1D1D; margin-top:0;'>👩‍⚕️ Clinical Product System Architecture</h3>
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
    if st.button("↩️ Reset Session"):
        jump_to_window(1)
    st.markdown(f"<div class='trending-quote-banner'>{window_quotes[6]}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
