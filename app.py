import streamlit as st
import streamlit.components.v1 as components

# 1. Setup Streamlit Page (Wide mode to fit the design)
st.set_page_config(page_title="SHEALTH+ | Aesthetic Clinical Precision", layout="wide", initial_sidebar_state="collapsed")

# 2. Hide Streamlit's default ugly margins and headers
st.markdown("""
    <style>
        .block-container { padding: 0rem !important; max-width: 100% !important; }
        header { display: none !important; }
        footer { display: none !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Embed our ultra-aesthetic Glassmorphism HTML code
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
            --deep-magenta: #B83280;
            --pastel-purple: #E9D5FF;
            --text-dark: #4A154B;
            --glass-bg: rgba(255, 255, 255, 0.35);
            --glass-border: rgba(255, 255, 255, 0.6);
            --glass-shadow: 0 15px 35px 0 rgba(184, 50, 128, 0.2);
            --input-glass: rgba(255, 255, 255, 0.5);
        }
        
        body, html {
            margin: 0; padding: 0;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: var(--text-dark) !important;
            min-height: 100vh;
            background-color: #fce4ec;
            background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            overflow-x: hidden;
        }

        .animated-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(45deg, rgba(244,114,182,0.1), rgba(233,213,255,0.1), rgba(255,218,185,0.1));
            background-size: 300% 300%;
            animation: pulseBg 12s ease infinite;
            pointer-events: none; z-index: -1;
        }
        @keyframes pulseBg { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }

        .calligraphy-title { 
            font-family: 'Great Vibes', cursive; 
            font-size: 7.5rem; 
            text-align: center; 
            margin: 10px 0; 
            background: linear-gradient(to right, #B83280, #F472B6, #ffb6c1, #B83280);
            background-size: 200% auto;
            color: transparent;
            -webkit-background-clip: text;
            background-clip: text;
            animation: shine 4s linear infinite;
            filter: drop-shadow(2px 4px 6px rgba(255,255,255,0.6));
        }
        @keyframes shine { to { background-position: 200% center; } }

        .doodle { position: fixed; pointer-events: none; opacity: 0.75; z-index: -1; }
        .doodle-bow { top: 5%; right: 10%; width: 70px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.15)); }
        .doodle-pill { bottom: 15%; left: 6%; width: 60px; transform: rotate(-20deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.15)); }
        .doodle-plant { position: fixed; bottom: 15px; right: 25px; width: 55px; transition: width 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); z-index: 100; pointer-events: none; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.2)); }

        .window-container {
            background: var(--glass-bg);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border: 1px solid var(--glass-border);
            border-radius: 40px; 
            padding: 50px;
            box-shadow: var(--glass-shadow), inset 0 0 20px rgba(255,255,255,0.5);
            max-width: 1000px; margin: 30px auto 60px;
            position: relative;
            display: none;
            animation: floatUp 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        .active-window { display: block; }
        @keyframes floatUp { from { opacity: 0; transform: translateY(40px) scale(0.98); } to { opacity: 1; transform: translateY(0) scale(1); } }

        h3, h4 { font-family: 'Playfair Display', serif; color: var(--deep-magenta); }
        .quote { font-family: 'Playfair Display', serif; font-style: italic; text-align: center; color: var(--deep-magenta); margin: 30px 0 20px; font-size: 1.4rem; }

        input, select, textarea { 
            width: 100%; padding: 16px 25px; margin: 10px 0 25px; 
            border-radius: 35px; 
            border: 1px solid rgba(255, 255, 255, 0.9); 
            background: var(--input-glass); 
            backdrop-filter: blur(12px);
            color: var(--text-dark); 
            font-family: 'Plus Jakarta Sans', sans-serif; 
            font-size: 1.05rem;
            font-weight: 600;
            box-sizing: border-box; outline: none; 
            box-shadow: inset 0 4px 6px rgba(0,0,0,0.03);
            transition: all 0.3s ease;
        }
        input:focus, select:focus, textarea:focus { 
            border-color: var(--deep-magenta); background: rgba(255, 255, 255, 0.9);
            box-shadow: 0 0 20px rgba(244, 114, 182, 0.4); 
        }

        button {
            background: linear-gradient(145deg, #F472B6, #B83280);
            color: white; font-weight: 800; border-radius: 40px; border: none;
            padding: 18px 50px; font-size: 1.2rem; cursor: pointer; display: block; margin: 30px auto;
            box-shadow: 0 12px 30px rgba(184, 50, 128, 0.5), inset 0 3px 6px rgba(255,255,255,0.4);
            text-transform: uppercase; letter-spacing: 1.5px; transition: all 0.3s ease;
        }
        button:hover { transform: scale(1.05) translateY(-4px); box-shadow: 0 15px 40px rgba(184, 50, 128, 0.6); }

        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
        .glass-box { 
            background: rgba(255, 255, 255, 0.65); border-radius: 30px; padding: 30px; 
            margin-bottom: 25px; border: 1px solid rgba(255,255,255,0.9); 
            box-shadow: 0 8px 25px rgba(0,0,0,0.05); 
        }

        details.faq-glass {
            background: rgba(255,255,255,0.5); border-radius: 25px; padding: 18px 25px;
            margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.8);
            cursor: pointer; transition: all 0.3s ease;
        }
        details.faq-glass[open] { background: rgba(255,255,255,0.9); box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
        summary { font-weight: 800; color: var(--deep-magenta); font-size: 1.15rem; outline: none; }
        
        .chart-container { display: flex; align-items: flex-end; height: 180px; gap: 15px; margin: 30px 0; padding-bottom: 15px; border-bottom: 3px solid rgba(184,50,128,0.2); }
        .bar-col { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; }
        .bar { width: 100%; border-radius: 15px 15px 0 0; box-shadow: 0 -4px 15px rgba(0,0,0,0.1); transition: height 1.2s ease; position: relative;}
        
        .bar-red { background: linear-gradient(to top, #ef4444, #fca5a5); }
        .bar-purple { background: linear-gradient(to top, #9333ea, #d8b4fe); }
        .bar-yellow { background: linear-gradient(to top, #eab308, #fef08a); }
        .bar-peach { background: linear-gradient(to top, #f97316, #fdba74); }
        
        .bar-label { margin-top: 12px; font-weight: 800; font-size: 0.9rem; text-align: center; color: var(--deep-magenta); }
        .bar-value { position: absolute; top: -30px; width: 100%; text-align: center; font-weight: 900; color: var(--text-dark); font-size: 1.1rem; }

        .disclaimer { 
            background: rgba(255, 255, 255, 0.8); 
            border: 2px dashed var(--primary-pink); 
            padding: 20px; 
            border-radius: 25px; 
            font-size: 0.9rem; 
            color: #9D174D; 
            text-align: center; 
            margin-top: 40px; 
            font-weight: 800; 
        }
        
        svg.hero { width: 28px; height: 28px; vertical-align: middle; margin-right: 10px; stroke: var(--deep-magenta); fill: none; stroke-width: 2.5; }
    </style>
</head>
<body onload="initApp()">

    <div class="animated-overlay"></div>
    <img src="https://cdn-icons-png.flaticon.com/512/3024/3024310.png" class="doodle doodle-pill">
    <img src="https://cdn-icons-png.flaticon.com/512/3075/3075908.png" class="doodle doodle-bow">
    <img id="growth-plant" class="doodle-plant" src="https://cdn-icons-png.flaticon.com/512/892/892926.png">

    <div class="calligraphy-title">Shealth+</div>
    <div style="text-align:center; font-weight:900; color:var(--deep-magenta); margin-bottom: 25px; font-size:1.2rem;" id="ist-clock">Loading Clock...</div>

    <div id="win-1" class="window-container active-window">
        <h3 style="text-align:center; font-size: 2.2rem; margin-top:0;">Endocrine Aesthetics & Clinical Nutrition</h3>
        <div class="grid-2" style="margin-top: 40px;">
            <div>
                <img src="https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=600" style="width:100%; border-radius: 35px; margin-bottom: 20px; border: 2px solid white;">
            </div>
            <div>
                <details class="faq-glass"><summary>What is Endocrine Pacing?</summary><p>Balancing complex carbs throughout the day to prevent insulin spikes.</p></details>
                <details class="faq-glass"><summary>Why Regional Palates?</summary><p>Your gut microbiome digests local, culturally familiar spices more efficiently.</p></details>
            </div>
        </div>
        <button onclick="jumpTo(2)">Begin Clinical Intake</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ is not a replacement for professional medical advisors.</div>
    </div>

    <div id="win-2" class="window-container">
        <h3>Patient Registration Portal</h3>
        <div class="grid-2">
            <div>
                <label>Full Name:</label> <input type="text" id="p_name">
                <label>Age:</label> <input type="number" id="p_age">
            </div>
            <div>
                <label>Biological Gender:</label>
                <select id="p_gender"><option>Female</option><option>Male</option></select>
                <label>Region:</label>
                <select id="p_region"><option>North India</option><option>South India</option><option>East India</option><option>West India</option></select>
                <label>Target:</label>
                <select id="p_target"><option>Weight Loss</option><option>Weight Gain</option></select>
            </div>
        </div>
        <button onclick="jumpTo(3)">Lock Profile</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ is not a replacement for professional medical advisors.</div>
    </div>

    <div id="win-3" class="window-container">
        <h3>Biometrics & History</h3>
        <div class="grid-2">
            <div><label>Weight (kg):</label> <input type="number" id="p_weight" oninput="calcBMI()"></div>
            <div><label>Height (cm):</label> <input type="number" id="p_height" oninput="calcBMI()"></div>
        </div>
        <div class="glass-box" style="text-align:center;">
            <strong>AI Calculated BMI: <span id="bmi_result" style="font-size:3rem; display:block;">--</span></strong>
        </div>
        <button onclick="jumpTo(4)">Generate Plan</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ is not a replacement for professional medical advisors.</div>
    </div>

    <div id="win-4" class="window-container">
        <h3>30-Day Precision Tracking</h3>
        <div class="glass-box" style="display:flex; justify-content:space-between;">
            <label>Slide Active Day (1-30):</label>
            <input type="range" id="day-slider" min="1" max="30" value="1" onchange="updateDashboardDay()" style="width:50%;">
            <span id="day-label" style="font-size:2rem; font-weight:bold; color:var(--deep-magenta);">Day 1</span>
        </div>
        <div class="grid-2">
            <div class="glass-box">
                <h4>Culinary Protocol</h4>
                <strong>Breakfast:</strong> <span id="diet_bfast">Paneer Oats Cheela</span><br><br>
                <strong>Lunch:</strong> <span id="diet_lunch">Quinoa Bowl</span>
            </div>
            <div class="glass-box">
                <h4>Target Fitness</h4>
                <strong>Yoga:</strong> <span id="yoga_plan">Baddha Konasana</span>
            </div>
        </div>
        <button onclick="jumpTo(5)">View Monthly Analytics</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ is not a replacement for professional medical advisors.</div>
    </div>

    <div id="win-5" class="window-container">
        <h3>Enhanced Monthly Blues</h3>
        <div class="glass-box">
            <h4 style="text-align:center;">Cycle Phase Metric Graph</h4>
            <div class="chart-container">
                <div class="bar-col"><div class="bar bar-red" style="height: 20%;"><div class="bar-value">1-5</div></div><div class="bar-label">Menstrual</div></div>
                <div class="bar-col"><div class="bar bar-peach" style="height: 40%;"><div class="bar-value">6-13</div></div><div class="bar-label">Follicular</div></div>
                <div class="bar-col"><div class="bar bar-yellow" style="height: 80%;"><div class="bar-value">14-16</div></div><div class="bar-label">Ovulation</div></div>
                <div class="bar-col"><div class="bar bar-purple" style="height: 60%;"><div class="bar-value">17-28</div></div><div class="bar-label">Luteal</div></div>
            </div>
        </div>
        <button onclick="jumpTo(6)">Open Daily Utilities</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ is not a replacement for professional medical advisors.</div>
    </div>

    <div id="win-6" class="window-container">
        <h3>Daily Utilities & Alarms</h3>
        <div class="grid-2">
            <div class="glass-box">
                <h4>💧 Hydration Tracker</h4>
                <p style="font-size:2rem; font-weight:bold; text-align:center;" id="water_status">0 / 8 Glasses</p>
                <button onclick="logWater()" style="padding:10px 20px; font-size:1rem;">+ Log Glass</button>
            </div>
        </div>
        
        <div class="glass-box" style="background:linear-gradient(145deg, #F472B6, #B83280); color:white; margin-top:40px;">
            <h3 style="color:white; margin-top:0;">Clinical Architecture</h3>
            <p style="font-size:1.6rem; font-weight:900; margin-bottom:0;">Maihwish Rizvi</p>
            <p style="font-size:1.2rem; font-weight:bold;">Registered Pharmacist</p>
            <p>Engineered with precision clinical protocols to bypass fitness trends and target authentic neuroendocrine baselines.</p>
        </div>
        <button onclick="jumpTo(1)">End Session</button>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ is not a replacement for professional medical advisors.</div>
    </div>

    <script>
        let waterCount = 0;
        function initApp() { setInterval(updateClock, 1000); }
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
            if(w && h) document.getElementById('bmi_result').innerText = (w / Math.pow(h/100, 2)).toFixed(1);
        }
        function updateDashboardDay() {
            let day = document.getElementById('day-slider').value;
            document.getElementById('day-label').innerText = "Day " + day;
            document.getElementById('growth-plant').style.width = (50 + (day * 2)) + "px";
        }
        function logWater() {
            if(waterCount < 8) waterCount++;
            document.getElementById('water_status').innerText = `${waterCount} / 8 Glasses`;
        }
    </script>
</body>
</html>
"""

# 4. Render the HTML using Streamlit Components
components.html(html_code, height=1400, scrolling=True)
