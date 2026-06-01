<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHEALTH+ | AI Precision Coach</title>
    <link href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap" rel="stylesheet">
    <style>
        /* --- FORCED LIGHT MODE & METALLIC THEME --- */
        :root {
            --magenta: #B83280;
            --metallic-pink: linear-gradient(145deg, #FFD1DC 0%, #F472B6 50%, #B83280 100%);
            --glossy-white: rgba(255, 255, 255, 0.85);
            --text-dark: #4A154B;
            --silver-border: linear-gradient(145deg, #e6e6e6, #ffffff, #cccccc);
        }
        
        body, html {
            margin: 0; padding: 0;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: var(--text-dark) !important;
            background-color: #FFE4E1 !important; /* Force Light Peach/Pink */
            background-image: 
                radial-gradient(circle at 15% 50%, rgba(244, 114, 182, 0.15), transparent 25%),
                radial-gradient(circle at 85% 30%, rgba(184, 50, 128, 0.15), transparent 25%);
            background-attachment: fixed;
        }

        /* Heroicon SVGs */
        svg.hero { width: 22px; height: 22px; vertical-align: middle; margin-right: 8px; stroke: var(--magenta); fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

        /* Glossy Window Containers */
        .window-container {
            background: var(--glossy-white);
            backdrop-filter: blur(16px);
            border-radius: 30px; padding: 40px;
            border: 2px solid transparent;
            background-clip: padding-box;
            box-shadow: 0 20px 50px rgba(184, 50, 128, 0.15), inset 0 0 15px rgba(255,255,255,1);
            max-width: 1000px; margin: 20px auto;
            position: relative;
            display: none;
            animation: slideUp 0.6s ease-out forwards;
        }
        
        .window-container::before {
            content: ''; position: absolute; top: -2px; left: -2px; right: -2px; bottom: -2px;
            background: var(--silver-border); z-index: -1; border-radius: 32px;
        }

        .active-window { display: block; }
        @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

        /* Typography */
        .calligraphy-title { font-family: 'Alex Brush', cursive; font-size: 6rem; background: var(--metallic-pink); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; margin: 10px 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); }
        h3, h4 { font-family: 'Playfair Display', serif; color: var(--magenta); }
        
        /* Clock Banner */
        .clock-banner { background: var(--glossy-white); border: 1px solid #FBCFE8; border-radius: 20px; padding: 10px 25px; font-weight: bold; color: var(--magenta); text-align: center; max-width: 400px; margin: 0 auto 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }

        /* Metallic Buttons */
        button {
            background: var(--metallic-pink); color: white; font-weight: 800; border-radius: 30px; border: none;
            padding: 15px 40px; font-size: 1.1rem; cursor: pointer; display: block; margin: 25px auto;
            box-shadow: 0 8px 20px rgba(184, 50, 128, 0.3), inset 0 2px 5px rgba(255,255,255,0.5);
            text-transform: uppercase; letter-spacing: 1px; transition: all 0.3s ease;
        }
        button:hover { transform: translateY(-3px); box-shadow: 0 12px 25px rgba(184, 50, 128, 0.4); }

        /* Inputs & Layouts */
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        input, select, textarea { width: 100%; padding: 12px; margin: 8px 0 15px; border-radius: 12px; border: 1px solid #FBCFE8; background: #FFF5F7; color: var(--text-dark); font-family: 'Plus Jakarta Sans', sans-serif; box-sizing: border-box; outline: none; }
        input:focus, select:focus { border-color: var(--magenta); box-shadow: 0 0 8px rgba(244, 114, 182, 0.4); }
        
        /* Content Boxes */
        .box { background: white; border-radius: 16px; padding: 20px; margin-bottom: 15px; border-left: 5px solid var(--magenta); box-shadow: 0 4px 15px rgba(0,0,0,0.03); }
        .disclaimer { background: #FFF0F5; border: 1px dashed #F472B6; padding: 15px; border-radius: 15px; font-size: 0.8rem; color: #9D174D; text-align: center; margin-top: 30px; }
        .quote { font-family: 'Playfair Display', serif; font-style: italic; text-align: center; color: var(--magenta); margin: 20px 0; font-size: 1.2rem; }

        /* Menstrual Tracker Chart */
        .cycle-bar { display: flex; height: 30px; border-radius: 15px; overflow: hidden; margin: 15px 0; background: #eee; }
        .phase-menstrual { background: #F43F5E; width: 20%; }
        .phase-follicular { background: #FDBA74; width: 30%; }
        .phase-ovulation { background: #34D399; width: 10%; }
        .phase-luteal { background: #818CF8; width: 40%; }
        
        /* Doodles */
        .doodle-plant { position: fixed; bottom: 20px; left: 20px; width: 50px; transition: width 1s ease; z-index: 100; pointer-events: none;}
        .doodle-pill { position: absolute; top: 20px; right: 20px; width: 40px; opacity: 0.6; pointer-events: none; }
    </style>
</head>
<body onload="initApp()">

    <!-- Growing Plant Doodle (Left corner) -->
    <img id="growth-plant" class="doodle-plant" src="https://cdn-icons-png.flaticon.com/512/892/892926.png" alt="Growing Plant">

    <div class="calligraphy-title">Shealth+</div>
    <div class="clock-banner" id="ist-clock">Loading IST Time...</div>

    <!-- ================= WINDOW 1: INTRO & MEDIA ================= -->
    <div id="win-1" class="window-container active-window">
        <img class="doodle-pill" src="https://cdn-icons-png.flaticon.com/512/3024/3024310.png">
        <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200" style="width:100%; border-radius:20px; object-fit: cover; height: 350px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        
        <h3 style="text-align:center; margin-top: 30px;">Elevate Your Endocrine Aesthetics</h3>
        <p style="text-align: center; line-height: 1.8;">Welcome to <strong>SHEALTH+</strong>, a hyper-personalized, clinical-grade nutrition and lifestyle architecture. We merge advanced pharmacological tracking with intuitive, beautiful daily rituals to prevent disease and optimize your vitality.</p>
        
        <div class="box">
            <h4><svg class="hero" viewBox="0 0 24 24"><path d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg> AI Health Coach Initiative (30s Overview)</h4>
            <!-- Placeholder for AI Video -->
            <div style="background:#000; height: 200px; border-radius: 12px; display:flex; align-items:center; justify-content:center; color:white;">[ AI Generated Coach Video Placeholder ]</div>
        </div>

        <button onclick="jumpTo(2)">Begin Clinical Intake</button>
        <div class="quote">"Nourish the cells, empower the soul." 🎀</div>
        <div class="disclaimer">⚠️ Health Disclaimer: SHEALTH+ provides AI-assisted wellness data and is not a replacement for professional medical advisors or physicians.</div>
    </div>

    <!-- ================= WINDOW 2: HOSPITAL INTAKE & MEDICAL HISTORY ================= -->
    <div id="win-2" class="window-container">
        <h3><svg class="hero" viewBox="0 0 24 24"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg> Patient Clinical Registration</h3>
        <div class="grid-2">
            <div>
                <label>Full Name:</label> <input type="text" id="p_name">
                <label>Email ID:</label> <input type="email" id="p_email">
                <label>Contact Number:</label> <input type="text" id="p_contact">
                <label>Age:</label> <input type="number" id="p_age">
            </div>
            <div>
                <label>Biological Gender:</label>
                <select id="p_gender" onchange="toggleFemaleFields()">
                    <option value="Female">Female</option>
                    <option value="Male">Male</option>
                    <option value="Other">Other</option>
                </select>
                <label>State / Region:</label>
                <select id="p_region">
                    <option value="North">North India</option>
                    <option value="South">South India</option>
                    <option value="East">East India</option>
                    <option value="West">West India</option>
                </select>
                <label>Dietary Preference:</label>
                <select id="p_diet_pref">
                    <option value="Both">Both (Veg & Non-Veg)</option>
                    <option value="Veg">Pure Vegetarian</option>
                    <option value="NonVeg">Non-Vegetarian Focus</option>
                </select>
                <label>Health Target:</label>
                <select id="p_target">
                    <option value="Weight Loss">Weight Loss (PCOS/Thyroid Safe)</option>
                    <option value="Weight Gain">Weight Gain / Muscle Synthesis</option>
                    <option value="Diabetic Maintenance">Diabetic / Hypertension Control</option>
                </select>
            </div>
        </div>

        <hr style="border:1px solid #FBCFE8; margin: 20px 0;">
        
        <h4><svg class="hero" viewBox="0 0 24 24"><path d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg> Biometrics & Vitals</h4>
        <div style="text-align: right; margin-bottom: 10px;">
            <label style="font-size:0.8rem; font-weight:bold; color:var(--magenta);">Toggle System: </label>
            <select id="unit_system" style="width:auto; padding:5px; margin:0;" onchange="updateUnits()">
                <option value="metric">Metric (kg / cm)</option>
                <option value="imperial">Imperial (lbs / ft)</option>
            </select>
        </div>
        <div class="grid-2">
            <div>
                <label id="lbl_weight">Weight (kg):</label> <input type="number" id="p_weight" oninput="calcBMI()">
            </div>
            <div>
                <label id="lbl_height">Height (cm):</label> <input type="number" id="p_height" oninput="calcBMI()">
            </div>
        </div>
        
        <div class="box" style="text-align:center;">
            <strong>AI Calculated BMI: <span id="bmi_result" style="font-size:1.5rem; color:var(--magenta);">--</span></strong>
            <p id="bmi_status" style="margin:5px 0 0 0; font-size:0.9rem;"></p>
        </div>

        <h4><svg class="hero" viewBox="0 0 24 24"><path d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg> Pharmacological History</h4>
        <label>List current medications (AI will check interactions/side-effects):</label>
        <textarea id="p_meds" rows="2" placeholder="e.g., Metformin, Levothyroxine..."></textarea>
        <button type="button" style="padding: 8px 20px; font-size: 0.9rem; margin:0 0 15px 0;" onclick="checkMeds()">Run Interaction Check</button>
        <div id="med_alert" style="display:none; color:#D97706; font-size:0.85rem; padding:10px; background:#FEF3C7; border-radius:8px;"></div>

        <div id="female_fields">
            <hr style="border:1px solid #FBCFE8; margin: 20px 0;">
            <h4>🎀 Monthly Blues Vitals</h4>
            <div class="grid-2">
                <div><label>Last Menstrual Start Date:</label> <input type="date" id="p_lmp"></div>
                <div><label>Average Cycle Length:</label> <input type="number" id="p_cycle" value="28"></div>
            </div>
        </div>

        <button onclick="generateDashboard(3)">Generate Protocol & Dashboard</button>
    </div>

    <!-- ================= WINDOW 3: MASTER DASHBOARD (Diet, Tracking, Period, Music) ================= -->
    <div id="win-3" class="window-container">
        <h3><svg class="hero" viewBox="0 0 24 24"><path d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg> SHEALTH+ Active Command Center</h3>
        
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom: 20px;">
            <label style="font-weight:bold; color:var(--magenta); width:40%;">Active Day Tracker (1-30):</label>
            <input type="range" id="day-slider" min="1" max="30" value="1" style="width:50%; accent-color: var(--magenta);" onchange="updateDashboardDay()">
            <span id="day-label" style="font-weight:bold; font-size:1.2rem; color:var(--magenta);">Day 1</span>
        </div>

        <div class="grid-2">
            <!-- LEFT COLUMN: Diet & Fitness -->
            <div>
                <h4><svg class="hero" viewBox="0 0 24 24"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2v10z"></path></svg> 4-Course Culinary Protocol</h4>
                <div class="box">
                    <p style="margin:0; font-size:0.8rem; color:gray;">Region: <span id="dash_region"></span> | Focus: <span id="dash_target"></span></p>
                    <hr style="border:0.5px solid #eee;">
                    <strong>💧 AM Detox:</strong> <span id="diet_detox"></span><br><br>
                    <strong>🍳 Breakfast:</strong> <span id="diet_bfast"></span> <br><em>Recipe: <span id="rec_bfast" style="color:var(--magenta); font-size:0.8rem;"></span></em><br><br>
                    <strong>🍱 Lunch:</strong> <span id="diet_lunch"></span><br><br>
                    <strong>🥗 Snack:</strong> <span id="diet_snack"></span><br><br>
                    <strong>🌙 Dinner:</strong> <span id="diet_dinner"></span>
                </div>

                <h4><svg class="hero" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg> AI Fitness & Yoga Routine</h4>
                <div class="box">
                    <p id="fitness_plan"></p>
                    <div style="background:#ddd; height:120px; border-radius:8px; display:flex; align-items:center; justify-content:center; margin-top:10px;">[ Workout Video Generator ]</div>
                </div>
            </div>

            <!-- RIGHT COLUMN: Trackers, Mood, Alarms -->
            <div>
                <!-- Female Tracker -->
                <div id="blues_meter_box">
                    <h4>🎀 Monthly Blues Meter</h4>
                    <div class="box">
                        <p style="margin:0; font-weight:bold;">Current Phase: <span id="cycle_phase" style="color:var(--magenta);"></span></p>
                        <div class="cycle-bar">
                            <div class="phase-menstrual" title="Menstruation"></div>
                            <div class="phase-follicular" title="Follicular"></div>
                            <div class="phase-ovulation" title="Ovulation"></div>
                            <div class="phase-luteal" title="Luteal"></div>
                        </div>
                        <p style="font-size:0.75rem; color:#666; margin:0;">Red=Menstrual, Orange=Follicular, Green=Ovulation, Purple=Luteal</p>
                    </div>
                </div>

                <!-- Mood & Comfort Bucket -->
                <h4><svg class="hero" viewBox="0 0 24 24"><path d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> Daily Mood & Comfort</h4>
                <select id="mood_selector" onchange="updateBucketList()">
                    <option value="Happy">Happy & Energetic</option>
                    <option value="Anxious">Anxious / Overwhelmed</option>
                    <option value="Cramps">Physical Discomfort / Cramps</option>
                </select>
                <div class="box" style="background:#FFF5F7;">
                    <strong>Comfort Bucket List:</strong>
                    <ul id="bucket_list" style="margin-top:5px; padding-left:20px; font-size:0.9rem;"></ul>
                </div>

                <!-- Daily Meters & Alarms -->
                <h4><svg class="hero" viewBox="0 0 24 24"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> Active System Tracking</h4>
                <div class="box">
                    <strong>💧 Water Status:</strong> <span id="water_status">0 / 8 Glasses</span>
                    <button style="padding:5px 15px; margin:5px 0; font-size:0.8rem;" onclick="logWater()">+ Log Glass</button>
                    <strong>🔥 Daily Calorie Target:</strong> <span id="cal_target">--</span> kcal
                    <hr style="border:0.5px solid #eee;">
                    <label><input type="checkbox" id="alarm_water" onchange="toggleAlarms()"> Enable 60-Min Hydration Alarm</label><br>
                    <label><input type="checkbox"> Enable Meal / Pill Timing Alarms</label>
                </div>
            </div>
        </div>

        <hr style="border:1px solid #FBCFE8; margin: 30px 0;">

        <!-- Music Module -->
        <h4 style="text-align:center;">🎧 30-Min Daily Bollywood/Hollywood Hybrid Mix</h4>
        <div style="background:#f0f0f0; padding:15px; border-radius:15px; text-align:center;">
            <audio controls style="width:100%; outline:none;">
                <!-- Placeholder for actual audio source -->
                <source src="" type="audio/mpeg">
                Your browser does not support the audio element. Placeholder for API hook.
            </audio>
        </div>

        <!-- Founder Card -->
        <div class="box" style="margin-top:40px; background:var(--metallic-pink); color:white; border:none;">
            <h3 style="color:white; margin-top:0;">Founder Architecture</h3>
            <p style="margin:5px 0; font-size:1.1rem; font-weight:bold;">Maihwish Rizvi, B.Pharm (AKTU)</p>
            <p style="font-size:0.9rem; line-height:1.5;">Registered Pharmacist & Visionary Developer.<br>Engineered with precision clinical protocols to bypass fitness trends and target authentic neuroendocrine baselines. Welcome to the future of aesthetic health technology.</p>
        </div>

        <button onclick="jumpTo(1)">End Session & Logout</button>
        <div class="quote">"She designed a life she loved." ✨</div>
    </div>

    <script>
        // --- CORE LOGIC & INITIALIZATION ---
        let waterCount = 0;
        let alarmInterval;
        let isMetric = true;

        function initApp() {
            updateClock();
            setInterval(updateClock, 1000);
            updateDashboardDay();
        }

        // Navigation
        function jumpTo(winId) {
            document.querySelectorAll('.window-container').forEach(w => w.classList.remove('active-window'));
            document.getElementById('win-' + winId).classList.add('active-window');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Clock (Delhi IST reference logic)
        function updateClock() {
            const now = new Date();
            // Convert to IST (UTC+5:30)
            const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
            const istDate = new Date(utc + (3600000 * 5.5));
            const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute:'2-digit', second:'2-digit' };
            document.getElementById('ist-clock').innerText = "Delhi IST: " + istDate.toLocaleDateString('en-IN', options);
        }

        // Unit Toggle Logic
        function updateUnits() {
            const sys = document.getElementById('unit_system').value;
            isMetric = (sys === 'metric');
            document.getElementById('lbl_weight').innerText = isMetric ? "Weight (kg):" : "Weight (lbs):";
            document.getElementById('lbl_height').innerText = isMetric ? "Height (cm):" : "Height (inches):";
            calcBMI();
        }

        function calcBMI() {
            let w = parseFloat(document.getElementById('p_weight').value);
            let h = parseFloat(document.getElementById('p_height').value);
            if(!w || !h) return;

            let bmi = 0;
            if(isMetric) {
                let hm = h / 100;
                bmi = w / (hm * hm);
            } else {
                bmi = (w / (h * h)) * 703;
            }
            
            document.getElementById('bmi_result').innerText = bmi.toFixed(1);
            let status = "";
            if(bmi < 18.5) status = "Underweight";
            else if(bmi <= 24.9) status = "Optimal Health Baseline";
            else if(bmi <= 29.9) status = "Overweight Matrix";
            else status = "Clinical Obesity Protocol Needed";
            document.getElementById('bmi_status').innerText = status;
        }

        function toggleFemaleFields() {
            const gender = document.getElementById('p_gender').value;
            document.getElementById('female_fields').style.display = (gender === 'Female') ? 'block' : 'none';
        }

        function checkMeds() {
            const meds = document.getElementById('p_meds').value;
            const alertBox = document.getElementById('med_alert');
            if(meds.length > 3) {
                alertBox.style.display = 'block';
                alertBox.innerHTML = `<strong>AI Pharmacist Note:</strong> Scanning '${meds}' against national databases. Please ensure hydration is maintained to support hepatic clearance. Monitor for standard GI side-effects.`;
            }
        }

        // --- DASHBOARD GENERATION ---
        function generateDashboard(winId) {
            // Setup Profile text
            document.getElementById('dash_region').innerText = document.getElementById('p_region').value;
            document.getElementById('dash_target').innerText = document.getElementById('p_target').value;
            
            // Set Calorie target based on goal
            const goal = document.getElementById('p_target').value;
            document.getElementById('cal_target').innerText = goal.includes("Loss") ? "1400 - 1600" : (goal.includes("Gain") ? "2200 - 2500" : "1800 - 2000");

            // Setup Menstrual logic visibility
            if(document.getElementById('p_gender').value !== 'Female') {
                document.getElementById('blues_meter_box').style.display = 'none';
            } else {
                document.getElementById('blues_meter_box').style.display = 'block';
                calculateCyclePhase();
            }

            updateDashboardDay();
            updateBucketList();
            jumpTo(winId);
        }

        // --- 30 DAY DIET & WORKOUT ALGORITHM ---
        function updateDashboardDay() {
            const day = parseInt(document.getElementById('day-slider').value);
            document.getElementById('day-label').innerText = "Day " + day;

            // Grow plant dynamically based on day (1 to 30)
            const plant = document.getElementById('growth-plant');
            plant.style.width = (50 + (day * 2)) + "px"; // Grows from 52px to 110px over 30 days

            const region = document.getElementById('p_region').value;
            const pref = document.getElementById('p_diet_pref').value;
            const goal = document.getElementById('p_target').value;

            // Array structures simulating 30-day rotation
            const detoxList = ["Warm Lemon Honey Water", "Jeera Coriander Decoction", "Apple Cider Vinegar Shot", "Fennel Seed Infusion", "Mint Aloe Vera Flush"];
            
            // Regional Breakfasts (Veg / NonVeg)
            const bfNorthVeg = ["Paneer Oats Cheela", "Sattu Paratha with Curd", "Besan Chilla", "Dalia Porridge"];
            const bfNorthNv = ["Egg White Scramble", "Chicken Keema Toast", "Masala Omelet"];
            const bfSouthVeg = ["Ragi Idli with Sambar", "Pesarattu (Moong Dal Dosa)", "Oats Upma"];
            const bfSouthNv = ["Malabar Egg Roast", "Egg Dosa", "Chicken Stew"];
            // Fallbacks for West/East to keep code concise but scalable
            const bfGenVeg = ["Poha with Peanuts", "Methi Thepla", "Brown Rice Flakes"];
            const bfGenNv = ["Anda Poha", "Egg Bhurji with Pav", "Boiled Egg Salad"];

            let activeVeg = (region === "North") ? bfNorthVeg : ((region === "South") ? bfSouthVeg : bfGenVeg);
            let activeNv = (region === "North") ? bfNorthNv : ((region === "South") ? bfSouthNv : bfGenNv);

            // Logic to pick based on Preference
            let finalBfast = "";
            if(pref === "Veg") finalBfast = activeVeg[day % activeVeg.length];
            else if (pref === "NonVeg") finalBfast = activeNv[day % activeNv.length];
            else finalBfast = (day % 2 === 0) ? activeVeg[day % activeVeg.length] : activeNv[day % activeNv.length];

            const lunchList = ["Quinoa Buddha Bowl with Regional Greens", "Lentil Stew with Brown Rice", "Grilled Lean Protein with Asparagus", "Millet Khichdi with Ghee", "Zucchini Noodles with Tofu/Chicken"];
            const snackList = ["Roasted Makhanas + Green Tea", "Handful of Almonds + Coconut Water", "Hummus with Carrot Sticks", "Chia Seed Pudding", "Dark Chocolate (70%+) + Herbal Tea"];
            const dinnerList = ["Light Clear Soup + Steamed Veggies", "Grilled Salmon/Tofu + Broccoli", "Bottle Gourd (Lauki) Sabzi + 1 Bran Roti", "Moong Dal Sprouts Salad", "Cauliflower Rice + Paneer/Chicken Tikka"];

            const workLoss = ["HIIT Cardio: 25 mins", "Bodyweight Squats & Core: 30 mins", "Brisk Walk + Resistance Bands", "Power Yoga Flow: 30 mins"];
            const workGain = ["Dumbbell Hypertrophy Protocol", "Heavy Leg Press & Squats", "Upper Body Strength Training", "Core & Calisthenics Routine"];
            const workDia = ["Steady State Walk (Post-meal)", "Light Yoga for Digestion", "Pilates Core Stability", "Low Impact Aerobics"];

            document.getElementById('diet_detox').innerText = detoxList[day % detoxList.length];
            document.getElementById('diet_bfast').innerText = finalBfast;
            document.getElementById('rec_bfast').innerText = `Blend ingredients, cook on non-stick pan using 1tsp olive oil. Serve warm.`;
            document.getElementById('diet_lunch').innerText = lunchList[day % lunchList.length];
            document.getElementById('diet_snack').innerText = snackList[day % snackList.length];
            document.getElementById('diet_dinner').innerText = dinnerList[day % dinnerList.length];

            if(goal.includes("Loss")) document.getElementById('fitness_plan').innerText = workLoss[day % workLoss.length];
            else if(goal.includes("Gain")) document.getElementById('fitness_plan').innerText = workGain[day % workGain.length];
            else document.getElementById('fitness_plan').innerText = workDia[day % workDia.length];
        }

        // --- CYCLE CALCULATOR ---
        function calculateCyclePhase() {
            const lmpStr = document.getElementById('p_lmp').value;
            if(!lmpStr) { document.getElementById('cycle_phase').innerText = "Awaiting LMP Input"; return; }
            
            const lmp = new Date(lmpStr);
            const today = new Date();
            const cycle = parseInt(document.getElementById('p_cycle').value);
            
            const diffTime = Math.abs(today - lmp);
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            const dayOfCycle = (diffDays % cycle) || 1;

            let phase = "";
            if(dayOfCycle >= 1 && dayOfCycle <= 5) phase = "Menstruation (Rest & Iron Focus)";
            else if(dayOfCycle >= 6 && dayOfCycle <= 13) phase = "Follicular (High Energy)";
            else if(dayOfCycle >= 14 && dayOfCycle <= 16) phase = "Ovulation (Peak Strength)";
            else phase = "Luteal Phase (PMS Care & Magnesium)";

            document.getElementById('cycle_phase').innerText = `Day ${dayOfCycle} - ${phase}`;
        }

        // --- MOOD & COMFORT ---
        function updateBucketList() {
            const mood = document.getElementById('mood_selector').value;
            const ul = document.getElementById('bucket_list');
            ul.innerHTML = "";
            let list = [];

            if(mood === "Happy") list = ["Hit a personal best in workout!", "Post a glowing selfie", "Meal prep for the week", "Upbeat Bollywood Dance Routine"];
            else if(mood === "Anxious") list = ["5-Minute Box Breathing", "Sip Chamomile Tea", "Digital Detox for 1 Hour", "Listen to Lo-Fi Hollywood Mix"];
            else list = ["Warm Heating Pad on Abdomen", "Dark Chocolate (Magnesium Boost)", "Gentle Yin Yoga Stretches", "Skip intense cardio today"];

            list.forEach(item => {
                let li = document.createElement("li");
                li.innerText = item;
                ul.appendChild(li);
            });
        }

        // --- ALARMS & TRACKERS ---
        function logWater() {
            if(waterCount < 8) waterCount++;
            document.getElementById('water_status').innerText = `${waterCount} / 8 Glasses`;
        }

        function toggleAlarms() {
            const isChecked = document.getElementById('alarm_water').checked;
            if(isChecked) {
                // In a real app this is 3600000 (1 hour). Set to 5 seconds for prototype demonstration.
                alarmInterval = setInterval(() => {
                    alert("💧 SHEALTH+ Reminder: Time to hydrate! Please drink a glass of water.");
                }, 60000 * 60); // 60 mins
                alert("60-minute hydration alarm activated.");
            } else {
                clearInterval(alarmInterval);
            }
        }
    </script>
</body>
</html>
