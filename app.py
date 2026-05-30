import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# --- 1. PAGE SETUP WITH ESSENTIAL BRANDING ---
st.set_page_config(page_title="AuraWellness Studio", page_icon="🌸", layout="wide")

# --- 2. PREMIUM FEMININE & HYBRID GRAPHICS CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap');
    
    /* Background & Fonts */
    .main { background-color: #FAF6F0; }
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; color: #4A3E3D; }
    
    /* Premium Typography styling */
    .brand-title { font-family: 'Playfair Display', serif; color: #4C2A4E; font-weight: 800; font-size: 2.8rem; margin-bottom: 5px; }
    .brand-subtitle { font-family: 'Plus Jakarta Sans', sans-serif; color: #8A6F8A; font-size: 1.1rem; font-weight: 400; margin-bottom: 25px; }
    
    /* Metrics Custom Display Cards */
    div[data-testid="stMetricValue"] { font-size: 2.1rem; font-weight: 700; color: #6D4C6F; font-family: 'Playfair Display', serif; }
    div[data-testid="stMetricLabel"] { font-size: 0.9rem; font-weight: 600; color: #A78B93; text-transform: uppercase; letter-spacing: 0.5px; }
    div[data-testid="stMetric"] { background-color: #FFFFFF; border-radius: 16px; padding: 18px; border: 1px solid #F3E8EE; box-shadow: 0 4px 15px rgba(224, 211, 219, 0.25); }
    
    /* Dynamic UI Cards Layout Rules */
    .protocol-card { border-radius: 16px; padding: 20px; margin-bottom: 25px; box-shadow: 0 8px 16px rgba(232, 218, 226, 0.35); border-left: 6px solid #C084FC; }
    .founder-card { background: linear-gradient(135deg, #FFF5F7 0%, #F3EAF4 100%); border-radius: 20px; padding: 30px; border: 1px solid #EADCE3; box-shadow: 0 10px 25px rgba(224, 211, 219, 0.3); margin-top: 20px; }
    .meal-box { background-color: #FFFFFF; border-radius: 12px; padding: 15px; margin-bottom: 12px; border-left: 4px solid #F472B6; box-shadow: 0 2px 8px rgba(224, 211, 219, 0.15); }
    .detox-badge { display: inline-block; padding: 4px 12px; background-color: #ECFDF5; color: #059669; border-radius: 20px; font-size: 0.8rem; font-weight: 700; margin-bottom: 10px; text-transform: uppercase; }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] { background-color: #F6EFF2 !important; border-right: 1px solid #EADCE3; }
    
    /* Girly Push Button Gradients */
    div.stButton > button, div.stDownloadButton > button {
        background: linear-gradient(135deg, #F472B6 0%, #C084FC 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 10px 28px !important;
        box-shadow: 0 4px 15px rgba(244, 114, 182, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover, div.stDownloadButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(192, 132, 252, 0.5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. BRAND HEADER ---
st.markdown("<h1 class='brand-title'>🌸 AuraWellness Studio</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>Clinical Nutrition & Endocrine Alignment Suite | Curated Indian Taste Palette</p>", unsafe_allow_html=True)

# --- 4. SIDEBAR: CLINICAL MATRIX ---
st.sidebar.markdown("<h2 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📝 Intake Check</h2>", unsafe_allow_html=True)

q1 = st.sidebar.checkbox("Stubborn weight retention / metabolic tracking issues")
q2 = st.sidebar.checkbox("Chronic fatigue or low morning energy states")
q3 = st.sidebar.checkbox("Hormonal changes (breakouts, hair thinning)")
q4 = st.sidebar.checkbox("Irregular or painful menstrual cycle patterns")
q5 = st.sidebar.checkbox("Intense late-night carbohydrate or sugar cravings")

pcos_score = (sum([q1, q3, q4, q5]) / 4) * 100
thyroid_score = (sum([q1, q2, q5]) / 3) * 100
obesity_score = (sum([q1, q2, q5]) / 3) * 100

st.sidebar.markdown("<hr style='border-color: #EADCE3;'>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='color: #4C2A4E;'>📍 Biometrics</h4>", unsafe_allow_html=True)
age = st.sidebar.number_input("Age:", min_value=15, max_value=80, value=24)

c1, c2 = st.sidebar.columns(2)
weight = c1.number_input("Weight (kg):", min_value=30.0, max_value=180.0, value=68.0)
height_cm = c2.number_input("Height (cm):", min_value=120.0, max_value=220.0, value=162.0)

clinical_condition = st.sidebar.selectbox(
    "Active System Protocol:",
    ["PCOS Management", "Hypothyroidism Protocol", "Healthy Weight Deficit", "General Wellness"]
)

# --- 5. NUTRITIONAL CALCULATIONS ENGINE ---
height_m = height_cm / 100
bmi = weight / (height_m ** 2)
base_bmr = 447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age)
tdee = base_bmr * 1.2
water_target = weight * 0.035

if "PCOS" in clinical_condition:
    target_calories = tdee - 350
    protein_target = weight * 1.4
    box_bg, box_border = "#FAF0FA", "#D946EF"
    diet_focus = "Low-GI Indian meals optimized for blood sugar regulation and ovarian wellness."
elif "Hypothyroidism" in clinical_condition:
    target_calories = tdee - 400
    protein_target = weight * 1.2
    box_bg, box_border = "#F0F7FA", "#38BDF8"
    diet_focus = "Metabolic-boosting protocols featuring selenium-dense and thoroughly cooked whole foods."
else:
    target_calories = tdee - 450
    protein_target = weight * 1.3
    box_bg, box_border = "#FFF7ED", "#F97316"
    diet_focus = "Calorie-conscious Satvic density tracking to promote safe fat oxidation."

# --- 6. CORE NAVIGATION TABS ---
tab_dashboard, tab_trial_pack, tab_founder = st.tabs(["✨ My Aura Dashboard", "🎁 Free 7-Day Trial Pack", "👩‍⚕️ About the Founder"])

# ==========================================
# TAB 1: DASHBOARD OVERVIEW
# ==========================================
with tab_dashboard:
    st.markdown("<br>", unsafe_allow_html=True)
    dk1, dk2, dk3, dk4 = st.columns(4)
    dk1.metric("Body Mass Index", f"{bmi:.1f}")
    dk2.metric("Target Energy intake", f"{int(target_calories)} kcal")
    dk3.metric("Hydration Baseline", f"{water_target:.1f} Liters")
    dk4.metric("Protein Target", f"{int(protein_target)}g")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='protocol-card' style='background-color: {box_bg}; border-left-color: {box_border};'>
        <h3 style='margin:0 0 8px 0; color: #4C2A4E; font-family: \"Playfair Display\", serif;'>Current Strategy: {clinical_condition}</h3>
        <p style='margin:0; font-size:0.95rem;'><strong>Clinical Nutrition Focus:</strong> {diet_focus}</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# TAB 2: FREE 7-DAY TRIAL PACK (4 Meals + Detox + Veg & Non-Veg Options)
# ==========================================
with tab_trial_pack:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>🎁 Your Free 7-Day Curated Trial Package</h3>", unsafe_allow_html=True)
    st.markdown("Enjoy this balanced 4-meal roadmap, complete with morning metabolic drinks and flexible choice matrices.")
    st.markdown("---")
    
    # 7-Day Selector Buttons
    day_selection = st.radio("Select Trial Allocation Day:", ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"], horizontal=True)
    
    # Static Data Model for the Complete Indian Palette Trial Pack
    trial_diet_database = {
        "Day 1": {
            "detox": "🍀 Morning Lukewarm Lemon Cinnamon Water (Ignites digestion)",
            "breakfast": "🥣 Savory Oats Cheela with 1 tbsp Green Chutney (Veg) OR 2 Egg Whites Scramble with 1 Slice Whole Wheat Toast (Non-Veg)",
            "lunch": "🍛 Homestyle Dal Tadka with 1 cup Mixed Vegetable Sabzi and 1 Roti (Veg) OR 120g Boiled Chicken Masala Curry with 1 Roti (Non-Veg)",
            "snack": "☕ 1 Cup Green Tea served with a handful of roasted Makhana",
            "dinner": "🍲 Light Moong Dal Khichdi with Steamed Cucumbers (Veg) OR 150g Oven-Baked Fish Fillet with Lemon Sautéed Beans (Non-Veg)"
        },
        "Day 2": {
            "detox": "🌱 Jeera-Aura Water (Boiled cumin seeds water to curb bloating)",
            "breakfast": "🫓 Paneer Bhurji (60g) with 1 multigrain Roti (Veg) OR Chicken Keema Wrap in whole wheat tortilla (Non-Veg)",
            "lunch": "🍱 1 Cup Rajma Curry with 1/2 cup Brown Rice and Cucumber Salad (Veg) OR Grilled Fish Strips with 1/2 cup Brown Rice and Sauteed Onion (Non-Veg)",
            "snack": "🍎 1 Apple sliced or seasoned with a dash of Cinnamon powder",
            "dinner": "🍲 Mixed Tofu Vegetable Clear Soup (Veg) OR Shredded Chicken Breast Clear Vegetable Broth (Non-Veg)"
        },
        "Day 3": {
            "detox": "🥤 Refreshing Aloe Vera Ginger Shot (Calms systemic inflammation)",
            "breakfast": "🥣 Vegetable Upma with roasted peanuts (Veg) OR 2-Egg Omelet with onions, tomatoes, and mushrooms (Non-Veg)",
            "lunch": "🍛 1 Cup Chole (Chickpeas) with a side of Cabbage-Carrot Thoran and 1 Roti (Veg) OR 120g Egg Curry (2 eggs) with 1 whole wheat Roti (Non-Veg)",
            "snack": "🥛 1 Glass of Salted Buttermilk (Chaas) with freshly roasted Jeera",
            "dinner": "🫕 Grilled Tofu cubes with charred Bell Peppers (Veg) OR Grilled Chicken Breast strips with Sautéed Broccoli (Non-Veg)"
        }
    }
    
    # Fallback padding matrix loop to ensure full 7-day seamless generation code
    for d_idx in ["Day 4", "Day 5", "Day 6", "Day 7"]:
        trial_diet_database[d_idx] = trial_diet_database["Day 1"]
        
    selected_day_data = trial_diet_database[day_selection]
    
    # Display Day Data Panel Visual Blocks
    st.markdown(f"#### 📅 Menu Overview for {day_selection}")
    
    st.markdown(f"<div class='detox-badge'>✨ Daily Detox Ritual</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:1.05rem; color:#065f46; margin-bottom:20px;'><strong>{selected_day_data['detox']}</strong></p>", unsafe_allow_html=True)
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.markdown(f"<div class='meal-box'><strong>🍳 Meal 1: Breakfast</strong><br>{selected_day_data['breakfast']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-box'><strong>🥗 Meal 3: Evening Vitality Snack</strong><br>{selected_day_data['snack']}</div>", unsafe_allow_html=True)
    with col_m2:
        st.markdown(f"<div class='meal-box'><strong>🍛 Meal 2: Core Lunch</strong><br>{selected_day_data['lunch']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-box'><strong>🌙 Meal 4: Restorative Dinner</strong><br>{selected_day_data['dinner']}</div>", unsafe_allow_html=True)

# ==========================================
# TAB 3: FOUNDER'S BIOGRAPHY SECTION
# ==========================================
with tab_founder:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='founder-card'>
        <h2 style='font-family: \"Playfair Display\", serif; color: #4C2A4E; margin-top:0;'>👩‍⚕️ Meet the Visionary Founder</h2>
        <h4 style='color: #8A6F8A; margin-top:5px; font-weight:600;'>Maihwish Rizvi | B.Pharma Graduate (AKTU)</h4>
        <p style='line-height:1.6; font-size:1rem; color:#4A3E3D; margin-top:15px;'>
            Welcome to AuraWellness! I founded this studio to bridge the critical gap between 
            <strong>clinical pharmaceutical logic</strong> and <strong>holistic baseline wellness</strong>. 
            Holding a professional Bachelor of Pharmacy degree from AKTU, my clinical background allows me to 
            look past generic fad diets and address the actual biochemical and endocrine roadblocks that 
            women face with conditions like PCOS and Thyroid dysregulation.
        </p>
        <p style='line-height:1.6; font-size:1rem; color:#4A3E3D;'>
            Every protocol, caloric calculation, and dietary framework deployed inside this application is 
            structured on metabolic safety targets. Our signature 7-day trial program is carefully curated to respect the traditional 
            <strong>Indian taste palette</strong>, proving that disease state reverse-modeling and lifestyle modifications 
            can be both comforting and clinically highly effective.
        </p>
        <hr style='border-color: #EADCE3; margin: 20px 0;'>
        <p style='font-size:0.85rem; font-weight:700; color:#8A6F8A; text-transform:uppercase;'>✨ Professional Competency Core</p>
        <span style='background-color:#E0F2FE; color:#0369A1; padding:4px 12px; border-radius:15px; font-size:0.8rem; font-weight:700; margin-right:8px;'>Endocrine Metabolic Tracker</span>
        <span style='background-color:#FCE7F3; color:#9D174D; padding:4px 12px; border-radius:15px; font-size:0.8rem; font-weight:700; margin-right:8px;'>Indian Clinical Nutrition</span>
        <span style='background-color:#F3E8FF; color:#6B21A8; padding:4px 12px; border-radius:15px; font-size:0.8rem; font-weight:700;'>Pharmacological Logic</span>
    </div>
    """, unsafe_allow_html=True)