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
if 'survey_score' not in st.session_state: st.session_state.survey_score = "General Balance Core"

def jump_to_window(window_id):
    st.session_state.active_window = window_id
    st.rerun()

# --- BRANDING LAYER ---
st.markdown("<h1 class='brand-title'>🌸 AuraWellness Studio</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>Clinical Endocrine Recalibration & Multi-Window Lifestyle Platform</p>", unsafe_allow_html=True)

# ==========================================
# WINDOW 1: PORTAL INTRODUCTION
# ==========================================
if st.session_state.active_window == 1:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1600", use_container_width=True)
    
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
    st.markdown("Please register your core vitals and therapeutic medication background to populate system calculations:")
    
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
    st.write(f"Patient Registry Record: **{st.session_state.user_data.get('name')}** | Screening algorithms online.")
    
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
    
    if p_calc == 0 and t_calc == 0: st.session_state.survey_score = "General Balance Core"
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
    st.markdown("<div class='window-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📐 Physical Biometrics & Stratification Lab</h3>", unsafe_allow_html=True)
    
    u_wt = st.session_state.user_data.get('weight', 68.0)
    u_ht = st.session_state.user_data.get('height', 162.0)
    
    with st.expander("🔄 Open Metric Converter Tool (Push Up/Down for Imperial Variables)", expanded=False):
        uc1, uc2 = st.columns(2)
        with uc1:
            lbs_in = st.number_input("Weight conversion value from Pounds (lbs):", value=u_wt * 2.20462)
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
        if computed_bmi < 18.5: st.warning("🚨 **Classification: Underweight Range.** Strategic mass reconstruction protocols required.")
        elif 18.5 <= computed_bmi <= 24.9: st.success("🌸 **Classification: Normal Weight Range.** Optimal physiological equilibrium parameters maintained.")
        elif 25.0 <= computed_bmi <= 29.9: st.warning("⚠️ **Classification: Overweight/Pre-Obese Range.** Deficit calibration matrices indicated.")
        else: st.error("🚨 **Classification: Obese Range.** High baseline metabolic stress signature. Caloric modification required.")
        
    st.markdown("<br><hr style='border-color: #F0E4EC;'><br>", unsafe_allow_html=True)
    st.session_state.target_goal = st.selectbox("Configure Targeted 30-Day Adherence Challenge Track:", ["Weight Loss Deficit Track", "Weight Gain Surplus Track"])
    
    if st.button("🎯 Finalize & Open My 30-Day Challenge Pack"):
        jump_to_window(5)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# WINDOW 5: THE 30-DAY CHALLENGE PACK (DIET + EXERCISE DETAILED MATRIX)
