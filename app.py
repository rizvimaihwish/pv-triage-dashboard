import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# --- 1. SYSTEM STANDARDS CONFIGURATION (Must be first) ---
st.set_page_config(page_title="AuraWellness Studio", page_icon="🌸", layout="wide")

# --- 2. ADVANCED CHIC PASTEL GLAMOUR STYLE SHEET ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght=0,400..900;1,400..900&family=Plus+Jakarta+Sans:ital,wght=0,200..800;1,200..800&display=swap');
    
    /* Luxury Aesthetic Aura Fluid Canvas Background Wallpaper */
    .stApp {
        background-image: linear-gradient(to bottom, rgba(250, 246, 240, 0.88), rgba(246, 239, 242, 0.92)), 
                          url('https://images.unsplash.com/photo-1557672172-298e090bd0f1?w=1600');
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; color: #4A3E3D; }
    
    /* Calligraphed Luxury Heading Styles */
    .brand-title { font-family: 'Playfair Display', serif; color: #4C2A4E; font-weight: 900; font-size: 3.5rem; text-align: center; letter-spacing: -0.5px; margin-bottom: 5px; }
    .brand-subtitle { font-family: 'Plus Jakarta Sans', sans-serif; color: #8A6F8A; font-size: 1.2rem; font-weight: 400; text-align: center; margin-bottom: 35px; }
    
    /* Elegant Content Glassmorphic Cards */
    .window-container { background-color: rgba(255, 255, 255, 0.82); backdrop-filter: blur(12px); border-radius: 24px; padding: 35px; border: 1px solid rgba(240, 228, 236, 0.8); box-shadow: 0 15px 35px rgba(224, 211, 219, 0.2); margin-bottom: 30px; }
    .meal-box { background-color: rgba(255, 255, 255, 0.9); border-radius: 14px; padding: 18px; margin-bottom: 15px; border-left: 5px solid #F472B6; box-shadow: 0 4px 12px rgba(224, 211, 219, 0.05); }
    .workout-box { background-color: rgba(255, 255, 255, 0.9); border-radius: 14px; padding: 18px; margin-bottom: 15px; border-left: 5px solid #A7F3D0; box-shadow: 0 4px 12px rgba(224, 211, 219, 0.05); }
    .detox-badge { display: inline-block; padding: 5px 14px; background-color: #ECFDF5; color: #059669; border-radius: 20px; font-size: 0.8rem; font-weight: 700; margin-bottom: 12px; text-transform: uppercase; }
    .provider-box { background-color: #FAFAF9; border-radius: 12px; padding: 18px; border-left: 4px solid #C084FC; margin-bottom: 12px; }
    .grocery-box { background-color: rgba(244, 251, 247, 0.85); padding: 15px; border-radius: 12px; border: 1px dashed #A7F3D0; margin-top: 15px; }
    
    /* Soft Girly Shimmer Gradient Push Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #F472B6 0%, #C084FC 100%) !important;
        color: white !important; font-weight: 700 !important; border-radius: 30px !important;
        border: none !important; padding: 12px 35px !important; font-size: 1rem !important;
        box-shadow: 0 6px 20px rgba(244, 114, 182, 0.3) !important; transition: all 0.3s ease !important;
        display: block; margin: 0 auto; width: 50%;
    }
    div.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 8px 25px rgba(192, 132, 252, 0.45) !important; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #F472B6, #C084FC) !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. PLATFORM CORE STATE ENGINE ---
if 'active_window' not in st.session_state: st.session_state.active_window = 1
if 'user_data' not in st.session_state: st.session_state.user_data = {}
if 'survey_score' not in st.session_state: st.session_state.survey_score = "General Wellness Core"
if 'target_goal' not in st.session_state: st.session_state.target_goal = "Weight Loss Tracker"

def jump_to_window(window_id):
    st.session_state.active_window = window_id
    st.rerun()

# ==========================================
# WINDOW 1: PORTAL INTRODUCTION
# ==========================================
if st.session_state.active_window == 1:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200", use_container_width=True)
    
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E; text-align:center;'>Welcome to a New Horizon of Feminine Metabolic Health</h3>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; font-size:1.05rem; line-height:1.7; max-width:850px; margin: 0 auto; color:#6B5E5E;'>
    AuraWellness Studio is a premium space designed exclusively for women mapping hormonal alignment. 
    We believe that addressing chronic disruptions like PCOS and Thyroid parameters shouldn't require aggressive 
    or mechanical protocols. Our platform reverse-models biological data to construct satvic, highly intuitive, 
    and comforting lifestyle regimes customized for the Indian palate.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><hr style='border-color: #F0E4EC;'><br>", unsafe_allow_html=True)
    st.markdown("#### 🎥 Daily Clinical Wellness Log")
    v1, v2 = st.columns([1.6, 1])
    with v1:
        st.video("https://www.youtube.com/watch?v=ScZs7L0_S38")
    with v2:
        st.markdown("<h5 style='color: #4C2A4E; font-family: \"Playfair Display\", serif;'>Managing Endocrine Cortisol Trajectories</h5>", unsafe_allow_html=True)
        st.write("Explore how sudden spikes in training intensities shift glucose baseline tolerances. Learn to apply localized, low-cortisol somatic loops to maximize metabolic adherence markers securely.")
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("✨ Begin Patient Onboarding Registration"):
            jump_to_window(2)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 2: PATIENT REGISTRATION & CLINICAL HISTORY
# ==========================================
elif st.session_state.active_window == 2:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>🔒 Patient Registration & Medical History Intake</h3>", unsafe_allow_html=True)
    
    r1, r2 = st.columns(2)
    with r1:
        name = st.text_input("Patient Full Name:", value="Riya Sharma")
        phone = st.text_input("Active Mobile Verification Line:", value="+91 98765 43210")
        location = st.text_input("Geographic Registration Location (City/State):", value="Lucknow, Uttar Pradesh")
    with r2:
        age = st.number_input("Biological Age Axis:", min_value=12, max_value=85, value=24)
        gender = st.radio("Gender Demographic Archetype:", ["Female Demographic Profile", "Male Demographic Profile"])
        weight = st.number_input("Registered Weight Metric (kg):", min_value=30.0, max_value=190.0, value=68.0)
        height_cm = st.number_input("Registered Height Metric (cm):", min_value=110.0, max_value=230.0, value=162.0)
        
    st.markdown("---")
    st.markdown("#### 📋 Prior Medical History & Pharmacological Background")
    med_history = st.text_area("Please list any historical medical diagnoses or active clinical prescriptions (e.g., Metformin 500mg, Thyronorm 25mcg, None):", value="None")
    
    if st.button("🚀 Confirm Profile & Initialize Survey"):
        st.session_state.user_data = {
            "name": name, "phone": phone, "location": location, "age": age,
            "weight": weight, "height": height_cm, "history": med_history
        }
        jump_to_window(3)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 3: AUTOMATED 10-QUESTION SCREENING SURVEY
# ==========================================
elif st.session_state.active_window == 3:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📋 Mandatory Intake Survey & Symptom Density Matrix</h3>", unsafe_allow_html=True)
    
    s1 = st.checkbox("1. Resistant weight gain patterns or unexplained metabolic plateaus?")
    s2 = st.checkbox("2. Waking up profoundly fatigued or tracking severe morning brain fog?")
    s3 = st.checkbox("3. Active androgenic disruptions (cystic acne flareups, unexpected hair thinness)?")
    s4 = st.checkbox("4. Irregular menstrual spacing, heavily delayed cycles, or complete stalls?")
    s5 = st.checkbox("5. Chronic room temperature sensitivities (unusually cold extremities or hot flashes)?")
    s6 = st.checkbox("6. Heightened psychological pacing, mood swings, or unprovoked anxiety spikes?")
    s7 = st.checkbox("7. Powerful late-night carbohydrate, sodium, or sugar processing cravings?")
    s8 = st.checkbox("8. Joint stiffness, persistent body aches, or muscular lethargy upon waking?")
    s9 = st.checkbox("9. Persistent facial water retention, puffiness, or dry localized skin patches?")
    s10 = st.checkbox("10. Recorded insulin resistance markers or paternal diabetic traits?")
    
    p_calc = (sum([s1, s3, s4, s6, s7, s10]) / 6) * 100
    t_calc = (sum([s1, s2, s5, s6, s8, s9]) / 6) * 100
    
    if p_calc == 0 and t_calc == 0: st.session_state.survey_score = "General Wellness Core"
    elif p_calc >= t_calc: st.session_state.survey_score = "PCOS Focus Protocol"
    else: st.session_state.survey_score = "Hypothyroidism Target"
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✨ Lock Symptom Vectors & Progress"):
        jump_to_window(4)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 4: BMI LAB & RE-CALIBRATED CONVERTERS
# ==========================================
elif st.session_state.active_window == 4:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📐 Physical Biometrics & Stratification Lab</h3>", unsafe_allow_html=True)
    
    u_wt = st.session_state.user_data.get('weight', 68.0)
    u_ht = st.session_state.user_data.get('height', 162.0)
    
    with st.expander("🔄 Open Metric Converter Tool (Push Up/Down for Imperial Variables)", expanded=False):
        uc1, uc2 = st.columns(2)
        with uc1:
            lbs_in = st.number_input("Weight conversion value from Pounds (lbs):", value=float(u_wt * 2.20462))
            st.code(f"Parsed Metric: {lbs_in / 2.20462:.1f} kg")
        with uc2:
            st.markdown("**Height conversion from Feet/Inches:**")
            ft = st.number_input("Feet Units:", value=5)
            inch = st.number_input("Inches Units:", value=4)
            st.code(f"Parsed Metric: {(ft * 30.48) + (inch * 2.54):.1f} cm")
            
    h_m = u_ht / 100
    computed_bmi = u_wt / (h_m ** 2)
    
    st.markdown("---")
    st.markdown("#### Clinical Stratification Assessment")
    col_metric1, col_metric2 = st.columns([1, 2])
    with col_metric1:
        st.metric("Your Personal Mass Index (BMI)", f"{computed_bmi:.1f}")
    with col_metric2:
        if computed_bmi < 18.5: st.warning("🚨 **Classification: Underweight Range.** Mass reconstruction protocols required.")
        elif 18.5 <= computed_bmi <= 24.9: st.success("🌸 **Classification: Normal Range.** Optimal physiological equilibrium parameters maintained.")
        elif 25.0 <= computed_bmi <= 29.9: st.warning("⚠️ **Classification: Overweight Range.** Deficit calibration matrices indicated.")
        else: st.error("🚨 **Classification: Obese Range.** High baseline metabolic stress signature.")
        
    st.markdown("<br><hr style='border-color: #F0E4EC;'><br>", unsafe_allow_html=True)
    st.session_state.target_goal = st.selectbox("Configure Targeted 30-Day Adherence Challenge Track:", ["Weight Loss Deficit Track", "Weight Gain Surplus Track"])
    
    if st.button("🎯 Finalize & Open My 30-Day Challenge Pack"):
        jump_to_window(5)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 5: THE 30-DAY CHALLENGE PACK (ROBUST STATIC RESOURCE MATRIX)
# ==========================================
elif st.session_state.active_window == 5:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📅 The 30-Day Endocrine Challenge Matrix ({st.session_state.target_goal.split(' ')[0]} Mode)</h3>", unsafe_allow_html=True)
    st.write(f"Screening Context: **{st.session_state.survey_score}**")
    
    st.image("https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1200", caption="Aura Studio Curated Balanced Indian Culinary Blueprint", use_container_width=True)
    
    active_phase = st.radio("Select Target Challenge Timeline Window:", ["Phase 1 (Days 1-10)", "Phase 2 (Days 11-20)", "Phase 3 (Days 21-30)"], horizontal=True)
    
    # COMPLETE SEPARATED MULTI-DIMENSIONAL SYSTEM RE-STRUCTURE
    if "PCOS" in st.session_state.survey_score:
        if "Loss" in st.session_state.target_goal:
            detox = "🧉 Morning: Warm Spearmint Leaf Tea + Cinnamon Grate (Targets insulin curves)"
            bfast = "🥣 Breakfast: 1 Fiber-dense Oats & Paneer Cheela with fresh Mint Chutney"
            lunch = "🍛 Lunch: 1 Cup Moong Dal Tadka + 1 cup stir-fried Bhindi Sabzi + 1 Missi Roti"
            snack = "☕ Evening: Green Tea served with a small bowl of dry-roasted unsalted Makhana"
            dinner = "🍲 Dinner: Light Lauki Oats Khichdi with fat-free curd"
            grocery = "✓ Rolled Organic Oats, Low-Fat Paneer, Fresh Spearmint leaves, Bran Flour, Bhindi"
            ex_title = "🏃‍♂️ Low-Cortisol Fat Loss Workout (Strength & Glucose Clearing)"
            ex_details = "• **Squats:** 3 sets x 15 reps (Rest 60s).<br>• **Wall Pushups:** 3 sets x 12 reps.<br>• **Post-Meal Walking:** 20 minutes slow-paced walk within 30 mins after your largest meal to clear glucose surges."
            yoga_title = "🧘‍♀️ Butterfly Pose (Baddha Konasana) for PCOS Pelvic Recovery"
            yoga_desc = "Sit straight, join the soles of your feet, and gently flutter your knees up and down. Maintain slow nasal breathing. • **Duration:** 8-10 mins daily. Stimulates healthy blood circulation to the reproductive axis."
            yoga_img = "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400"
        else: # PCOS Weight Gain
            detox = "🥛 Morning: Warm Almond-Date Infused Whole Milk (Calorie dense matrix start)"
            bfast = "🫓 Breakfast: 2 Paneer Stuffed Multigrain Parathas cooked in 1 tsp Ghee + Curd"
            lunch = "🍱 Lunch: 100g Paneer Tofu Bhurji Masala + 1 cup Dal Makhani + 2 Chapatis"
            snack = "🍌 Evening: 1 Large Banana + handful of Walnuts, Cashews, and Pumpkin seeds"
            dinner = "🍛 Dinner: High-protein Soya Chunks Rice Pulao + Thick Dal Tadka"
            grocery = "✓ Full-cream Milk, Desi Ghee, Organic Paneer, Walnuts, Soya Chunks, Basmati Rice"
            ex_title = "💪 Progressive Strength & Hypertrophy Track"
            ex_details = "• **Glute Bridges:** 3 sets x 12 reps (Hold for 2 seconds at peak contraction).<br>• **Chair Squats:** 3 sets x 10 reps (Slow down phase).<br>• **Plank Holds:** 3 sets x 45 seconds to secure core trunk line variables."
            yoga_title = "🧘‍♀️ Supta Baddha Konasana (Reclined Cobras Alignment)"
            yoga_desc = "Lie flat on your back with soles of feet touching, letting gravity gently expand the pelvic floor. • **Duration:** 10 mins. Lowers central nervous stress variables."
            yoga_img = "image_agent_tag_661660542252443559"
            yoga_img = "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400"
            
    elif "Thyroid" in st.session_state.survey_score:
        if "Loss" in st.session_state.target_goal:
            detox = "🌱 Morning: Warm Jeera Coriander Seed Infusion (Enhances kinetic metabolism thyroid spikes)"
            bfast = "🥣 Breakfast: 1 High-Protein Besan Onion Chilla + 2 boiled Egg Whites"
            lunch = "🍛 Lunch: Grilled Tofu chunks wok-tossed with sweet cooked carrots and 1 Chapati"
            snack = "🥥 Evening: Fresh Tender Coconut Water + 2 raw Brazil Nuts (Supreme Selenium source)"
            dinner = "🍲 Dinner: Well-cooked Pink Masoor Dal soup with half a cup of soft brown rice"
            grocery = "✓ Bengal Gram Besan, Firm Tofu, Raw Brazil Nuts, Sweet Carrots, Pink Masoor Dal"
            ex_title = "🔥 Cardio-Metabolic Awakening Deficit Framework"
            ex_details = "• **Brisk Walking:** 25-30 minutes under direct morning sunlight to synthesize Vitamin D and awaken thyroid cells.<br>• **Standing High Knees:** 3 sets x 20 reps to safely raise baseline resting metabolism variables."
            yoga_title = "🧘‍♀️ Supported Shoulder Stand (Sarvangasana) for Thyroid Gland Massaging"
            yoga_desc = "Lie on your back, lift your torso vertically, and support your lower back with your hands. • **Duration:** 3-5 mins. Induces hydrostatic parameters that stimulate the throat chakra axis."
            yoga_img = "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400"
        else: # Thyroid Weight Gain
            detox = "🥛 Morning: Warm Ashwagandha Turmeric Laced Dairy Milk (Lowers baseline TSH stress parameters)"
            bfast = "🫓 Breakfast: 2 Mixed Vegetable Parathas served with a dollop of fresh White Butter"
            lunch = "🍛 Lunch: Thick Arhar Dal Tarka + 100g Malai Paneer Subzi + 2 Soft Chapatis"
            snack = "🥑 Evening: Calorie-dense Mango/Avocado Shake with chia and sunflower seeds"
            dinner = "🍱 Dinner: Baked Herb Salmon Fillet OR Paneer Tikka Platter with Sweet Potato Mash"
            grocery = "✓ White Butter, Ashwagandha Churna, Malai Paneer, Chia Seeds, Arhar Dal, Sweet Potatoes"
            ex_title = "🏃‍♀️ Low-Intensity Mass Density Stabilization"
            ex_details = "• **Supported Wall Sits:** 3 sets x 30-second steady holds to secure quadriceps density templates.<br>• **Floor Bird-Dogs:** 3 sets x 10 reps per side to stabilize back extensor tissue lines cleanly."
            yoga_title = "🧘‍♀️ Fish Pose (Matsyasana) for Thyroid Extension"
            yoga_desc = "Arch your back while lying down, resting the crown of your head on the floor to expand your neck structure. • **Duration:** 4 mins. Restores optimal circulation arrays."
            yoga_img = "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400"
            
    else: # General Balance Fallback Paths
        detox = "🍀 Morning: Warm Fennel (Saunf) Water with a drop of organic Honey"
        bfast = "🥣 Breakfast: Savory Vegetable Dalia or Sprouted Moong Dal Chaat"
        lunch = "🍛 Lunch: 1 Bowl Mixed Lentil Soup + 1 cup seasonal Sabzi + 1 Multigrain Roti"
        snack = "☕ Evening: Herbal Tulsi tea with a palmful of dry roasted Almonds"
        dinner = "🍲 Dinner: Light Moong Dal Veggie Khichdi with a dash of lime juice"
        grocery = "✓ Broken Wheat Dalia, Sprouted Moong, Seasonal Vegetables, Almonds, Masoor Dal"
        ex_title = "🧘‍♀️ Structural Flexibility & Functional Mobility"
        ex_details = "• Full-body dynamic flexibility routines for 20 minutes daily.<br>• Maintain a baseline goal of 8,000 total stepping movements spread throughout the day."
        yoga_title = "🧘‍♀️ Child's Pose (Balasana) for Mind-Body Harmony"
        yoga_desc = "Kneel down, sit on your heels, extend your arms forward on the ground and lower your chest. • **Duration:** 5 mins. Decompresses spinal column links."
        yoga_img = "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400"

    # Push Columns Interface (Streamlit Expanders Layout)
    with st.expander("🥤 Step 1: Morning Detox Elixir Protocols (Click to Pull Up/Down)", expanded=True):
        st.markdown("<div class='detox-badge'>Active Intake Infusion</div>", unsafe_allow_html=True)
        st.write(f"**{detox}**")
        
    with st.expander("🍱 Step 2: Custom 4-Course Daily Meal Plans (Click to Pull Up/Down)", expanded=True):
        st.markdown(f"<div class='meal-box'><strong>🍳 Course 1: Breakfast</strong><br>{bfast}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-box'><strong>🍛 Course 2: Mid-Day Lunch</strong><br>{lunch}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-box'><strong>🥗 Course 3: Evening Vitality Snack</strong><br>{snack}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-box'><strong>🌙 Course 4: Restorative Night Repair Dinner</strong><br>{dinner}</div>", unsafe_allow_html=True)
        
    with st.expander("🛒 Step 3: Shopping Manifest & Grocery List (Click to Pull Up/Down)", expanded=False):
        st.markdown(f"<div class='grocery-box'>{grocery}</div>", unsafe_allow_html=True)

    with st.expander(f"🏋️‍♀️ Step 4: {ex_title} (Click to Pull Up/Down)", expanded=True):
        st.markdown(f"<div style='background-color:rgba(255,255,255,0.7); padding:15px; border-radius:10px; border-left:4px solid #A7F3D0;'>{ex_details}</div>", unsafe_allow_html=True)
        
    with st.expander(f"🧘‍♂️ Step 5: {yoga_title} (Click to Pull Up/Down)", expanded=False):
        ey1, ey2 = st.columns([1, 2])
        with ey1:
            st.image(yoga_img, use_container_width=True, caption="Asana Execution Guide")
        with ey2:
            st.write(yoga_desc)
            
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔒 Proceed to Live Daily Compliance Center"):
        jump_to_window(6)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 6: COMPLIANCE, CALORIES & PROVIDER LOCATOR
# ==========================================
elif st.session_state.active_window == 6:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>🚨 Safety Compliance Alarms & Regional Provider Networks</h3>", unsafe_allow_html=True)
    
    u_city_verified = st.session_state.user_data.get('location', 'Lucknow, Uttar Pradesh')
    w_target_metric = float(st.session_state.user_data.get('weight', 68.0) * 0.035)
    
    hud1, hud2 = st.columns(2)
    with hud1:
        st.markdown("#### ⏰ Active Patient Alarm Systems")
        st.checkbox("🔔 Water Hydration Intake Alarm (Every 60 minutes)")
        st.checkbox("💊 Pre-Meal empty stomach hormonal prescription medication alarm tracker log")
        
        st.markdown("---")
        st.markdown("#### 🍎 Multi-Food Caloric Dictionary Index")
        food_query = st.selectbox("Search Indian Pantry Base Calories:", ["1 Wheat Chapati", "100g Paneer Bhurji", "1 Bowl Moong Dal Khichdi", "1 Whole Boiled Egg", "100g Chicken Breast (Grilled)", "1 Roasted Papad", "1 Bowl Dal Tadka"])
        dictionary_cal = {"1 Wheat Chapati": "85 kcal", "100g Paneer Bhurji": "190 kcal", "1 Bowl Moong Dal Khichdi": "220 kcal", "1 Whole Boiled Egg": "78 kcal", "100g Chicken Breast (Grilled)": "165 kcal", "1 Roasted Papad": "35 kcal", "1 Bowl Dal Tadka": "150 kcal"}
        st.code(f"Database Density Analysis: {dictionary_cal[food_query]}")
        
        st.markdown("---")
        st.markdown("#### 🥛 Real-time Hydration Tracker Progress")
        drunk_glasses = st.slider("Glasses logged today (250ml capacity units):", 0, 16, 4)
        logged_liters = drunk_glasses * 0.25
        st.progress(min(logged_liters / w_target_metric, 1.0))
        st.write(f"Logged Status: **{logged_liters:.2f} L** out of your clinical baseline **{w_target_metric:.1f} L**")
        
    with hud2:
        st.markdown("#### 📍 Geolocation Health Center Locator")
        st.info(f"🛰️ Active Geolocation Signal: Locked near **{u_city_verified}**")
        
        st.markdown("##### Closest Specialized Diagnostics & Pharmacy Nodes found:")
        st.markdown(f"""
        <div class='provider-box'>
            <strong>🏥 Emergency Medical Center & Endocrine Specialists</strong><br>
            Location Coordinates: Regional Peripheral Ward, {u_city_verified.split(',')[0]} • Specialized Diagnostic Wing Active
        </div>
        <div class='provider-box'>
            <strong>💊 Apollo Pharmacy 24x7 Retail Outlets</strong><br>
            Distance Mapping: 0.7 km • Verified supply chain links for specialized hormonal medications
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color: #F0E4EC;'><br>", unsafe_allow_html=True)
    
    # THE PROFESSIONAL FOUNDER MATRIX BRAND ARCHITECTURE SECTION
    st.markdown(f"""
    <div class='founder-card'>
        <h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E; margin-top:0;'>👩‍⚕️ Clinical Product Leadership Matrix</h3>
        <h4 style='color: #8A6F8A; margin-top:5px; font-weight:600; letter-spacing:0.5px;'>Maihwish Rizvi | Registered Pharmacist</h4>
        <p style='line-height:1.6; font-size:0.95rem; color:#4A3E3D; margin-top:12px;'>
            As a <strong>Registered Pharmacist</strong>, my formal clinical evaluation training allows me to design user-friendly digital medical 
            products that target actual baseline neuroendocrine mechanisms rather than superficial fitness trends. By coupling multi-window biological 
            calibrations with a tailored <strong>Indian culinary palate</strong>, AuraWellness Studio presents an enterprise-ready healthcare surveillance architecture 
            optimized for rigorous patient safety compliance tracking protocols.
        </p>
        <hr style='border-color: #EADCE3; margin: 15px 0;'>
        <p style='font-size:0.8rem; color:#8A6F8A; margin:0;'><strong>Registered Demographics Audit:</strong> Name: {st.session_state.user_data.get('name')} • Contact: {st.session_state.user_data.get('phone')} • History: {st.session_state.user_data.get('history')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↩️ Reset Platform Surveillance Session"):
        jump_to_window(1)
    st.markdown("</div>", unsafe_allow_html=True)
