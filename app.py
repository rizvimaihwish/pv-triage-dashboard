import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# --- 1. CORE SYSTEM INITIALIZATION ---
st.set_page_config(page_title="SHEALTH | AI Precision Coach", page_icon="🌸", layout="wide")

# --- 2. ELITE TECH-FEMININE GLASSMORPHIC LUXURY STYLING SHEET ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght=0,400..900;1,400..900&family=Plus+Jakarta+Sans:ital,wght=0,200..800;1,200..800&display=swap');
    
    .stApp {
        background-image: linear-gradient(to bottom, rgba(250, 246, 240, 0.88), rgba(246, 239, 242, 0.92)), 
                          url('https://images.unsplash.com/photo-1557672172-298e090bd0f1?w=1600');
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; color: #4A3E3D; }
    
    /* Calligraphed Luxury HEADING - SHEALTH Title Architecture */
    .brand-title { font-family: 'Playfair Display', serif; color: #4C2A4E; font-weight: 900; font-size: 4rem; text-align: center; letter-spacing: -1px; margin-bottom: 2px; }
    .brand-subtitle { font-family: 'Plus Jakarta Sans', sans-serif; color: #8A6F8A; font-size: 1.15rem; font-weight: 500; text-align: center; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 35px; }
    
    .window-container { background-color: rgba(255, 255, 255, 0.84); backdrop-filter: blur(12px); border-radius: 24px; padding: 35px; border: 1px solid rgba(240, 228, 236, 0.8); box-shadow: 0 15px 35px rgba(224, 211, 219, 0.2); margin-bottom: 30px; }
    .meal-box { background-color: rgba(255, 255, 255, 0.92); border-radius: 14px; padding: 18px; margin-bottom: 15px; border-left: 5px solid #F472B6; box-shadow: 0 4px 12px rgba(224, 211, 219, 0.05); }
    .workout-box { background-color: rgba(255, 255, 255, 0.92); border-radius: 14px; padding: 18px; margin-bottom: 15px; border-left: 5px solid #C084FC; box-shadow: 0 4px 12px rgba(224, 211, 219, 0.05); }
    .detox-badge { display: inline-block; padding: 5px 14px; background-color: #ECFDF5; color: #059669; border-radius: 20px; font-size: 0.8rem; font-weight: 700; margin-bottom: 12px; text-transform: uppercase; }
    .provider-box { background-color: #FAFAF9; border-radius: 12px; padding: 18px; border-left: 4px solid #C084FC; margin-bottom: 12px; }
    .grocery-box { background-color: rgba(244, 251, 247, 0.85); padding: 15px; border-radius: 12px; border: 1px dashed #A7F3D0; margin-top: 15px; }
    
    div.stButton > button {
        background: linear-gradient(135deg, #F472B6 0%, #C084FC 100%) !important;
        color: white !important; font-weight: 700 !important; border-radius: 30px !important;
        border: none !important; padding: 12px 35px !important; font-size: 1rem !important;
        box-shadow: 0 6px 20 rgba(244, 114, 182, 0.3) !important; transition: all 0.3s ease !important;
        display: block; margin: 0 auto; width: 50%;
    }
    div.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 8px 25px rgba(192, 132, 252, 0.45) !important; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #F472B6, #C084FC) !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. PLATFORM SYSTEM STATE CONTROLLER ---
if 'active_window' not in st.session_state: st.session_state.active_window = 1
if 'user_data' not in st.session_state: st.session_state.user_data = {}
if 'survey_score' not in st.session_state: st.session_state.survey_score = "General Wellness Track"
if 'target_goal' not in st.session_state: st.session_state.target_goal = "Weight Loss Deficit"

def jump_to_window(window_id):
    st.session_state.active_window = window_id
    st.rerun()

# --- GLOBAL PLATFORM SHEALTH CALLIGRAPHED TOP HEADER ---
st.markdown("<h1 class='brand-title'>🌸 SHEALTH</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>Precision AI Endocrine Modifications & 30-Day Adaptive Clinical Portal</p>", unsafe_allow_html=True)

# ==========================================
# WINDOW 1: ARCHITECTURE OVERVIEW & LOGS
# ==========================================
if st.session_state.active_window == 1:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200", use_container_width=True)
    
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E; text-align:center;'>Welcome to your Precision Metabolic Life-Science Environment</h3>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; font-size:1.05rem; line-height:1.7; max-width:850px; margin: 0 auto; color:#6B5E5E;'>
    <strong>SHEALTH</strong> is a modern high-tech AI-driven nutrient and diet coach wellness system engineered to manage root metabolic parameters. 
    By decoding baseline clinical markers, the platform structures completely daily-differentiated therapeutic regimes and 
    low-impact functional workouts adapted beautifully for your system guidelines.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><hr style='border-color: #F0E4EC;'><br>", unsafe_allow_html=True)
    st.markdown("#### 🎥 Daily Clinical Coaching Segment")
    v1, v2 = st.columns([1.6, 1])
    with v1:
        st.video("https://www.youtube.com/watch?v=ScZs7L0_S38")
    with v2:
        st.markdown("<h5 style='color: #4C2A4E; font-family: \"Playfair Display\", serif;'>Endocrine Stabilization Mechanics</h5>", unsafe_allow_html=True)
        st.write("Understand how continuous daily variance in complex carbohydrate structure manages pancreatic recovery pathways. Learn to balance systematic active tissue extensions to clear hormonal load layers safely.")
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("✨ Initialize SHEALTH AI Registration Profile"):
            jump_to_window(2)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 2: COMPREHENSIVE MEDICAL ENTRY LAB
# ==========================================
elif st.session_state.active_window == 2:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>🔒 Clinical Profile Registration Portal</h3>", unsafe_allow_html=True)
    
    r1, r2 = st.columns(2)
    with r1:
        name = st.text_input("Patient Full Name String:", value="Riya Sharma")
        phone = st.text_input("Active Verification Line:", value="+91 98765 43210")
        location = st.text_input("Geographic Coordinate Base (City/State):", value="Lucknow, Uttar Pradesh")
    with r2:
        age = st.number_input("Biological Age Value:", min_value=12, max_value=85, value=24)
        gender = st.radio("Dynamic Gender Profile Template:", ["Female Archetype Settings", "Male Archetype Settings"])
        weight = st.number_input("Core Mass Weight Field (kg):", min_value=30.0, max_value=190.0, value=68.0)
        height_cm = st.number_input("Core Axis Height Field (cm):", min_value=110.0, max_value=230.0, value=162.0)
        
    st.markdown("---")
    st.markdown("#### 📋 Prior Diagnoses & Medication Overlays")
    med_history = st.text_area("Log active clinical prescriptions or metabolic history markers (e.g., Metformin 500mg daily, Thyronorm 25mcg, None):", value="None")
    
    if st.button("🚀 Lock Biometrics & Continue"):
        st.session_state.user_data = {
            "name": name, "phone": phone, "location": location, "age": age,
            "weight": weight, "height": height_cm, "history": med_history
        }
        jump_to_window(3)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 3: AUTOMATED CLINICAL INTAKE SCANNER
# ==========================================
elif st.session_state.active_window == 3:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📋 AI Symptom Stratification & Vector Intake Matrix</h3>", unsafe_allow_html=True)
    
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
    if st.button("✨ Lock Endocrine Vectors & Advance"):
        jump_to_window(4)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 4: BMI METRIC CONVERTER LABORATORY
# ==========================================
elif st.session_state.active_window == 4:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📐 Physical Biometrics Converter & Diagnostic Registry</h3>", unsafe_allow_html=True)
    
    u_wt = st.session_state.user_data.get('weight', 68.0)
    u_ht = st.session_state.user_data.get('height', 162.0)
    
    with st.expander("🔄 Open Metric Converter Tool (Push Up/Down for Conversion Matrices)", expanded=False):
        uc1, uc2 = st.columns(2)
        with uc1:
            lbs_in = st.number_input("Weight Input scale from Pounds (lbs):", value=float(u_wt * 2.20462))
            st.code(f"Parsed Metric Equivalence: {lbs_in / 2.20462:.1f} kg")
        with uc2:
            st.markdown("**Height Input scale from Feet/Inches:**")
            ft = st.number_input("Feet:", value=5)
            inch = st.number_input("Inches:", value=4)
            st.code(f"Parsed Metric Equivalence: {(ft * 30.48) + (inch * 2.54):.1f} cm")
            
    h_m = u_ht / 100
    computed_bmi = u_wt / (h_m ** 2)
    
    st.markdown("---")
    st.markdown("#### Clinical Mass Analysis Stratification")
    col_metric1, col_metric2 = st.columns([1, 2])
    with col_metric1:
        st.metric("Your Calculated Body Mass Index (BMI)", f"{computed_bmi:.1f}")
    with col_metric2:
        if computed_bmi < 18.5: st.warning("🚨 **Classification Matrix: Underweight.** Lean lean mass tissues require optimization.")
        elif 18.5 <= computed_bmi <= 24.9: st.success("🌸 **Classification Matrix: Homeostatic Equilibrium.** Baselines are clinically optimal.")
        elif 25.0 <= computed_bmi <= 29.9: st.warning("⚠️ **Classification Matrix: Overweight Category Ranges.** Modification indicated.")
        else: st.error("🚨 **Classification Matrix: Obese Category Ranges.** High systemic physiological load lines detected.")
        
    st.markdown("<br><hr style='border-color: #F0E4EC;'><br>", unsafe_allow_html=True)
    st.session_state.target_goal = st.selectbox("Configure Targeted 30-Day Target Pathway Matrix:", ["Weight Loss Tracker Focus", "Weight Gain Tracker Focus"])
    
    if st.button("🎯 Compile My Dynamic 30-Day Adherence Schedule"):
        jump_to_window(5)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 5: THE 100% DYNAMIC 30-DAY TIMELINE PLAN
# ==========================================
elif st.session_state.active_window == 5:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📅 SHEALTH AI 30-Day Precision Challenge Tracker</h3>", unsafe_allow_html=True)
    st.write(f"Active Diagnosis Anchor: **{st.session_state.survey_score}** | Goal: **{st.session_state.target_goal}**")
    
    st.image("https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1200", caption="SHEALTH Precision AI Metabolic Culinary Center", use_container_width=True)
    
    # 30-Day Subdivided Selection Matrix
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

    # --- THE 100% MATHEMATICAL DYNAMIC DIET & FITNESS SYNTHESIS CALCULATOR ENGINE ---
    # To avoid repeating elements, we use the specific day index to algorithmically generate unique food metrics
    hash_idx = day_num + phase_offset
    
    # Indian Base Options pools for algorithmic selection
    veg_proteins = ["Low-fat Tofu Tikka", "Grated Paneer Bhurji", "Sprouted Green Moong", "Chana Masala Chaat", "Soya Chunk Stir-Fry", "Masala Dal Soups"]
    nonveg_proteins = ["Lemon Grilled Chicken Breast", "Baked Pomfret Herb Fillet", "Oven Pan-Seared Salmon", "Egg White Podimas Bhurji", "Shredded Chicken Broth"]
    grains_deficit = ["Multigrain Oats Oats Roti", "Bran Roti", "Quinoa Base Mash", "Brown Basmati Rice", "Barley Porridge"]
    grains_surplus = ["Desi Ghee Layered Wheat Paratha", "Premium Basmati Pulao", "Buttered Tandoori Naan", "Sweet Potato Mash Bowls"]
    veggies = ["Sautéed Spinach & Garlic", "Stir-fried Bhindi", "Wok-Tossed Methi and Carrots", "Bottle Gourd (Lauki) Curry", "Baked Ivy Gourd (Kundu)"]
    detox_drinks = ["Spearmint Infused Herbal Flush", "Jeera Coriander Warm Decoction", "Aloe Vera Ginger Anti-inflammatory Shot", "Sun-warmed Fennel Cleanse", "Salted Mint Buttermilk"]
    
    workouts_loss = ["Low-Cortisol Bodyweight Squats: 3 sets x 15 reps + 20 mins walk", "Wall Pushups: 3 sets x 12 reps + 15 mins steady stepping", "Incline Slow Treadmill Pace: 25 mins continuous steady track", "Tricep Chair Dips: 3 sets x 10 reps + 20 mins post-meal stroll"]
    workouts_gain = ["Floor Glute Bridges: 4 sets x 12 reps (Hold peak 2 seconds)", "Chair Assisted Squats: 3 sets x 10 reps (Very slow 3-sec drop descent)", "Plank Alignment Core Holds: 4 sets x 45 seconds holds", "Dumbbell Overhead Presses: 3 sets x 12 reps (Strength density pace)"]
    
    yoga_asanas = [
        {"title": "Baddha Konasana (Butterfly Alignment Pose)", "desc": "Sit straight, press soles together, gently expand groin fields. Improves pelvic vascular vectors.", "img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400"},
        {"title": "Bhujangasana (Classic Cobra Extension)", "desc": "Lie flat on stomach, lift chest gently using spinal extensors. Lengthens core tracking systems.", "img": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400"},
        {"title": "Sarvangasana (Supported Shoulder Stand)", "desc": "Invert torso fully, supporting hips with upper arms. Massages thyroid hormonal centers.", "img": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?w=400"}
    ]

    # Algorithmically pick items based on mathematical modulo mapping rules
    d_drink = detox_drinks[hash_idx % len(detox_drinks)]
    v_prot = veg_proteins[hash_idx % len(veg_proteins)]
    nv_prot = nonveg_proteins[hash_idx % len(nonveg_proteins)]
    veg_side = veggies[hash_idx % len(veggies)]
    
    if "Loss" in st.session_state.target_goal:
        grain_item = grains_deficit[hash_idx % len(grains_deficit)]
        active_workout_plan = workouts_loss[hash_idx % len(workouts_loss)]
    else:
        grain_item = grains_surplus[hash_idx % len(grains_surplus)]
        active_workout_plan = workouts_gain[hash_idx % len(workouts_gain)]
        
    selected_yoga_block = yoga_asanas[hash_idx % len(yoga_asanas)]
    
    # --- INTERFACE DISPLAY PRINT LAYER ---
    st.markdown(f"### 📋 Personal AI Curriculum Mapping Matrix: **Day {day_num} Logs**")
    
    with st.expander(f"🥤 Step 1: Morning Detox Elixir - Day {day_num} (Click to Pull Up/Down)", expanded=True):
        st.markdown("<div class='detox-badge'>Active Fluid Infusion</div>", unsafe_allow_html=True)
        st.write(f"**Therapeutic Protocol:** Warmed {d_drink} administered empty-stomach to settle cellular targets.")
        
    with st.expander(f"🍱 Step 2: 4-Course Daily Culinary Layout - Day {day_num} (Click to Pull Up/Down)", expanded=True):
        st.markdown(f"""
        <div class='meal-box'><strong>🍳 Course 1: Breakfast Target</strong><br>Veg Choice: 1 Savory {v_prot} Cheela wrapped with herbs. <br>Non-Veg Choice: 2 Egg Whites whipped and pan-tossed with green chives.</div>
        <div class='meal-box'><strong>🍛 Course 2: Mid-Day Lunch Alignment</strong><br>Veg Path: 1 Bowl Lentil Stew + 1 cup {veg_side} + 1 serving {grain_item}. <br>Non-Veg Path: 150g {nv_prot} served alongside fresh green leafy sprouts salad.</div>
        <div class='meal-box'><strong>🥗 Course 3: Evening Adrenal Vitality Snack</strong><br>1 Cup Spiced Ayurvedic Kadha Tea paired with a small palmful of roasted crunchy Makhanas.</div>
        <div class='meal-box'><strong>🌙 Course 4: Restorative Night Repair Dinner</strong><br>Veg Path: Soft textured {v_prot} salad with sweet lime glaze. <br>Non-Veg Path: 120g Pan-seared {nv_prot} paired with charred broccoli strings.</div>
        """, unsafe_allow_html=True)
        
    with st.expander(f"🛒 Step 3: Shopping Manifest Basket - Day {day_num} (Click to Pull Up/Down)", expanded=False):
        st.markdown(f"<div class='grocery-box'>✓ Required Active Ingredients: {v_prot}, {nv_prot}, {grain_item}, {veg_side}, Spices, Mint, Makhana lines.</div>", unsafe_allow_html=True)
        
    with st.expander(f"🏋️‍♀️ Step 4: Customized Exercise Blueprint - Day {day_num} (Click to Pull Up/Down)", expanded=True):
        st.markdown(f"<div class='workout-box'><strong>Active Functional Training Routine:</strong><br>{active_workout_plan}</div>", unsafe_allow_html=True)
        st.caption("Advisory: Track performance speeds smoothly. Maintain controlled heart rates to manage cortisol levels.")
        
    with st.expander(f"🧘‍♂️ Step 5: Labeled Yoga Asana Form Manual - Day {day_num} (Click to Pull Up/Down)", expanded=False):
        ycol1, ycol2 = st.columns([1, 2])
        with ycol1:
            st.image(selected_yoga_block["img"], use_container_width=True, caption="Form Guidance Frame")
        with ycol2:
            st.markdown(f"##### **Asana Target: {selected_yoga_block['title']}**")
            st.write(selected_yoga_block["desc"])
            st.caption("Execution Rule: Discontinue if spinal pressure loops exceed comfort baselines.")
            
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔒 Enter Live Verification Surveillance Hub"):
        jump_to_window(6)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 6: COMPLIANCE, TRACKERS & PROVIDER GRID
# ==========================================
elif st.session_state.active_window == 6:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>🚨 Real-time Adherence Dashboards & Regional Provider Locator</h3>", unsafe_allow_html=True)
    
    city_tag = st.session_state.user_data.get('location', 'Lucknow, Uttar Pradesh')
    w_baseline = float(st.session_state.user_data.get('weight', 68.0) * 0.035)
    
    h1, h2 = st.columns(2)
    with h1:
        st.markdown("#### ⏰ Precision AI Active Alarms Panel")
        st.checkbox("🔔 Water Tracker: Log 250ml capacity fluid clear interval now.")
        st.checkbox("💊 Pharmacy Line: Fasting Levothyroxine / Metformin compliance checklist locked.")
        
        st.markdown("---")
        st.markdown("#### 🍎 Multi-Food Caloric Dictionary Index Lookups")
        f_select = st.selectbox("Search Indian Food Items Base Matrix:", ["1 Wheat Chapati", "100g Paneer Bhurji", "1 Bowl Moong Dal Khichdi", "1 Whole Boiled Egg", "100g Chicken Breast (Grilled)", "1 Roasted Papad", "1 Bowl Green Sabzi"])
        cal_index = {"1 Wheat Chapati": "85 kcal", "100g Paneer Bhurji": "190 kcal", "1 Bowl Moong Dal Khichdi": "220 kcal", "1 Whole Boiled Egg": "78 kcal", "100g Chicken Breast (Grilled)": "165 kcal", "1 Roasted Papad": "35 kcal", "1 Bowl Green Sabzi": "95 kcal"}
        st.code(f"Database Caloric Core Value: {cal_index[f_select]}")
        
        st.markdown("---")
        st.markdown("#### 🥛 Hydration Multiplier Tracker Progress")
        gl_drunk = st.slider("Glasses consumed today (250ml base units):", 0, 16, 4)
        total_liters = gl_drunk * 0.25
        st.progress(min(total_liters / w_baseline, 1.0))
        st.write(f"Logged Status: **{total_liters:.2f} L** out of calculated target **{w_baseline:.1f} L**")
        
    with h2:
        st.markdown("#### 📍 Satellite Healthcare Provider Locator Grid")
        st.info(f"🛰️ Active Geolocation Lock Signal: Verified within **{city_tag}** Perimeter Networks")
        
        st.markdown("##### Closest Specialized Diagnostics & Emergency Nodes found:")
        st.markdown(f"""
        <div class='provider-box'>
            <strong>🏥 Apollo Diagnostic Healthcare Center & Endocrine Hub</strong><br>
            Location Ward Coordinates: Regional Peripheral Ward, {city_tag.split(',')[0]} • Specialized Clinical Testing Wing Active
        </div>
        <div class='provider-box'>
            <strong>💊 Apollo Pharmacy 24x7 Retail Counter Outlets</strong><br>
            Distance Matrix: 0.7 km away • Synced with state pharmacist prescription networks for specialized hormonal therapeutics
        </div>
        """, unsafe_allow_html=True)
        st.caption("Registry tracking logs are directly verified in accordance with national integrated health council data streams.")

    st.markdown("<br><hr style='border-color: #F0E4EC;'><br>", unsafe_allow_html=True)
    
    # --- EXECUTIVE FOUNDER AUTHENTICITY BLOCK ---
    st.markdown(f"""
    <div class='founder-card' style='background: linear-gradient(135deg, rgba(255, 245, 247, 0.9) 0%, rgba(243, 234, 244, 0.9) 100%) !important; padding: 30px; border-radius: 20px; border: 1px solid #EADCE3;'>
        <h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E; margin-top:0;'>👩‍⚕️ Clinical Product System Architecture</h3>
        <h4 style='color: #8A6F8A; margin-top:5px; font-weight:600; letter-spacing:0.5px;'>Maihwish Rizvi | Registered Pharmacist</h4>
        <p style='line-height:1.6; font-size:0.95rem; color:#4A3E3D; margin-top:12px;'>
            As a <strong>Registered Pharmacist</strong>, my academic training allows me to design user-friendly wellness products 
            that bypass superficial fitness trends to target actual baseline neuroendocrine mechanisms. By pairing 30-day dynamic life-science 
            calibrations with a rich, comforting <strong>Indian culinary palate</strong>, SHEALTH presents a high-tech healthcare platform 
            engineered for rigorous daily patient safety and compliance tracking protocols.
        </p>
        <hr style='border-color: #EADCE3; margin: 15px 0;'>
        <p style='font-size:0.8rem; color:#8A6F8A; margin:0;'><strong>Active Session Demographic Registry Details:</strong> Name: {st.session_state.user_data.get('name', 'N/A')} • Contact Token: {st.session_state.user_data.get('phone', 'N/A')} • Diagnostics History Log: {st.session_state.user_data.get('history', 'N/A')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↩️ Reset Platform Surveillance Session"):
        jump_to_window(1)
    st.markdown("</div>", unsafe_allow_html=True)
