import streamlit as st
import streamlit.components.v1 as components

# 1. Setup Streamlit Page
st.set_page_config(page_title="SHEALTH+ | Advanced Clinical AI", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .block-container { padding: 0rem !important; max-width: 100% !important; }
        header { display: none !important; }
        footer { display: none !important; }
    </style>
""", unsafe_allow_html=True)

# 2. Ultra-Aesthetic HTML/JS Engine
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHEALTH+ | Aesthetic Clinical Precision</title>
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-pink: #F472B6;
            --deep-magenta: #8A1C5F; 
            --text-dark: #2D0A22; 
            --metallic-grey: #5a5a5f;
            --glass-bg: rgba(255, 255, 255, 0.45);
            --glass-border: rgba(255, 255, 255, 0.85);
            --glass-shadow: 0 10px 40px 0 rgba(138, 28, 95, 0.15);
            --input-glass: rgba(255, 255, 255, 0.55);
        }
        
        body, html {
            margin: 0; padding: 0;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: var(--text-dark) !important;
            min-height: 100vh;
            background-color: #fce4ec;
            background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop');
            background-size: cover; background-attachment: fixed; background-position: center;
            overflow-x: hidden;
        }

        .animated-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(45deg, rgba(244,114,182,0.15), rgba(233,213,255,0.15), rgba(255,218,185,0.15));
            background-size: 300% 300%; animation: pulseBg 12s ease infinite; pointer-events: none; z-index: -1;
        }
        @keyframes pulseBg { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }

        .calligraphy-title { 
            font-family: 'Great Vibes', cursive; font-size: 7.5rem; text-align: center; margin: 15px 0 5px; 
            background: linear-gradient(to right, #8A1C5F, #F472B6, #ffb6c1, #8A1C5F); background-size: 200% auto;
            color: transparent; -webkit-background-clip: text; background-clip: text;
            animation: shine 4s linear infinite; filter: drop-shadow(2px 4px 4px rgba(255,255,255,0.7));
        }
        @keyframes shine { to { background-position: 200% center; } }

        .doodle { position: fixed; pointer-events: none; opacity: 0.75; z-index: -1; }
        .doodle-bow { top: 5%; right: 10%; width: 70px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.15)); }
        .doodle-pill { bottom: 15%; left: 6%; width: 60px; transform: rotate(-20deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.15)); }
        .doodle-plant { position: fixed; bottom: 15px; right: 25px; width: 55px; transition: width 1.5s ease; z-index: 100; pointer-events: none;}

        .window-container {
            background: var(--glass-bg); backdrop-filter: blur(30px); -webkit-backdrop-filter: blur(30px);
            border: 1px solid var(--glass-border); border-radius: 40px; padding: 50px;
            box-shadow: var(--glass-shadow), inset 0 0 25px rgba(255,255,255,0.6);
            max-width: 1000px; margin: 30px auto 60px; position: relative; display: none;
            animation: floatUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        .active-window { display: block; }
        @keyframes floatUp { from { opacity: 0; transform: translateY(30px) scale(0.99); } to { opacity: 1; transform: translateY(0) scale(1); } }

        h3, h4 { font-family: 'Playfair Display', serif; color: var(--deep-magenta); }
        .quote { font-family: 'Playfair Display', serif; font-style: italic; text-align: center; color: var(--deep-magenta); margin: 30px 0 20px; font-size: 1.4rem; font-weight: bold; }

        input, textarea { 
            width: 100%; padding: 16px 25px; margin: 10px 0 25px; border-radius: 35px; 
            border: 1px solid var(--glass-border); background: var(--input-glass); backdrop-filter: blur(15px);
            color: var(--text-dark); font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.05rem; font-weight: 700;
            box-sizing: border-box; outline: none; box-shadow: inset 0 2px 8px rgba(0,0,0,0.04); transition: all 0.3s ease;
        }
        
        select {
            width: 100%; padding: 16px 25px; margin: 10px 0 25px; border-radius: 35px; 
            border: 1px solid var(--glass-border); background: var(--input-glass); backdrop-filter: blur(15px);
            color: var(--metallic-grey); text-shadow: 1px 1px 0px rgba(255,255,255,0.8);
            font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.05rem; font-weight: 800;
            box-sizing: border-box; outline: none; box-shadow: inset 0 2px 8px rgba(0,0,0,0.04); transition: all 0.3s ease;
            appearance: none;
            background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%235a5a5f%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E"); 
            background-repeat: no-repeat; background-position: right 20px top 50%; background-size: 14px auto; padding-right: 40px;
        }
        select option { background: rgba(255, 255, 255, 0.95); color: var(--metallic-grey); font-weight: bold; }
        input:focus, select:focus, textarea:focus { border-color: var(--deep-magenta); background: rgba(255, 255, 255, 0.85); box-shadow: 0 0 20px rgba(138, 28, 95, 0.3); }

        button {
            background: linear-gradient(145deg, #F472B6, #8A1C5F); color: white; font-weight: 800; border-radius: 40px; border: none;
            padding: 18px 50px; font-size: 1.2rem; cursor: pointer; display: block; margin: 30px auto;
            box-shadow: 0 12px 30px rgba(138, 28, 95, 0.4), inset 0 3px 6px rgba(255,255,255,0.3);
            text-transform: uppercase; letter-spacing: 1.5px; transition: all 0.3s ease;
        }
        button:hover { transform: scale(1.03) translateY(-3px); box-shadow: 0 15px 40px rgba(138, 28, 95, 0.5); }

        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
        .glass-box { background: rgba(255, 255, 255, 0.55); border-radius: 30px; padding: 35px; margin-bottom: 25px; border: 1px solid var(--glass-border); box-shadow: 0 8px 30px rgba(0,0,0,0.06); }

        .chart-container { display: flex; align-items: flex-end; height: 180px; gap: 15px; margin: 30px 0; padding-bottom: 15px; border-bottom: 3px solid rgba(138, 28, 95, 0.2); }
        .bar-col { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; }
        .bar { width: 100%; border-radius: 15px 15px 0 0; box-shadow: 0 -4px 15px rgba(0,0,0,0.1); transition: height 1.2s ease; position: relative;}
        .bar-red { background: linear-gradient(to top, #ef4444, #fca5a5); }
        .bar-purple { background: linear-gradient(to top, #9333ea, #d8b4fe); }
        .bar-yellow { background: linear-gradient(to top, #eab308, #fef08a); }
        .bar-peach { background: linear-gradient(to top, #f97316, #fdba74); }
        .bar-label { margin-top: 12px; font-weight: 800; font-size: 0.95rem; text-align: center; color: var(--deep-magenta); }

        .disclaimer { background: rgba(255, 255, 255, 0.7); border: 2px dashed var(--primary-pink); padding: 20px; border-radius: 25px; font-size: 0.95rem; color: #70114c; text-align: center; margin-top: 40px; font-weight: 800; }
        .alert-box { background: rgba(254, 226, 226, 0.9); border-left: 5px solid #ef4444; padding: 20px; border-radius: 15px; margin-top: 15px; font-size: 1.05rem; display: none; font-weight: 700; color: #7f1d1d; box-shadow: 0 5px 15px rgba(239, 68, 68, 0.15);}
    </style>
</head>
<body onload="initApp()">

    <!-- Audio Elements for Alarms -->
    <audio id="waterAlarmSound" src="https://assets.mixkit.co/sfx/preview/mixkit-software-interface-start-2574.mp3" preload="auto"></audio>
    <audio id="medAlarmSound" src="https://assets.mixkit.co/sfx/preview/mixkit-doorbell-single-press-333.mp3" preload="auto"></audio>

    <div class="animated-overlay"></div>
    <img src="https://cdn-icons-png.flaticon.com/512/3024/3024310.png" class="doodle doodle-pill">
    <img src="https://cdn-icons-png.flaticon.com/512/3075/3075908.png" class="doodle doodle-bow">
    <img id="growth-plant" class="doodle-plant" src="https://cdn-icons-png.flaticon.com/512/892/892926.png">

    <div class="calligraphy-title">Shealth+</div>
    <div style="text-align:center; font-weight:900; color:var(--deep-magenta); margin-bottom: 30px; font-size:1.3rem;" id="ist-clock">Loading Clock...</div>

    <!-- WINDOW 1 -->
    <div id="win-1" class="window-container active-window">
        <h3 style="text-align:center; font-size: 2.4rem; margin-top:0;">Endocrine Aesthetics & Clinical Nutrition</h3>
        <p style="text-align: center; line-height: 1.9; font-size: 1.25rem; font-weight: 600;">Welcome to the hyper-personalized, clinical-grade nutrition architecture.</p>
        <div class="grid-2" style="margin-top: 40px;">
            <div><img src="https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=600" style="width:100%; border-radius: 35px; border: 3px solid rgba(255,255,255,0.8); box-shadow: 0 10px 30px rgba(0,0,0,0.1);"></div>
            <div class="glass-box">
                <p style="font-weight:900; color:var(--deep-magenta); font-size:1.3rem; margin-top:0;">Why SHEALTH+ is different:</p>
                <ul style="line-height:2.2; font-weight:700; font-size: 1.1rem;">
                    <li>30-Day constantly rotating diet specific to your Indian State.</li>
                    <li>Clinical drug-nutrient interaction tracking.</li>
                    <li>Dynamic BMR & TDEE Calorie algorithms.</li>
                </ul>
            </div>
        </div>
        <button onclick="jumpTo(2)">Begin Clinical Intake</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ provides AI-assisted wellness data and is not a replacement for professional medical advisors or physicians.</div>
    </div>

    <!-- WINDOW 2 -->
    <div id="win-2" class="window-container">
        <h3 style="font-size: 2.2rem;">Patient Registration Portal</h3>
        <div class="grid-2">
            <div>
                <label style="font-weight: 800; font-size: 1.1rem; margin-left: 10px;">Full Name:</label> <input type="text" id="p_name">
                <label style="font-weight: 800; font-size: 1.1rem; margin-left: 10px;">Age:</label> <input type="number" id="p_age" value="25" oninput="calcBMI()">
            </div>
            <div>
                <label style="font-weight: 800; font-size: 1.1rem; margin-left: 10px;">Biological Gender:</label>
                <select id="p_gender" onchange="calcBMI()"><option>Female</option><option>Male</option></select>
                <label style="font-weight: 800; font-size: 1.1rem; margin-left: 10px;">Home State (Native Diet Alignment):</label>
                <select id="p_region">
                    <option value="Uttar Pradesh">Uttar Pradesh (UP)</option>
                    <option value="Punjab & Haryana">Punjab & Haryana</option>
                    <option value="Maharashtra">Maharashtra</option>
                    <option value="Gujarat">Gujarat</option>
                    <option value="Kerala">Kerala</option>
                    <option value="Tamil Nadu">Tamil Nadu</option>
                    <option value="West Bengal">West Bengal</option>
                    <option value="Rajasthan">Rajasthan</option>
                </select>
                <label style="font-weight: 800; font-size: 1.1rem; margin-left: 10px;">Dietary Preference:</label>
                <select id="p_pref"><option>Both (Veg & Non-Veg)</option><option>Pure Vegetarian</option><option>Non-Vegetarian Focus</option></select>
                <label style="font-weight: 800; font-size: 1.1rem; margin-left: 10px;">Target Goals:</label>
                <select id="p_target" onchange="calcBMI()"><option>Weight Loss (PCOS/Thyroid Safe)</option><option>Weight Gain / Muscle Synthesis</option><option>Diabetic / Hypertension Control</option></select>
            </div>
        </div>
        <button onclick="jumpTo(3)">Lock Profile</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ provides AI-assisted wellness data and is not a replacement for professional medical advisors or physicians.</div>
    </div>

    <!-- WINDOW 3 -->
    <div id="win-3" class="window-container">
        <h3 style="font-size: 2.2rem;">Biometrics & Pharmacological Matrix</h3>
        <div class="grid-2">
            <div><label style="font-weight: 800; font-size: 1.1rem; margin-left: 10px;">Weight (kg):</label> <input type="number" id="p_weight" value="65" oninput="calcBMI()"></div>
            <div><label style="font-weight: 800; font-size: 1.1rem; margin-left: 10px;">Height (cm):</label> <input type="number" id="p_height" value="160" oninput="calcBMI()"></div>
        </div>
        
        <div class="grid-2">
            <div class="glass-box" style="text-align:center;">
                <strong style="font-size: 1.2rem;">Calculated BMI: <span id="bmi_result" style="font-size:3.5rem; display:block; color:var(--deep-magenta);">--</span></strong>
            </div>
            <div class="glass-box" style="text-align:center;">
                <strong style="font-size: 1.2rem;">Daily Caloric Target: <span id="cal_target" style="font-size:3.5rem; display:block; color:var(--primary-pink); text-shadow: 1px 1px 0px rgba(0,0,0,0.1);">--</span></strong>
            </div>
        </div>

        <label style="font-weight: 800; font-size: 1.1rem; margin-left: 10px;">List current medications for Clinical Interaction Check:</label>
        <textarea id="p_meds" rows="2" placeholder="e.g., Metformin, Thyroxine, Iron..." oninput="checkMeds()"></textarea>
        <div id="med_alert" class="alert-box"></div>

        <button onclick="jumpTo(4)">Generate Master Plan</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ provides AI-assisted wellness data and is not a replacement for professional medical advisors or physicians.</div>
    </div>

    <!-- WINDOW 4 -->
    <div id="win-4" class="window-container">
        <h3 style="font-size: 2.2rem;">30-Day Precision Tracking</h3>
        <div class="glass-box" style="display:flex; justify-content:space-between; align-items:center;">
            <label style="font-weight:900; font-size: 1.2rem;">Slide Active Day (1-30):</label>
            <input type="range" id="day-slider" min="1" max="30" value="1" onchange="updateDashboardDay()" style="width:50%;">
            <span id="day-label" style="font-size:2.5rem; font-weight:900; color:var(--deep-magenta);">Day 1</span>
        </div>
        <div class="grid-2">
            <div class="glass-box">
                <h4 style="font-size: 1.5rem; border-bottom: 2px solid rgba(255,255,255,0.5); padding-bottom: 10px;">Culinary Protocol (<span id="dash_region"></span>)</h4>
                <p style="font-size: 1.1rem;"><strong>💧 AM Detox:</strong> <br><span id="diet_detox" style="color:var(--deep-magenta); font-weight:800;"></span></p>
                <p style="font-size: 1.1rem;"><strong>🍳 Breakfast:</strong> <br><span id="diet_bfast" style="color:var(--deep-magenta); font-weight:800;"></span></p>
                <p style="font-size: 1.1rem;"><strong>🍱 Lunch:</strong> <br><span id="diet_lunch" style="color:var(--deep-magenta); font-weight:800;"></span></p>
                <p style="font-size: 1.1rem;"><strong>🥗 Snack:</strong> <br><span id="diet_snack" style="color:var(--deep-magenta); font-weight:800;"></span></p>
                <p style="font-size: 1.1rem;"><strong>🌙 Dinner:</strong> <br><span id="diet_dinner" style="color:var(--deep-magenta); font-weight:800;"></span></p>
            </div>
            <div class="glass-box">
                <h4 style="font-size: 1.5rem; border-bottom: 2px solid rgba(255,255,255,0.5); padding-bottom: 10px;">Target Fitness</h4>
                <p style="font-size: 1.1rem;"><strong>Exercise Protocol:</strong><br><span id="fitness_plan" style="color:var(--deep-magenta); font-weight:800;"></span></p>
                <p style="font-size: 1.1rem;"><strong>Daily Yoga Asana:</strong><br><span id="yoga_plan" style="color:var(--deep-magenta); font-weight:800;"></span></p>
            </div>
        </div>
        <button onclick="jumpTo(5)">View Monthly Analytics</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ provides AI-assisted wellness data and is not a replacement for professional medical advisors or physicians.</div>
    </div>

    <!-- WINDOW 5 -->
    <div id="win-5" class="window-container">
        <h3 style="font-size: 2.2rem;">Enhanced Monthly Blues</h3>
        <div class="glass-box" style="padding: 40px;">
            <h4 style="text-align:center; font-size: 1.8rem; margin-top: 0;">Cycle Phase Metric Graph</h4>
            <div class="chart-container">
                <div class="bar-col"><div class="bar bar-red" style="height: 20%;"><div class="bar-value">1-5</div></div><div class="bar-label">Menstrual</div></div>
                <div class="bar-col"><div class="bar bar-peach" style="height: 40%;"><div class="bar-value">6-13</div></div><div class="bar-label">Follicular</div></div>
                <div class="bar-col"><div class="bar bar-yellow" style="height: 80%;"><div class="bar-value">14-16</div></div><div class="bar-label">Ovulation</div></div>
                <div class="bar-col"><div class="bar bar-purple" style="height: 60%;"><div class="bar-value">17-28</div></div><div class="bar-label">Luteal</div></div>
            </div>
        </div>
        <button onclick="jumpTo(6)">Open Daily Utilities</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ provides AI-assisted wellness data and is not a replacement for professional medical advisors or physicians.</div>
    </div>

    <!-- WINDOW 6 -->
    <div id="win-6" class="window-container">
        <h3 style="font-size: 2.2rem;">Daily Utilities & Interactive Alarms</h3>
        <div class="grid-2">
            <div class="glass-box">
                <h4 style="font-size: 1.5rem;">💧 Hydration Tracker</h4>
                <p style="font-size:2.8rem; font-weight:900; text-align:center; color: var(--deep-magenta); margin: 20px 0;" id="water_status">0 / 8 Glasses</p>
                <button onclick="logWater()" style="padding:12px 25px; font-size:1.1rem; width: 80%;">+ Log Glass</button>
                <div style="margin-top:30px; font-weight: 700; font-size: 1.05rem;">
                    <label style="display:block; margin-bottom: 15px;"><input type="checkbox" id="alarm_water" onchange="toggleWaterAlarm()" style="width:20px; height:20px; vertical-align: middle; margin-right: 10px;"> Play Sound for Water (Every 60m)</label>
                    <label style="display:block;"><input type="checkbox" id="alarm_med" onchange="toggleMedAlarm()" style="width:20px; height:20px; vertical-align: middle; margin-right: 10px;"> Play Sound for Meds (Every 4h)</label>
                </div>
            </div>
            <div class="glass-box">
                <h4 style="font-size: 1.5rem;">🔥 End of Day Checklist</h4>
                <label style="font-weight: 800; font-size: 1.1rem; margin-left: 10px;">Log EOD Weight (kg):</label>
                <input type="number" placeholder="Enter tonight's weight...">
                <button style="padding:12px 25px; font-size:1.1rem; width: 80%;">Save EOD Data</button>
            </div>
        </div>
        
        <!-- EXPLICIT FOUNDER CARD AS REQUESTED -->
        <div class="glass-box" style="background:linear-gradient(145deg, #F472B6, #8A1C5F); color:white; margin-top:40px; text-align: center; border: 2px solid rgba(255,255,255,0.6);">
            <p style="font-size:2rem; font-weight:900; margin-bottom:5px; color: white;">Maihwish Rizvi</p>
            <p style="font-size:1.4rem; font-weight:bold; margin-top: 0; color: rgba(255,255,255,0.9);">Registered Pharmacist</p>
        </div>

        <button onclick="jumpTo(1)">End Session</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ provides AI-assisted wellness data and is not a replacement for professional medical advisors or physicians.</div>
    </div>

    <script>
        let waterCount = 0;
        let waterInterval, medInterval;

        function initApp() { 
            setInterval(updateClock, 1000); 
            calcBMI();
            updateDashboardDay();
        }

        function jumpTo(winId) {
            document.querySelectorAll('.window-container').forEach(w => w.classList.remove('active-window'));
            document.getElementById('win-' + winId).classList.add('active-window');
            window.scrollTo({top: 0, behavior: 'smooth'});
        }

        function updateClock() {
            let now = new Date();
            let utc = now.getTime() + (now.getTimezoneOffset() * 60000);
            let istDate = new Date(utc + (3600000 * 5.5));
            document.getElementById('ist-clock').innerText = "Delhi IST: " + istDate.toLocaleDateString('en-IN', {weekday:'long', month:'long', day:'numeric', hour:'2-digit', minute:'2-digit'});
        }

        function calcBMI() {
            let w = parseFloat(document.getElementById('p_weight').value);
            let h = parseFloat(document.getElementById('p_height').value);
            let age = parseInt(document.getElementById('p_age').value);
            let gender = document.getElementById('p_gender').value;
            let target = document.getElementById('p_target').value;
            
            if(w && h) {
                let bmi = (w / Math.pow(h/100, 2));
                document.getElementById('bmi_result').innerText = bmi.toFixed(1);
                
                let bmr = (10 * w) + (6.25 * h) - (5 * age);
                bmr = (gender === "Male") ? bmr + 5 : bmr - 161;
                
                let tdee = bmr * 1.3;
                if(target.includes("Loss")) tdee -= 400; 
                if(target.includes("Gain")) tdee += 400; 
                
                document.getElementById('cal_target').innerText = Math.round(tdee) + " kcal";
            }
        }

        function checkMeds() {
            let meds = document.getElementById('p_meds').value.toLowerCase();
            let alertBox = document.getElementById('med_alert');
            let warnings = [];

            if (meds.includes("metformin")) warnings.push("<strong>Metformin:</strong> Long-term use may deplete Vitamin B12. AI will prioritize B12-rich foods in your diet.");
            if (meds.includes("thyrox") || meds.includes("synthroid")) warnings.push("<strong>Thyroid Meds:</strong> Ensure a 4-hour gap between your medication and calcium/iron rich meals.");
            if (meds.includes("iron")) warnings.push("<strong>Iron Supplements:</strong> Consume with Vitamin C (like Nimbu Pani) for better absorption. Avoid tea/coffee immediately after.");

            if (warnings.length > 0) {
                alertBox.style.display = "block";
                alertBox.innerHTML = "<strong>⚕️ Clinical Pharmacist Alert:</strong><br>" + warnings.join("<br><br>");
            } else {
                alertBox.style.display = "none";
            }
        }

        function updateDashboardDay() {
            let day = parseInt(document.getElementById('day-slider').value);
            document.getElementById('day-label').innerText = "Day " + day;
            document.getElementById('growth-plant').style.width = (50 + (day * 2)) + "px";

            let state = document.getElementById('p_region').value;
            let pref = document.getElementById('p_pref').value;
            document.getElementById('dash_region').innerText = state;

            let detox = ["Warm Lemon Honey Water", "Jeera Coriander Decoction", "Apple Cider Vinegar Shot", "Fennel Seed Infusion", "Mint Aloe Vera Flush", "Cinnamon Brew", "Fenugreek (Methi) Water", "Tulsi Ginger Drop"];
            
            let bf_veg = [], bf_nv = [], lunch_veg = [], lunch_nv = [];

            if (state === "Uttar Pradesh") {
                bf_veg = ["Sattu Paratha & Curd", "Dal Fara (Steamed)", "Besan Cheela", "Banarasi Chura Matar", "Dalia Porridge", "Matar Nimona Extract", "Methi Puri (Baked)"];
                bf_nv = ["Egg White Scramble", "Awadhi Minced Chicken Toast", "Masala Omelet Platter", "Boiled Eggs with Chaat Masala"];
                lunch_veg = ["Tehri (Mix Veg Rice)", "Dal Nimona + Roti", "Lauki Chana Dal", "Kala Chana Curry + Brown Rice", "Arhar Dal & Jeera Rice"];
                lunch_nv = ["Awadhi Chicken Stew + Roti", "Egg Curry + Brown Rice", "Chicken Reshmi Kebab + Salad", "Mutton Dalcha (Light Portion)"];
            } else if (state === "Punjab & Haryana") {
                bf_veg = ["Missi Roti with White Butter", "Paneer Bhurji", "Oats Kulcha", "Makki Di Roti (Portion controlled)"];
                bf_nv = ["Egg Bhurji with Roti", "Chicken Sausage", "Tandoori Omelet", "Keema Paratha (Light Oil)"];
                lunch_veg = ["Sarson Ka Saag + Less Ghee Roti", "Pindi Chole + Salad", "Rajma Chawal", "Kadhi Pakora (Air fried)"];
                lunch_nv = ["Tandoori Chicken + Mint Chutney", "Saag Gosht (Light)", "Chicken Tikka Masala + Roti", "Fish Amritsari (Baked)"];
            } else if (state === "Maharashtra") {
                bf_veg = ["Thalipeeth (Multigrain)", "Misal (Sprouts, no oil) + Pav", "Kanda Poha", "Upma with Veggies"];
                bf_nv = ["Anda Poha", "Boiled Eggs + Green Chutney", "Chicken Kheema Toast"];
                lunch_veg = ["Zunka Bhakri", "Varan Bhaat", "Bharli Vangi (Light oil) + Roti", "Usal + Salad"];
                lunch_nv = ["Malvani Chicken Curry", "Anda Curry + Roti", "Kolhapuri Chicken (Less Spice)", "Bombil (Baked)"];
            } else if (state === "Gujarat") {
                bf_veg = ["Methi Thepla + Curd", "Khaman Dhokla", "Handvo (Baked Lentil Cake)", "Fada Ni Khichdi"];
                bf_nv = ["Egg Ghotala", "Surti Egg Bhurji", "Masala Half Fry"];
                lunch_veg = ["Gujarati Dal + Brown Rice", "Undhiyu (Baked veggies)", "Sev Tameta (Less oil) + Bhakri", "Rotla & Garlic Chutney"];
                lunch_nv = ["Chicken Curry (Gujarati Style)", "Egg Masala", "Grilled Fish"];
            } else if (state === "Kerala") {
                bf_veg = ["Puttu with Steamed Kadala", "Appam & Veg Stew", "Idiyappam", "Oats Upma"];
                bf_nv = ["Malabar Egg Roast", "Kerala Chicken Stew", "Beef Roast (Lean/Light)", "Egg Appam"];
                lunch_veg = ["Avial + Red Rice", "Sambar + Brown Rice", "Olan & Kalan", "Vegetable Thoran"];
                lunch_nv = ["Meen Moilee (Fish Curry)", "Chicken Curry (Coconut base)", "Kerala Egg Curry", "Fish Pollichathu (Banana Leaf)"];
            } else if (state === "Tamil Nadu") {
                bf_veg = ["Ragi Idli with Sambar", "Pongal (Less Ghee)", "Kambu Koozh (Millet)", "Pesarattu"];
                bf_nv = ["Egg Podimas", "Chicken Dosa", "Omelet with Curry Leaves"];
                lunch_veg = ["Rasam & Poriyal + Rice", "Bisi Bele Bath", "Vatha Kuzhambu", "Lemon Rice"];
                lunch_nv = ["Chettinad Chicken (Light oil)", "Meen Kuzhambu", "Egg Pepper Fry", "Mutton Curry (Lean portion)"];
            } else if (state === "West Bengal") {
                bf_veg = ["Luchi & Chholar Dal (Air fried)", "Poha", "Chiror Pulao", "Dalia"];
                bf_nv = ["Dim Kosha (Egg)", "Chicken Kabiraji (Baked)", "Masala Omelet"];
                lunch_veg = ["Shukto + Rice", "Moong Dal & Begun Bhaja (Air fried)", "Aloo Posto", "Vegetable Chorchori"];
                lunch_nv = ["Machher Jhol (Fish Curry)", "Kosha Mangsho (Light)", "Chicken Dak Bungalow", "Doi Maach"];
            } else {
                bf_veg = ["Bajra Roti + Garlic Chutney", "Moong Dal Cheela", "Poha", "Dalia"];
                bf_nv = ["Egg Bhurji", "Masala Omelet", "Chicken Keema"];
                lunch_veg = ["Dal Baati (Baked)", "Gatte Ki Sabzi", "Ker Sangri", "Panchmel Dal"];
                lunch_nv = ["Laal Maas (Less oil/spice)", "Safed Maas", "Egg Curry", "Chicken Banjara"];
            }

            let final_bf = "", final_lunch = "";
            if (pref.includes("Veg") && !pref.includes("Both") && !pref.includes("Non")) {
                final_bf = bf_veg[(day - 1) % bf_veg.length];
                final_lunch = lunch_veg[(day - 1) % lunch_veg.length];
            } else if (pref.includes("Non")) {
                final_bf = bf_nv[(day - 1) % bf_nv.length];
                final_lunch = lunch_nv[(day - 1) % lunch_nv.length];
            } else {
                final_bf = (day % 2 === 0) ? bf_veg[(day - 1) % bf_veg.length] : bf_nv[(day - 1) % bf_nv.length];
                final_lunch = (day % 2 === 0) ? lunch_veg[(day - 1) % lunch_veg.length] : lunch_nv[(day - 1) % lunch_nv.length];
            }

            let snack = ["Roasted Makhanas", "Handful of Almonds & Walnuts", "Hummus with Cucumber", "Chia Seed Pudding", "Dark Chocolate (70%+)", "Roasted Chana", "Greek Yogurt", "Fruit Bowl (Apple/Papaya)"];
            let dinner = ["Light Clear Soup + Steamed Veggies", "Grilled Paneer/Tofu + Broccoli", "Bottle Gourd (Lauki) Sabzi + 1 Roti", "Moong Dal Sprouts Salad", "Cauliflower Rice + Tikka", "Vegetable Khichdi", "Pumpkin Soup"];

            let yoga = ["Baddha Konasana (Butterfly) - Improves Pelvic Flow", "Bhujangasana (Cobra) - Stretches Core", "Balasana (Child's Pose) - Relieves Stress", "Viparita Karani - Great for circulation", "Surya Namaskar - Full body metabolic boost", "Anulom Vilom - Nervous system balance", "Marjaryasana (Cat-Cow) - Spinal health"];
            let exercise = ["HIIT Cardio: 25 mins", "Bodyweight Squats & Core: 30 mins", "Brisk Walk + Resistance Bands", "Power Yoga Flow: 30 mins", "Upper Body Dumbbells: 20 mins", "Core & Pilates Stability", "Active Rest: 45 min Light Walk"];

            document.getElementById('diet_detox').innerText = detox[(day - 1) % detox.length];
            document.getElementById('diet_bfast').innerText = final_bf;
            document.getElementById('diet_lunch').innerText = final_lunch;
            document.getElementById('diet_snack').innerText = snack[(day - 1) % snack.length];
            document.getElementById('diet_dinner').innerText = dinner[(day - 1) % dinner.length];
            
            document.getElementById('yoga_plan').innerText = yoga[(day - 1) % yoga.length];
            document.getElementById('fitness_plan').innerText = exercise[(day - 1) % exercise.length];
        }

        function logWater() {
            if(waterCount < 8) waterCount++;
            document.getElementById('water_status').innerText = `${waterCount} / 8 Glasses`;
        }

        function toggleWaterAlarm() {
            let isChecked = document.getElementById('alarm_water').checked;
            let audio = document.getElementById('waterAlarmSound');
            if(isChecked) {
                waterInterval = setInterval(() => { audio.play(); alert("💧 Time to hydrate!"); }, 3600000); 
                alert("60-minute hydration alarm activated.");
            } else { clearInterval(waterInterval); }
        }

        function toggleMedAlarm() {
            let isChecked = document.getElementById('alarm_med').checked;
            let audio = document.getElementById('medAlarmSound');
            if(isChecked) {
                medInterval = setInterval(() => { audio.play(); alert("💊 Time for your prescribed medication."); }, 14400000); 
                alert("4-hour Medication timing sync activated.");
            } else { clearInterval(medInterval); }
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=1550, scrolling=True)
