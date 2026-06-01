<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHEALTH | AI Precision Coach</title>
    <link href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap" rel="stylesheet">
    <style>
        :root {
            --crimson: #7F1D1D;
            --light-pink: #FEF2F2;
            --border-pink: #FCA5A5;
            --text-dark: #451A1A;
        }
        
        body, html {
            margin: 0; padding: 0;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: var(--text-dark) !important;
            background-image: linear-gradient(to bottom, rgba(254, 242, 242, 0.88), rgba(252, 228, 228, 0.92)), 
                              url('https://images.unsplash.com/photo-1557672172-298e090bd0f1?w=1600');
            background-size: cover; background-position: center; background-attachment: fixed;
        }

        .window-container {
            background-color: rgba(255, 255, 255, 0.74);
            backdrop-filter: blur(22px) saturate(140%);
            border-radius: 30px; padding: 40px;
            border: 1px solid rgba(254, 202, 202, 0.6);
            box-shadow: 0 22px 50px rgba(185, 28, 28, 0.12);
            max-width: 1100px; margin: 20px auto 40px auto;
            animation: fadeIn 0.5s ease-in-out;
            display: none;
        }

        .active-window { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        .logo-container { text-align: center; margin-bottom: 2px; padding-top: 15px; }
        .calligraphy-title { font-family: 'Alex Brush', cursive; font-size: 5.6rem; color: var(--crimson); font-weight: 600; line-height: 0.9; }
        .brand-subtitle { font-size: 0.95rem; font-weight: 700; text-align: center; text-transform: uppercase; letter-spacing: 5px; color: #991B1B; margin-bottom: 20px;}

        button {
            background: linear-gradient(135deg, #F87171 0%, #991B1B 100%);
            color: white; font-weight: 700; border-radius: 30px; border: none;
            padding: 12px 35px; font-size: 0.95rem; cursor: pointer;
            display: block; margin: 20px auto; transition: transform 0.2s;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        button:hover { transform: scale(1.03); }

        .disclaimer {
            background-color: #FFF1F2; border: 1px solid #FDA4AF; padding: 12px;
            border-radius: 15px; margin-top: 25px; font-size: 0.75rem; color: #991B1B; text-align: center;
        }

        .meal-box { background-color: rgba(255, 255, 255, 0.92); border-radius: 16px; padding: 20px; margin-bottom: 15px; border-left: 5px solid #F87171; box-shadow: 0 4px 15px rgba(153, 27, 27, 0.03);}
        .info-box { background-color: #FEF2F2; color: #991B1B; padding: 15px; border-radius: 10px; border: 1px dashed #FCA5A5; font-weight: bold; margin-bottom: 15px;}
        
        input, select, textarea {
            width: 100%; padding: 12px; margin: 8px 0 15px 0;
            border-radius: 8px; border: 1px solid var(--border-pink);
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: white; color: var(--text-dark);
            box-sizing: border-box;
        }
        
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        h3, h4 { font-family: 'Playfair Display', serif; color: var(--crimson); }
        .quote { background: linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%); border: 1px dashed #FDA4AF; border-radius: 16px; padding: 15px; text-align: center; margin-top: 35px; font-style: italic;}
        
        svg.hero { width:24px; height:24px; vertical-align: middle; margin-right: 8px; stroke: var(--crimson); fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
    </style>
</head>
<body>

    <div class='logo-container'>
        <svg width="90" height="90" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="44" fill="white" fill-opacity="0.85"/>
            <circle cx="50" cy="50" r="41" stroke="#F472B6" stroke-width="1.5" stroke-dasharray="4 4"/>
            <path d="M50 32C42 22 28 26 28 42C28 58 45 70 50 74C55 70 72 58 72 42C72 26 58 22 50 32Z" stroke="#F472B6" stroke-width="3"/>
            <circle cx="50" cy="40" r="8" stroke="#DB2777" stroke-width="3" fill="none"/>
            <line x1="50" y1="48" x2="50" y2="65" stroke="#DB2777" stroke-width="3"/>
            <line x1="42" y1="56" x2="58" y2="56" stroke="#DB2777" stroke-width="3"/>
        </svg>
        <div class='calligraphy-title'>Shealth</div>
        <p class='brand-subtitle'>AI Precision Endocrine Alignment</p>
    </div>

    <div id="win-1" class="window-container active-window">
        <img src="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=1200" style="width:100%; border-radius:20px; object-fit: cover; height: 300px;">
        <h3 style="text-align:center;">Welcome to your Precision Metabolic Environment</h3>
        <p style="text-align: center; font-size:1.05rem; line-height:1.7; max-width:850px; margin: 0 auto;">
            <strong>SHEALTH</strong> is an advanced, high-tech AI-driven nutrient and diet coach wellness architecture engineered to resolve root endocrine variables. By compiling baseline biological signatures, the ecosystem structures completely custom, daily-differentiated therapeutic regimes.
        </p>
        <button onclick="jumpTo(2)">Initialize Profile ➔</button>
        <div class="quote">'Invest in your health, it pays the best biological interest.' — Stay Radiant</div>
        <div class="disclaimer"><svg class="hero" viewBox="0 0 24 24"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg> Medical Disclaimer: This application provides AI-driven wellness suggestions and is for informational purposes only.</div>
    </div>

    <div id="win-2" class="window-container">
        <h3><svg class="hero" viewBox="0 0 24 24"><path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg> Clinical Profile Registration Portal</h3>
        <div class="grid-2">
            <div>
                <label>Patient Full Name String:</label>
                <input type="text" id="p_name" value="Riya Sharma">
                
                <label>Geographic Coordinate Base (City/State):</label>
                <input type="text" id="p_loc" value="Lucknow, Uttar Pradesh">
                
                <label>Select Your Native Culinary Region:</label>
                <select id="p_region">
                    <option value="North">North India (Punjab/Haryana/UP)</option>
                    <option value="West">West India (Gujarat/Maharashtra/Rajasthan)</option>
                    <option value="South">South India (Kerala/Tamil Nadu/Karnataka)</option>
                    <option value="East">East India (Bengal/Odisha/Bihar)</option>
                </select>
            </div>
            <div>
                <label>Biological Age Value:</label>
                <input type="number" id="p_age" value="24">
                
                <label>Core Mass Weight Field (kg):</label>
                <input type="number" id="p_weight" value="68">
                
                <label>Core Axis Height Field (cm):</label>
                <input type="number" id="p_height" value="162">
            </div>
        </div>
        <hr style="border-color: #FCA5A5;">
        <div class="grid-2">
            <div>
                <label>Approximate date of last 'Monthly Reds':</label>
                <input type="date" id="p_reds">
            </div>
            <div>
                <label>Average Cycle Length (Days):</label>
                <input type="number" id="p_cycle" value="28">
            </div>
        </div>
        <label>Log active clinical prescriptions or metabolic history markers:</label>
        <textarea id="p_history" rows="3">None</textarea>
        <button onclick="saveProfileAndJump(3)">Lock Profile ➔</button>
        <div class="quote">'Self-care is a non-negotiable prescription. Your recovery journey initializes now.'</div>
        <div class="disclaimer">⚠️ Medical Disclaimer: Not a substitute for professional medical advice.</div>
    </div>

    <div id="win-3" class="window-container">
        <h3><svg class="hero" viewBox="0 0 24 24"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"></path></svg> AI Symptom Stratification & Vector Intake Matrix</h3>
        <div style="line-height: 2;">
            <label><input type="checkbox" id="s1"> 1. Sudden weight shifts or high resistance to metabolic calorie deficits?</label><br>
            <label><input type="checkbox" id="s2"> 2. Deep muscular exhaustion, systemic fatigue, or morning sluggishness profiles?</label><br>
            <label><input type="checkbox" id="s3"> 3. Active hair volume reductions, facial flareups, or cystic flare clusters?</label><br>
            <label><input type="checkbox" id="s4"> 4. Missing menstrual cycle parameters or deeply delayed hormonal schedules?</label><br>
            <label><input type="checkbox" id="s5"> 5. Chronic internal room temperature sensitivities (feeling cold or unprovoked flushes)?</label><br>
            <label><input type="checkbox" id="s6"> 6. Rapid mood shifts, nervous energy, or unexplained anxiety vectors?</label><br>
            <label><input type="checkbox" id="s7"> 7. Intense late-night processing cravings for sweet or high-sodium foods?</label><br>
            <label><input type="checkbox" id="s10"> 8. Diagnosed insulin processing disruptions or parental diabetic history records?</label><br>
        </div>
        <button onclick="calculateSymptoms(4)">Process Vectors ➔</button>
        <div class="quote">'Listening to your body's subtle bio-signals is the highest form of self-love.'</div>
        <div class="disclaimer">⚠️ Medical Disclaimer: Not a substitute for professional medical advice.</div>
    </div>

    <div id="win-4" class="window-container">
        <h3><svg class="hero" viewBox="0 0 24 24"><path d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg> Physical Biometrics Converter & AI Diagnostic Engine</h3>
        
        <div class="grid-2" style="margin-top:30px;">
            <div>
                <p style="color:var(--crimson); font-weight:bold; margin-bottom:5px;">Calculated Body Mass Index (BMI)</p>
                <h1 id="bmi-display" style="color:var(--crimson); font-size:4.5rem; margin:0; font-family: 'Playfair Display', serif;">25.9</h1>
            </div>
            <div style="display:flex; align-items:center;">
                <div id="bmi-status" class="info-box" style="width:100%; text-align:center;">Status Placeholder</div>
            </div>
        </div>

        <h4 style="margin-top: 40px;"><svg class="hero" viewBox="0 0 24 24"><path d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"></path></svg> SHEALTH AI Real-time Intelligent Coaching Core</h4>
        <div id="ai-insight" class="info-box">AI Insight Placeholder</div>
        
        <label style="margin-top: 20px; display:block;">Configure Targeted 30-Day Target Pathway Matrix:</label>
        <select id="target_goal">
            <option>Weight Loss Deficit Track</option>
            <option>Weight Gain Surplus Track</option>
        </select>
        <button onclick="generatePlan(5)">Compile Schedule ➔</button>
        <div class="quote">'Vitals are just coordinate data markers; consistency is where transformation lives.'</div>
        <div class="disclaimer">⚠️ Medical Disclaimer: Not a substitute for professional medical advice.</div>
    </div>

    <div id="win-5" class="window-container">
        <h3><svg class="hero" viewBox="0 0 24 24"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg> SHEALTH AI 30-Day Precision Challenge Tracker</h3>
        
        <div class="info-box" id="diet-context" style="text-align:center; font-size: 1.1rem;"></div>

        <div style="display:flex; flex-direction:column; align-items:center; margin: 30px 0;">
            <label style="font-weight:bold; color:var(--crimson);">Select Active Tracking Day (1 to 30):</label>
            <input type="range" id="day-slider" min="1" max="30" value="1" style="width:80%; accent-color: var(--crimson);" onchange="updateDietPlan()">
            <h2 id="day-label" style="color:var(--crimson); font-family: 'Playfair Display', serif; margin:10px 0;">Day 1 Logs</h2>
        </div>
        
        <div class="meal-box">
            <strong>🥤 Step 1: Morning Detox Elixir</strong>
            <p id="diet-detox" style="margin-top:5px;"></p>
        </div>
        <div class="meal-box">
            <strong>🍳 Course 1: Breakfast Target</strong>
            <p id="diet-breakfast" style="margin-top:5px;"></p>
        </div>
        <div class="meal-box">
            <strong>🥗 Course 3: Evening Adrenal Vitality Snack</strong>
            <p id="diet-snack" style="margin-top:5px;"></p>
        </div>
        <div class="meal-box">
            <strong>🌙 Course 4: Restorative Night Repair Dinner</strong>
            <p id="diet-dinner" style="margin-top:5px;"></p>
        </div>
        <div class="meal-box" style="border-left-color: #3B82F6;">
            <strong>🏋️‍♀️ Step 4: Customized Exercise Blueprint</strong>
            <p id="diet-workout" style="margin-top:5px;"></p>
        </div>

        <button onclick="jumpTo(6)">Compliance Center ➔</button>
        <div class="quote">'Eat to nourish your system cell-by-cell. You are entirely worth the commitment.'</div>
        <div class="disclaimer">⚠️ Medical Disclaimer: Not a substitute for professional medical advice.</div>
    </div>

    <div id="win-6" class="window-container">
        <h3><svg class="hero" viewBox="0 0 24 24"><path d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg> Real-time Adherence Dashboards</h3>
        
        <div class="grid-2">
            <div>
                <h4><svg class="hero" viewBox="0 0 24 24"><path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg> Private Dynamic 'Monthly Reds' Forecast</h4>
                <div style="background-color:#FFF5F5; padding:20px; border-radius:15px; border-left:5px solid #DC2626;">
                    <p style="margin:0; font-weight:700; color:#991B1B; font-size:1.1rem;">Estimated Next Secure Window Arrival</p>
                    <p id="reds-countdown" style="font-size:2rem; font-weight:800; color:#7F1D1D; margin:10px 0;">-- Days Remaining</p>
                    <p id="reds-advice" style="font-size:0.9rem; color:#451A1A; margin:0;">AI Tracker Advice: Loading...</p>
                </div>
            </div>
            <div>
                <h4><svg class="hero" viewBox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg> Satellite Healthcare Provider Locator</h4>
                <div class="info-box" style="font-weight: normal;">
                    Verified within <strong id="provider-loc">Location</strong> Perimeter Networks
                </div>
                <div class="meal-box" style="border-left-color: #991B1B;">
                    <strong>Apollo Diagnostic Healthcare Center & Endocrine Hub</strong><br>
                    Specialized Clinical Testing Wing Active
                </div>
            </div>
        </div>

        <hr style="border-color: #FCA5A5; margin: 30px 0;">
        
        <div style="background: linear-gradient(135deg, rgba(254, 242, 242, 0.9) 0%, rgba(254, 226, 226, 0.9) 100%); padding: 30px; border-radius: 20px; border: 1px solid #FCA5A5;">
            <h3 style="margin-top:0;"><svg class="hero" viewBox="0 0 24 24"><path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg> Clinical Product System Architecture</h3>
            <h4 style="color: #991B1B; margin-top:5px; font-weight:600;">Maihwish Rizvi Bpharm aktu | Registered Pharmacist</h4>
            <p style="line-height:1.6; font-size:0.95rem;">
                As a <strong>Registered Pharmacist</strong>, my formal clinical evaluation training allows me to design user-friendly wellness products that bypass superficial fitness trends to target actual baseline neuroendocrine mechanisms. By pairing 30-day dynamic life-science calibrations with a rich, comforting <strong>Indian culinary palate</strong>, SHEALTH presents a high-tech healthcare platform engineered for rigorous daily patient safety and compliance tracking protocols.
            </p>
            <p style="font-size:0.85rem; color:#991B1B; margin-bottom:0;" id="founder-patient-info"></p>
        </div>

        <button onclick="jumpTo(1)">⟲ Reset Session</button>
        <div class="quote">'Small daily adjustments build ultimate physiological resilience. Keep glowing!'</div>
        <div class="disclaimer">⚠️ Medical Disclaimer: Not a substitute for professional medical advice.</div>
    </div>

    <script>
        // State Object
        const state = {
            name: "Riya Sharma",
            weight: 68,
            height: 162,
            region: "North",
            cycle: 28,
            redsLast: new Date(),
            surveyScore: "General Wellness Track",
            goal: "Weight Loss Deficit Track",
            bmi: 0,
            history: "None"
        };

        // Navigation
        function jumpTo(windowId) {
            document.querySelectorAll('.window-container').forEach(el => el.classList.remove('active-window'));
            document.getElementById('win-' + windowId).classList.add('active-window');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Save Profile & Jump
        function saveProfileAndJump(windowId) {
            state.name = document.getElementById('p_name').value || state.name;
            state.weight = parseFloat(document.getElementById('p_weight').value) || state.weight;
            state.height = parseFloat(document.getElementById('p_height').value) || state.height;
            state.region = document.getElementById('p_region').value;
            state.cycle = parseInt(document.getElementById('p_cycle').value) || state.cycle;
            state.history = document.getElementById('p_history').value || "None";
            
            let redDate = document.getElementById('p_reds').value;
            if(redDate) state.redsLast = new Date(redDate);
            
            // Set Founder card info early
            document.getElementById('founder-patient-info').innerHTML = `<strong>Active Session:</strong> Patient: ${state.name} • Diagnostics Log: ${state.history}`;

            jumpTo(windowId);
        }

        // Calculate Symptoms & BMI
        function calculateSymptoms(windowId) {
            let p_calc = 0; let t_calc = 0;
            if(document.getElementById('s1').checked) { p_calc++; t_calc++; }
            if(document.getElementById('s2').checked) t_calc++;
            if(document.getElementById('s3').checked) p_calc++;
            if(document.getElementById('s4').checked) p_calc++;
            if(document.getElementById('s5').checked) t_calc++;
            if(document.getElementById('s6').checked) { p_calc++; t_calc++; }
            if(document.getElementById('s7').checked) p_calc++;
            if(document.getElementById('s10').checked) p_calc++;

            if (p_calc === 0 && t_calc === 0) state.surveyScore = "General Wellness Track";
            else if (p_calc >= t_calc) state.surveyScore = "PCOS Modification Matrix";
            else state.surveyScore = "Hypothyroidism Protocol Hub";

            let hm = state.height / 100;
            state.bmi = (state.weight / (hm * hm)).toFixed(1);
            document.getElementById('bmi-display').innerText = state.bmi;
            
            let status = "";
            if(state.bmi < 18.5) status = "Underweight Baseline";
            else if(state.bmi <= 24.9) status = "Optimal Homeostasis";
            else if(state.bmi <= 29.9) status = "Overweight Matrix Burden";
            else status = "Obese Clinical Stress";
            
            document.getElementById('bmi-status').innerText = "System Matrix Node Status: " + status;

            let ai_text = "";
            if(state.surveyScore.includes("PCOS")) {
                ai_text = `Warning: Insulin sensitivity margins are compressed. Prior logs: '${state.history}'. Recommendation: Implement clean complex carbohydrates safely.`;
            } else if (state.surveyScore.includes("Hypothyroidism")) {
                ai_text = `Detected reduced energetic output axes matching a thyroid cellular lag. Prior logs: '${state.history}'. Recommendation: Focus on natural Selenium.`;
            } else {
                ai_text = `System coordinates verified within homeostatic ranges. Operational tier: '${status}'. Maintenance enabled.`;
            }
            document.getElementById('ai-insight').innerText = "✨ AI Engine Response: " + ai_text;

            jumpTo(windowId);
        }

        function generatePlan(windowId) {
            state.goal = document.getElementById('target_goal').value;
            updateDietPlan();
            jumpTo(windowId);
        }

        // FULL 60-ITEM DIET ARRAYS & LOGIC
        function updateDietPlan() {
            let day = parseInt(document.getElementById('day-slider').value);
            document.getElementById('day-label').innerText = "Day " + day + " Logs";
            document.getElementById('diet-context').innerText = `Active Plan: ${state.surveyScore} | Goal: ${state.goal} | Region: ${state.region}`;

            let vegB = [], nVegB = [], dinV = [], dinNv = [];

            if (state.region === "North") {
                vegB = ["Paneer Oats Cheela", "Kashmiri Noon Chai with Almond Girda", "Sattu Porridge with Jaggery", "Sattu Stuffed Kachori", "Sidu with Lentil Mash", "Whole Wheat Dalia", "Chana Dal Steamed Fara", "Besan Onion Cheela", "Singhara Flour Crepe"];
                nVegB = ["Egg White Scramble Spinach Wrap", "Kashmiri Poached Eggs in Light Tomato Broth", "Mughlai Minced Chicken Toast", "Pahadi Herb Baked Omelet", "UP Style Masala Omelet Platter", "Kumaoni Herb Fried Eggs", "Haryanvi Ghee Egg White Scramble"];
                dinV = ["Lauki Soup + 1 Bran Roti", "Moong Dal Khichdi", "Palak Paneer (Light) + Roti", "Tofu Matar Sabzi", "Chana Dal Fara", "Roasted Makhana Bowl"];
                dinNv = ["Grilled Chicken Tikka + Salad", "Egg Curry + Roti", "Chicken Clear Soup", "Tandoori Fish + Broccoli", "Egg Stew", "Baked Fish"];
            } else if (state.region === "West") {
                vegB = ["Methi Thepla with Curd", "Bajra Raab with Roasted Nuts", "Moong Dal Sprouts Chat", "Thalipeeth with Low Fat Butter", "Steamed Jowar Flakes", "Sprouted Chana Salad", "Roasted Makhana Porridge", "Buckwheat Khichdi"];
                nVegB = ["Egg Poha Infused with Turmeric", "Goan Egg Cafe-real Wrap", "Maharashtrian Anda Poha Plates", "Bhopali Minced Egg Toast", "Chhattisgarhi Egg Fara"];
                dinV = ["Gujarati Kadhi + Brown Rice", "Varan Bhaat (Less Ghee)", "Bajra Roti + Baingan Bharta", "Usal + Salad", "Millet Flour Dumplings", "Soft Tofu Hash"];
                dinNv = ["Fish Koliwada (Baked) + Salad", "Chicken Sukka (Dry) + Jowar Roti", "Egg Stew", "Goan Fish Curry (Light)", "Chicken Clear Soup", "Egg Pepper Fry"];
            } else if (state.region === "South") {
                vegB = ["Puttu with Steamed Kadala", "Ragi Idli with Tomato Chutney", "Foxtail Millet Upma", "Pesarattu Mint Toast", "Akki Roti with Dill Leaves", "Finger Millet Gruel", "Malabar Neem Leaf Infusion Pancakes"];
                nVegB = ["Malabar Egg Roast with Whole Wheat Appam", "Tamil Nadu Egg Podimas with Curry Leaves", "Hyderabadi Chicken Keema Pattern Roll", "Andhra Spicy Egg White Omelet", "Mangalorean Egg Ghee Roast Whites", "Malabar Boiled Egg Podi Wrap"];
                dinV = ["Bisi Bele Bath (Millet)", "Rasam + Brown Rice", "Vegetable Stew", "Avial + Red Rice", "Steamed Broccoli + Paneer", "Bottle Gourd Soup"];
                dinNv = ["Chettinad Chicken (Less Oil) + Salad", "Meen Curry (Fish) + Red Rice", "Pepper Chicken Dry", "Egg Pepper Fry", "Seared Salmon", "Grilled Chicken Salad"];
            } else { // East
                vegB = ["Brown Rice Flakes Poha", "Chhena Poda Slice", "Boiled Sweet Potatoes with Black Salt", "Bamboo Shoot Rice Cakes", "Sticky Rice Mash", "Millet Flour Dumplings"];
                nVegB = ["Assamese Egg Bor with Green Herbs", "Bengali Dim Bhurji with Mustard Hints", "Odisha Egg Masala Mash", "Bihari Egg Bhujia with Roasted Gram", "Naga Style Smoked Chicken Shreds", "Khasi Egg Veg Scramble", "Mizo Egg Stew Bowls", "Tripuri Boiled Egg Salad", "Sikkim Chicken Momos (Steamed)", "Jharkhand Desi Chicken Shreds", "Manipuri Fish Pepper Mash", "Arunachal Steamed Herbs Egg"];
                dinV = ["Dalma (Lentil Veggie Mash)", "Shukto + Brown Rice", "Alo Bhaja (Air Fried) + Roti", "Mushroom Tarkari", "Soft Tofu Hash", "Moong Dal Khichdi"];
                dinNv = ["Machher Jhol (Light Fish Curry)", "Chicken Dak Bungalow", "Egg Curry (Dim Kosha)", "Steamed Fish (Bhaapa Maach)", "Egg White Stew", "Baked Fish"];
            }

            let detox = ["Spearmint Herbal Flush", "Jeera Coriander Decoction", "Aloe Vera Ginger Shot", "Fennel Cleanse", "Mint Buttermilk", "Warm Lemon Water"];
            let snacks = ["Ayurvedic Kadha + Roasted Makhanas", "Warm Turmeric Milk + 4 Almonds", "Green Tea + Roasted Chana", "Mint Buttermilk + Flax Seeds", "Coconut Water + Chia Seeds", "Apple Slices + Peanut Butter"];
            let workLoss = ["Low-Cortisol Bodyweight Squats: 3x15 reps + 20 min walk", "Wall Pushups: 3x12 reps + 15 min stepping", "Incline Slow Treadmill: 25 mins", "Tricep Chair Dips: 3x10 reps + 20 min stroll"];
            let workGain = ["Floor Glute Bridges: 4x12 reps", "Chair Assisted Squats: 3x10 reps", "Plank Alignment Core: 4x45s holds", "Dumbbell Overhead Presses: 3x12 reps"];

            // Hashing logic
            document.getElementById('diet-detox').innerHTML = `Warmed <strong>${detox[day % detox.length]}</strong> administered empty-stomach.`;
            document.getElementById('diet-breakfast').innerHTML = `Veg: ${vegB[day % vegB.length]} <br>Non-Veg: ${nVegB[day % nVegB.length]}`;
            document.getElementById('diet-snack').innerHTML = snacks[day % snacks.length];
            document.getElementById('diet-dinner').innerHTML = `Veg: ${dinV[day % dinV.length]} <br>Non-Veg: ${dinNv[day % dinNv.length]}`;
            
            if(state.goal.includes("Loss")) {
                document.getElementById('diet-workout').innerText = workLoss[day % workLoss.length];
            } else {
                document.getElementById('diet-workout').innerText = workGain[day % workGain.length];
            }

            // Update Dashboards in Window 6
            let today = new Date();
            let diffTime = today - state.redsLast;
            let diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
            
            let daysUntil = 0;
            if (diffDays < 0) {
                daysUntil = Math.abs(diffDays) % state.cycle;
            } else {
                daysUntil = state.cycle - (diffDays % state.cycle);
                if (daysUntil === state.cycle) daysUntil = 0;
            }
            if(isNaN(daysUntil)) daysUntil = "--";

            document.getElementById('reds-countdown').innerText = daysUntil + " Days Remaining";
            let advice = (daysUntil <= 7) ? "Prioritize cellular recovery and include roasted makhana to balance micro-cravings safely." : "Energy parameters are stable. Optimal window to execute Alternate Squat progressions.";
            document.getElementById('reds-advice').innerText = "AI Tracker Advice: " + advice;
            document.getElementById('provider-loc').innerText = document.getElementById('p_loc').value || "Your City";
        }

        // Initialize today's date in Window 2
        window.onload = function() {
            document.getElementById('p_reds').valueAsDate = new Date(new Date().setDate(new Date().getDate() - 14));
        };
    </script>
</body>
</html>
