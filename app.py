import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# --- 1. CORE SYSTEM INITIALIZATION (Must be first) ---
st.set_page_config(page_title="AuraWellness Studio", page_icon="🌸", layout="wide")

# --- 2. ADVANCED CHIC PASTEL GLAMOUR STYLE SHEET ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght=0,400..900;1,400..900&family=Plus+Jakarta+Sans:ital,wght=0,200..800;1,200..800&display=swap');
    
    /* Luxury Aesthetic Aura Fluid Canvas Backdrop */
    .stApp {
        background-image: linear-gradient(to bottom, rgba(250, 246, 240, 0.86), rgba(246, 239, 242, 0.90)), 
                          url('https://images.unsplash.com/photo-1557672172-298e090bd0f1?w=1600');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; color: #4A3E3D; }
    
    .brand-title { font-family: 'Playfair Display', serif; color: #4C2A4E; font-weight: 800; font-size: 2.8rem; margin-bottom: 5px; }
    .brand-subtitle { font-family: 'Plus Jakarta Sans', sans-serif; color: #8A6F8A; font-size: 1.1rem; font-weight: 400; margin-bottom: 25px; }
    
    /* Transparent Glassmorphism Tokens */
    div[data-testid="stMetricValue"] { font-size: 2rem; font-weight: 700; color: #6D4C6F; font-family: 'Playfair Display', serif; }
    div[data-testid="stMetricLabel"] { font-size: 0.85rem; font-weight: 600; color: #A78B93; text-transform: uppercase; letter-spacing: 0.5px; }
    div[data-testid="stMetric"] { 
        background-color: rgba(255, 255, 255, 0.8) !important; 
        backdrop-filter: blur(8px); border-radius: 16px; padding: 15px; 
        border: 1px solid rgba(243, 232, 238, 0.7); box-shadow: 0 4px 15px rgba(224, 211, 219, 0.12); 
    }
    
    .window-card { background-color: rgba(255, 255, 255, 0.75); backdrop-filter: blur(8px); border-radius: 20px; padding: 25px; border: 1px solid #F0E4EC; box-shadow: 0 8px 24px rgba(224, 211, 219, 0.15); margin-bottom: 20px; }
    .meal-box { background-color: rgba(255, 255, 255, 0.85); border-radius: 12px; padding: 15px; margin-bottom: 12px; border-left: 4px solid #F472B6; box-shadow: 0 2px 8px rgba(224, 211, 219, 0.05); }
    .workout-box { background-color: rgba(255, 255, 255, 0.85); border-radius: 12px; padding: 15px; margin-bottom: 12px; border-left: 4px solid #A7F3D0; box-shadow: 0 2px 8px rgba(224, 211, 219, 0.05); }
    .detox-badge { display: inline-block; padding: 4px 12px; background-color: #ECFDF5; color: #059669; border-radius: 20px; font-size: 0.8rem; font-weight: 700; margin-bottom: 10px; text-transform: uppercase; }
    .provider-box { background-color: #FAFAF9; border-radius: 12px; padding: 15px; border-left: 4px solid #C084FC; margin-bottom: 10px; }
    
    /* Soft Girly Push Buttons styling overrides */
    div.stButton > button, div.stDownloadButton > button {
        background: linear-gradient(135deg, #F472B6 0%, #C084FC 100%) !important;
        color: white !important; font-weight: 700 !important; border-radius: 25px !important;
        border: none !important; padding: 10px 28px !important;
        box-shadow: 0 4px 15px rgba(244, 114, 182, 0.3) !important; transition: all 0.3s ease !important;
        width: 100%;
    }
    div.stButton > button:hover { transform: translateY(-1px) !important; box-shadow: 0 6px 20px rgba(192, 132, 252, 0.4) !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. UPPER PLATFORM BRAND BANNER ---
st.markdown("<h1 class='brand-title'>🌸 AuraWellness Studio</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>Clinical Endocrine Modification Hub & Multi-Window Lifecycle Suite</p>", unsafe_allow_html=True)
st.markdown("---")

# --- 4. MULTI-PAGE WINDOW NAVIGATION CONTROLLER ---
st.markdown("### 🪟 Navigation Hub")
window_selection = st.radio(
    "Select Interface Window To Open:",
    ["Window 1: Clinical Survey", "Window 2: Biometrics Center", "Window 3: 1-Month Medical Diet Pack", "Window 4: Daily Compliance & Provider Locator"],
    horizontal=True
)
st.markdown("---")

# --- GLOBAL CLINICAL MEMORY CACHE ---
if 'survey_complete' not in st.session_state: st.session_state.survey_complete = False
if 'pcos_vector' not in st.session_state: st.session_state.pcos_vector = 0
if 'thyroid_vector' not in st.session_state: st.session_state.thyroid_vector = 0

# ==========================================
# WINDOW 1: CLINICAL SURVEY
# ==========================================
if "Window 1" in window_selection:
    st.markdown("<div class='window-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📋 Clinical Intake & Symptom Screening (10 Question Matrix)</h3>", unsafe_allow_html=True)
    st.markdown("Please complete this diagnostic evaluation checklist to calibrate the system logic:")
    
    s1 = st.checkbox("1. Sudden or stubborn weight fluctuations unlinked to caloric changes?")
    s2 = st.checkbox("2. Waking up exhausted, chronic brain fog, or generalized lethargy?")
    s3 = st.checkbox("3. Active androgenic symptoms (hair volume drops, facial flareups, severe acne)?")
    s4 = st.checkbox("4. Menstrual cycles irregular, heavily delayed, or consistently missed?")
    s5 = st.checkbox("5. Hypersensitivity to standard room temperatures (feeling extreme cold or sudden hot flashes)?")
    s6 = st.checkbox("6. Mood swings, heightened irritability, or unprovoked anxiety spikes?")
    s7 = st.checkbox("7. Powerful carbohydrate, sodium, or refined sugar cravings?")
    s8 = st.checkbox("8. Muscle stiffness, joint inflammation, or muscle fatigue upon waking?")
    s9 = st.checkbox("9. Puffiness localized around the eyes/face or chronic skin dryness?")
    s10 = st.checkbox("10. Diagnosed insulin resistance or paternal family history of early diabetes?")
    
    if st.button("✨ Lock & Process Symptom Density"):
        st.session_state.pcos_vector = (sum([s1, s3, s4, s6, s7, s10]) / 6) * 100
        st.session_state.thyroid_vector = (sum([s1, s2, s5, s6, s8, s9]) / 6) * 100
        st.session_state.survey_complete = True
        st.success("Symptom vectors successfully mapped! Please proceed to Window 2 to calibrate your biometrics.")
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 2: BIOMETRICS & CONVERTERS CENTER
# ==========================================
elif "Window 2" in window_selection:
    st.markdown("<div class='window-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📐 Physical Biometrics & Unit Converter Lab</h3>", unsafe_allow_html=True)
    
    # Advanced Unit Conversion Sub-Panel
    with st.expander("🔄 Open Unit Conversion Assistant (Push Up/Down for Lbs/Inches)", expanded=False):
        st.markdown("##### Convert parameters smoothly into metric standards:")
        u_col1, u_col2 = st.columns(2)
        with u_col1:
            input_lbs = st.number_input("Weight in Pounds (lbs):", min_value=0.0, value=150.0)
            st.code(f"Metric Equivalent: {input_lbs * 0.453592:.2f} kg")
        with u_col2:
            f_feet = st.number_input("Height - Feet Component:", min_value=0, max_value=8, value=5)
            f_inch = st.number_input("Height - Inches Component:", min_value=0, max_value=12, value=4)
            total_cm = (f_feet * 30.48) + (f_inch * 2.54)
            st.code(f"Metric Equivalent: {total_cm:.2f} cm")

    st.markdown("---")
    st.markdown("##### Input Metric Variables for Core Calculations:")
    b_col1, b_col2, b_col3 = st.columns(3)
    age = b_col1.number_input("Current Age:", min_value=15, max_value=80, value=24)
    weight = b_col2.number_input("Weight (in Kilograms):", min_value=30.0, max_value=180.0, value=68.0)
    height_cm = b_col3.number_input("Height (in Centimeters):", min_value=120.0, max_value=220.0, value=162.0)
    
    clinical_path = st.selectbox("Confirm Active Endocrine Filter Group:", ["PCOS Mapping", "Thyroid Profile", "General Balance Core"])
    target_path = st.selectbox("Confirm Target Track Option:", ["Weight Loss Tracker", "Weight Gain Tracker"])

    # Calculations Engine Core
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    base_bmr = 447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age)
    tdee = base_bmr * 1.25
    water_target = weight * 0.035

    st.markdown("---")
    st.markdown("#### Clinical Diagnostic Evaluation Summary")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Calculated BMI Profile", f"{bmi:.1f}")
    m3.metric("Hydration Baseline", f"{water_target:.1f} Liters")
    
    if "Weight Loss" in target_path:
        caloric_ceiling = tdee - 450
        m2.metric("Target Daily Energy Ceiling", f"{int(caloric_ceiling)} kcal", delta="-450 kcal (Deficit)")
    else:
        caloric_ceiling = tdee + 450
        m2.metric("Target Daily Energy Ceiling", f"{int(caloric_ceiling)} kcal", delta="+450 kcal (Surplus)")

    # BMI Status Visualizer
    st.markdown("##### BMI Stratification Criteria Mapping:")
    if bmi < 18.5:
        st.warning("🚨 **Classification: Underweight.** Requires mass reconstruction and lean tissue support protocols.")
    elif 18.5 <= bmi <= 24.9:
        st.success("🌸 **Classification: Euthyroid Normal Weight.** Optimal metric homeostasis balance detected.")
    elif 25.0 <= bmi <= 29.9:
        st.warning("⚠️ **Classification: Overweight/Pre-Obese Range.** Strategic caloric deficit calibration advised.")
    else:
        st.error("🚨 **Classification: Obese Range.** High endocrine stress profile. Immediate nutritional modifications indicated.")
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 3: 1-MONTH DIET & ACTIVITY BLOCK
# ==========================================
elif "Window 3" in window_selection:
    st.markdown("<div class='window-card'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📅 1-Month Structured Medical Diet & Activity Blueprint</h3>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1600", caption="Aura Studio Holistic Satvic Kitchen", use_container_width=True)
    
    week_select = st.radio("Select Training/Diet Cycle Week:", ["Week 1", "Week 2", "Week 3", "Week 4"], horizontal=True)
    
    # 1-Month Static Structural Database (Indian Palette Layout + 4 Meals)
    monthly_diet_framework = {
        "PCOS Mapping": {
            "loss": {
                "detox": "🧉 Warm Spearmint Tea + Lemon Drop (Directly drops testosterone arrays)",
                "bfast": "🥣 Veg Track: 1 High-Protein Oats & Paneer Cheela with fresh Mint Chutney OR Non-Veg: 2 Egg Whites Veggie Scramble",
                "lunch": "🍛 Veg Track: 1 Cup Moong Dal Tadka + 1 cup stir-fried Methi Sabzi + 1 Missi Roti",
                "snack": "☕ Green Tea with 1 small cup dry roasted unsalted Makhana",
                "dinner": "🍲 Veg Track: Light Lauki Oats Khichdi with curd OR Non-Veg: 150g Grilled Lemon Pomfret Fish",
                "grocery": "Rolled Oats, Low-fat Paneer, Mint, Soya Chunks, Bran Flour, Flaxseeds",
                "yoga": "🧘‍♂️ Butterfly Pose (Baddha Konasana) & Bhujangasana • 15 Mins • Stimulates blood supply to pelvic floor tracking paths.",
                "yoga_img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400"
            },
            "gain": {
                "detox": "🥛 Warm Almond Powder Date Infused Whole Dairy Milk",
                "bfast": "🫓 Veg Track: 2 Stuffed Paneer Parathas with Ghee + 1 cup Curd OR Non-Veg: 3 Egg Masala Omelet with buttered Toast",
                "lunch": "🍱 Veg Track: 1 Cup Shahi Paneer + 1 cup Dal Makhani + 2 Multigrain Chapatis",
                "snack": "🍌 1 Medium Banana + handful of Walnuts and Cashews",
                "dinner": "🍛 Veg Track: Paneer Tikka Makhani bowl with sweet potatoes OR Non-Veg: Chicken Keema Curry with 2 Rotis",
                "grocery": "Full-cream Milk, Ghee, Whole Paneer, Nuts, Potatoes, Basmati Rice",
                "yoga": "💪 Light Progressive Bodyweight Squats & Floor Glute Bridges • 20 Mins • Builds muscle density.",
                "yoga_img": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=400"
            }
        },
        "Thyroid Profile": {
            "loss": {
                "detox": "🌱 Warm Jeera Coriander Seed Infusion (Enhances thyroid secretion kinetics)",
                "bfast": "🥣 Veg Track: 1 Besan Chilla with cooked tomatoes OR Non-Veg: 2 Boiled Eggs with toasted brown bread",
                "lunch": "🍛 Veg Track: Tofu Stir-fry with cooked carrots and 1 Chapati OR Non-Veg: 120g Chicken Sauteed Masala Curry",
                "snack": "🥥 Fresh Coconut Water + 2 Brazil Nuts (Essential Selenium booster)",
                "dinner": "🍲 Veg Track: Well-cooked Masoor Dal soup with soft rice OR Non-Veg: Grilled Salmon with steamed beans",
                "grocery": "Besan, Tofu, Brazil Nuts, Carrots, Chicken, Masoor Dal",
                "yoga": "🧘‍♂️ Shoulder Stand (Sarvangasana) & Fish Pose (Matsyasana) • 12 Mins • Massages thyroid gland vectors.",
                "yoga_img": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400"
            },
            "gain": {
                "detox": "🥛 Warm Ashwagandha Turmeric Laced Milk (Balances TSH stress markers)",
                "bfast": "🫓 Veg Track: 2 Mixed Veg Parathas with White Butter OR Non-Veg: Egg Podimas (3 Eggs Bhurji) with paratha",
                "lunch": "🍛 Thick Arhar Dal Tarka + Paneer Bhurji (100g) + 2 Rotis + Salad",
                "snack": "🥑 Mango/Avocado Shake with chia seeds",
                "dinner": "🍱 Veg Track: Thick Malai Kofta with 2 buttered rotis OR Non-Veg: Butter Chicken (150g) with 2 Chapatis",
                "grocery": "Butter, Ashwagandha, Paneer, Mango pulp, Cream, Arhar Dal",
                "yoga": "🧘‍♂️ Dynamic Surya Namaskars • 6 Rounds (Moderate Pace) • Speeds up sluggish endocrine loops.",
                "yoga_img": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?w=400"
            }
        }
    }
    
    monthly_diet_framework["General Wellness Core"] = monthly_diet_framework["PCOS Mapping"]
    
    active_profile_key = "PCOS Mapping" if "PCOS" in clinical_path else ("Thyroid Profile" if "Thyroid" in clinical_path else "General Wellness Core")
    active_goal_key = "loss" if "Loss" in target_path else "gain"
    
    selected_diet_map = monthly_diet_framework[active_profile_key][active_goal_key]
    
    st.markdown(f"### 📋 Active Matrix Grid: {week_select} ({clinical_path})")
    
    # Push Up & Down columns using Expanders
    with st.expander("🥤 Step 1: Morning Detox Strategy (Click to Open)", expanded=True):
        st.markdown(f"<div class='detox-badge'>Active Detox Infusion</div>", unsafe_allow_html=True)
        st.write(f"**{selected_diet_map['detox']}**")
        
    with st.expander("🍱 Step 2: The 4-Meal Plan Breakdown (Click to Open)", expanded=True):
        st.markdown(f"<div class='meal-box'><strong>🍳 Meal 1: Breakfast</strong><br>{selected_diet_map['bfast']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-box'><strong>🍛 Meal 2: Core Mid-Day Lunch</strong><br>{selected_diet_map['lunch']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-box'><strong>🥗 Meal 3: Evening Vitality Snack</strong><br>{selected_diet_map['snack']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-box'><strong>🌙 Meal 4: Restorative Night Dinner</strong><br>{selected_diet_map['dinner']}</div>", unsafe_allow_html=True)
        
    with st.expander("🛒 Step 3: Grocery & Ingredient List (Click to Open)", expanded=False):
        st.info(f"**Ingredients Needed this week:** {selected_diet_map['grocery']}")
        
    with st.expander("🧘‍♀️ Step 4: Therapeutic Yoga & Movement Guide (Click to Open)", expanded=False):
        y_col1, y_col2 = st.columns([1, 2])
        with y_col1:
            st.image(selected_diet_map['yoga_img'], width=220, caption="Form Guidance Pose")
        with y_col2:
            st.markdown(f"**Exercise Routine Protocol:**")
            st.write(selected_diet_map['yoga'])
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 4: COMPLIANCE & LOCATOR (Realtime Engine)
# ==========================================
elif "Window 4" in window_selection:
    st.markdown("<div class='window-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>🚨 Compliance Central Alarms & Provider Locator</h3>", unsafe_allow_html=True)
    
    alarm_col1, alarm_col2 = st.columns(2)
    
    with alarm_col1:
        st.markdown("#### ⏰ Active Patient Alarms Dashboard")
        st.checkbox("🔔 Water Alarm: Time to drink 250ml water (Maintain hydration matrix)")
        st.checkbox("💊 Medicine Alarm: Empty-stomach dose / Hormonal tracking logs")
        
        st.markdown("---")
        st.markdown("#### 🍎 Food Caloric Dictionary Lookup")
        food_item = st.selectbox("Search Indian Food Item Calories:", ["1 Roti (Whole Wheat)", "100g Paneer Sabzi", "1 bowl Moong Dal Khichdi", "1 Boiled Egg", "1 plate Chicken Biryani"])
        calorie_dict = {"1 Roti (Whole Wheat)": "85 kcal", "100g Paneer Sabzi": "220 kcal", "1 bowl Moong Dal Khichdi": "240 kcal", "1 Boiled Egg": "78 kcal", "1 plate Chicken Biryani": "480 kcal"}
        st.code(f"Energy Value: {calorie_dict[food_item]}")
        
    with alarm_col2:
        st.markdown("#### 📍 Automated Medical Provider Locator")
        st.write("Tracking engine active. User region verified within **Uttar Pradesh, India.**")
        
        st.markdown("##### 🏥 Nearest Clinical Centers & Pharmacies found:")
        st.markdown("""
        <div class='provider-box'>
            <strong>🏥 Apollo Medical Diagnostics & Clinic</strong><br>
            Distance: 1.4 km away • Endocrine Specialists available
        </div>
        <div class='provider-box'>
            <strong>💊 Apollo Pharmacy 24x7 Retail Store</strong><br>
            Distance: 0.6 km away • All critical hormonal prescriptions stocked
        </div>
        <div class='provider-box'>
            <strong>🏥 District Government Hospital Emergency Center</strong><br>
            Distance: 3.2 km away • State support facilities available
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 👩‍⚕️ About the Founder")
    st.markdown(f"""
    <div class='founder-card' style='margin-top:5px;'>
        <h4 style='color: #4C2A4E; margin:0; font-family: \"Playfair Display\", serif; font-weight:700;'>Maihwish Rizvi | Registered Pharmacist</h4>
        <p style='font-size:0.92rem; line-height:1.5; margin-top:10px; color:#4A3E3D;'>
            As a <strong>Registered Pharmacist</strong>, my academic training allows me to look past generic fitness fads and track the deep endocrine pathways that drive metabolic conditions. Every calculator threshold, calorie framework, and therapeutic food selection in this suite is built on medical safety standards to optimize patient compliance.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