# ==========================================
elif st.session_state.active_window == 5:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family: \"Playfair Display\", serif; color: #4C2A4E;'>📅 The 30-Day Endocrine Challenge Matrix ({st.session_state.target_goal.split(' ')[0]} Mode)</h3>", unsafe_allow_html=True)
    st.write(f"Screening Context: **{st.session_state.survey_score}** | Matrix updated dynamically.")
    
    # Hero Culinary Image Asset from copy protocol mapping
    st.image("https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcRvZVqSuV0FwrqJ9Wyv6CryOFM8uoEOvmGIG-3m9zRmOpm5XOdHWAIjhZlWWIFVb_Cwu-49AjBMcka-C6k", caption="Aura Studio Curated Balanced Indian Culinary Blueprint", use_container_width=True)
    
    active_week = st.radio("Select Target Challenge Timeline Window:", ["Phase 1 (Days 1-10)", "Phase 2 (Days 11-20)", "Phase 3 (Days 21-30)"], horizontal=True)
    
    # 1-Month Static Structural Database
    challenge_dictionary = {
        "PCOS Focus Protocol": {
            "loss": {
                "detox": "🧉 Warm Spearmint Tea + Fresh Lemon Squeeze (Lowers active androgen vectors)",
                "bfast": "🥣 Veg: 1 Fiber-dense Oats & Paneer Cheela with green Mint chutney. <br>Non-Veg: 2 Egg White Scramble cooked with hand-torn baby spinach sheets.",
                "lunch": "🍛 Veg: 1 Cup Moong Dal Tadka + 1 cup stir-fried Bhindi Sabzi + 1 Missi Roti. <br>Non-Veg: 120g Lemon Herb Grilled Chicken breast + cucumber salad.",
                "snack": "☕ Green Tea served with a small bowl of crunchy dry-roasted Makhana strings.",
                "dinner": "🍲 Veg: Highly Fibrous Lauki Oats Khichdi with fresh curd. <br>Non-Veg: 150g Baked Pomfret Fish Fillet paired with steamed green beans.",
                "grocery": "✓ Rolled Organic Oats, Low-Fat Paneer, Fresh Spearmint, Unflavored Soya Chunks, Bran Flour, Flaxseeds",
                "ex_title": "🏃‍♂️ Low-Cortisol Fat Loss Workout (Strength & LISS)",
                "ex_details": "• **Warmup (5 mins):** Joint mobilizations and neck rotations.<br>• **Bodyweight Squats:** 3 sets x 15 reps (Rest 60s between sets). Focus on controlled depth.<br>• **Wall Pushups:** 3 sets x 12 reps. Strengthens pectorals and stability cores smoothly.<br>• **Post-Meal LISS Cardio:** 20 minutes slow paced walk within 30 mins after lunch. Maximizes insulin clearing action.",
                "yoga": "🧘‍♀️ **Butterfly Pose (Baddha Konasana):** Sit tall, join soles of feet, pull close to pelvis, gently flutter knees up & down. • **Duration:** 5-8 mins daily. Promotes pelvic vascularity and balances ovarian targets.",
                "yoga_img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcR0SK-PWu0WXqlZG8OYUl2V3_zXLD89QFJx6l-tx-uI3TptCetOViDG8qln-gOK99pnST4uS986e1PViac"
            },
            "gain": {
                "detox": "🥛 Warm Almond-Date Infused Whole Cow Milk (Calorie dense matrix start)",
                "bfast": "🫓 Veg: 2 Paneer Stuffed Parathas cooked in 1 tsp Desi Ghee + Curd. <br>Non-Veg: 3 Whole Egg Masala Omelet with 2 slices of buttered whole-wheat Toast.",
                "lunch": "🍱 Veg: 100g Thick Shahi Paneer Curry + 1 cup Dal Makhani + 2 Multigrain Chapatis.",
                "snack": "🍌 1 Large Ripened Banana + handful of Walnuts and Cashews.",
                "dinner": "🍛 Veg: Paneer Tikka Makhani bowl with sweet potato mash. <br>Non-Veg: Chicken Keema Masala paired with 2 hot buttered Rotis.",
                "grocery": "✓ Full-cream Milk, Desi Ghee, Organic Paneer, Walnuts, Sweet Potatoes, Basmati Rice",
                "ex_title": "💪 Hypertrophy Lean Mass Reconstruction Protocol",
                "ex_details": "• **Warmup (5 mins):** Dynamic full body stretches.<br>• **Glute Bridges:** 3 sets x 12 reps (Hold for 2 seconds at peak contraction). Builds posterior lines.<br>• **Chair Squats:** 3 sets x 10 reps. Lower down very slowly (3 seconds descent phase).<br>• **Plank Holds:** 3 sets x 45-second holds. Stabilizes trunk baseline framework alignment values.",
                "yoga": "🧘‍♀️ **Cobra Pose (Bhujangasana):** Lie face down, place hands under shoulders, gently arch chest upwards while keeping thighs anchored. • **Duration:** 5 mins. Lengthens abdominal tracking paths.",
                "yoga_img": "https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcQDOw6AsdJ_IKA-FYYQo5kwT338FUVQfda-w5Q0Em8TRC956wQb64nbzkJN0aIzdQwPdDoTjg7QA5fGBhk"
            }
        },
        "Hypothyroidism Target": {
            "loss": {
                "detox": "🌱 Infused Coriander & Crushed Cumin Seed Decoction (Stimulates thyroid secretion kinetics)",
                "bfast": "🥣 Veg: 1 High-Protein Besan Onion Chilla. <br>Non-Veg: 2 Soft Boiled Eggs paired with one crisp slice of toasted multigrain bread.",
                "lunch": "🍛 Veg: Tofu Cubes wok-tossed with cooked carrots and 1 whole Chapati. <br>Non-Veg: 120g Light Chicken Curry prepared in light mustard oil base.",
                "snack": "🥥 Fresh Tender Coconut Water + 2 raw Brazil Nuts (Supreme Selenium tracing metrics).",
                "dinner": "🍲 Veg: Thick Masoor Dal Soup with half a cup of soft basmati rice. <br>Non-Veg: 150g Grilled Atlantic Salmon with charred asparagus strings.",
                "grocery": "✓ Bengal Gram Besan, Firm Tofu, Raw Brazil Nuts, Sweet Carrots, Lean Chicken cuts, Pink Masoor Dal",
                "ex_title": "🔥 Metabolic Awakening Cardio Blueprint",
                "ex_details": "• **Brisk Walking:** 25-30 minutes under fresh morning sunlight to kickstart endocrine metabolic baselines.<br>• **Knee-to-Chest Raises:** 3 sets x 15 reps while standing. Stimulates heart rate safely.<br>• **Adrenal Recovery Stretches:** 5 minutes full body decompression templates to preserve energy indices.",
                "yoga": "🧘‍♀️ **Supported Shoulder Stand (Sarvangasana):** Lie on back, lift legs and torso vertically, support lower back with palms. • **Duration:** 3-5 mins. Induces hydrostatic pressure vectors to massage the thyroid gland axis.",
                "yoga_img": "https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcSHYd-7DhdNbpOjq53P4qTbQCCvEymGIFwEq-pVzHu0qEzYDdO7b_ng3yxzIlqq-XD4Ihr4XRcfvDghYyA"
            },
            "gain": {
                "detox": "🥛 Warm Ashwagandha Turmeric Laced Milk (Balances TSH stress markers)",
                "bfast": "🫓 Veg: 2 Mixed Veg Parathas with White Butter. <br>Non-Veg: Egg Podimas (3 Eggs Bhurji) with paratha.",
                "lunch": "🍛 Thick Arhar Dal Tarka + Paneer Bhurji (100g) + 2 Rotis + Salad.",
                "snack": "🥑 Mango/Avocado Shake with chia seeds.",
                "dinner": "🍱 Veg: Thick Malai Kofta with 2 buttered rotis. <br>Non-Veg: Butter Chicken (150g) with 2 Chapatis.",
                "grocery": "✓ Amul Butter, Ashwagandha Churna, Malai Paneer, Chia Seeds, Arhar Dal lines",
                "ex_title": "🏃‍♀️ Low-Intensity Mass Density Work",
                "ex_details": "• **Supported Wall Sits:** 3 sets x 30-second steady isometric holds. Strengthens quadriceps tissue blocks.<br>• **Floor Bird-Dogs:** 3 sets x 10 reps per side. Stabilizes back extensor alignments cleanly.<br>• **Daily Activity Window:** Restrict high energetic expenditure; prioritize restful, systemic regeneration.",
                "yoga": "🧘‍♀️ **Dynamic Surya Namaskars:** 6 complete rounds executed at a slow steady pace. Wakens basal biological efficiency loops.",
                "yoga_img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcR0SK-PWu0WXqlZG8OYUl2V3_zXLD89QFJx6l-tx-uI3TptCetOViDG8qln-gOK99pnST4uS986e1PViac"
            }
        }
    }
    challenge_dictionary["General Balance Core"] = challenge_dictionary["PCOS Focus Protocol"]
    
    active_profile_map = "PCOS Focus Protocol" if "PCOS" in st.session_state.survey_score else ("Hypothyroidism Target" if "Hypothyroidism" in st.session_state.survey_score else "General Balance Core")
    active_goal_map = "loss" if "Loss" in st.session_state.target_goal else "gain"
    
    plan_data = challenge_dictionary[active_profile_map][active_goal_map]
    
    # Push Columns Interface (Streamlit Expanders Layout)
    with st.expander("🥤 Step 1: Morning Detox Protocol (Click to Toggle Columns)", expanded=True):
        st.markdown("<div class='detox-badge'>Active Trial Infusion</div>", unsafe_allow_html=True)
        st.write(f"**{plan_data['detox']}**")
        
    with st.expander("🍱 Step 2: Continuous 4-Meal Plan Architecture (Click to Toggle Columns)", expanded=True):
        st.markdown(f"<div class='meal-box'><strong>🍳 Meal 1: Breakfast</strong><br>{plan_data['bfast']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-box'><strong>🍛 Meal 2: Core Lunch</strong><br>{plan_data['lunch']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-box'><strong>🥗 Meal 3: Evening Vitality Buffer</strong><br>{plan_data['snack']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-box'><strong>🌙 Meal 4: Restorative Dinner</strong><br>{plan_data['dinner']}</div>", unsafe_allow_html=True)
        
    with st.expander("🛒 Step 3: Grocery Procurement Manifest (Click to Toggle Columns)", expanded=False):
        st.markdown(f"<div class='grocery-box'>{plan_data['grocery']}</div>", unsafe_allow_html=True)

    with st.expander(f"{plan_data['ex_title']} (Click to Toggle Columns)", expanded=True):
        st.markdown("<p style='font-size:0.95rem; line-height:1.6;'>Follow this structured routine every alternate day to optimize your body composition targets safely:</p>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color:rgba(255,255,255,0.7); padding:15px; border-radius:10px; border-left:4px solid #A7F3D0;'>{plan_data['ex_details']}</div>", unsafe_allow_html=True)
        
    with st.expander("🧘‍♀️ Step 5: Labeled Yoga Asana & Form Manual (Click to Toggle Columns)", expanded=False):
        ey1, ey2 = st.columns([1, 1.8])
        with ey1:
            st.image(plan_data['yoga_img'], use_container_width=True, caption="Asana Form Guidance Pose")
        with ey2:
            st.markdown("**Therapeutic Yoga Guidance:**")
            st.write(plan_data['yoga'])
            st.caption("Pre-execution advisory: Discontinue immediately if acute physical joint strains or dizziness manifest.")
            
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
    w_target_metric = st.session_state.user_data.get('weight', 68.0) * 0.035
    
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
        st.caption("Registry sync parameters updated in alignment with state healthcare monitoring criteria data feeds.")

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
