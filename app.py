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

# 2. Use r""" (Raw String) to prevent any syntax errors with HTML characters
html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SHEALTH+ | Aesthetic Clinical Precision</title>
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display&family=Plus+Jakarta+Sans&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-pink: #F472B6;
            --deep-magenta: #8A1C5F; 
            --text-dark: #2D0A22; 
        }
        body { margin: 0; padding: 20px; font-family: 'Plus Jakarta Sans', sans-serif; background: #fce4ec; }
        .window-container { background: rgba(255,255,255,0.7); backdrop-filter: blur(20px); border-radius: 40px; padding: 40px; max-width: 900px; margin: auto; display: none; }
        .active-window { display: block; }
        button { background: linear-gradient(145deg, #F472B6, #8A1C5F); color: white; padding: 15px 30px; border-radius: 30px; border: none; font-weight: bold; cursor: pointer; }
        .glass-box { background: rgba(255,255,255,0.6); border-radius: 20px; padding: 20px; margin: 10px 0; }
    </style>
</head>
<body>
    <div id="win-1" class="window-container active-window">
        <h1 style="font-family:'Great Vibes'; font-size: 5rem; text-align: center; color: var(--deep-magenta);">Shealth+</h1>
        <p style="text-align: center; font-size: 1.2rem;">Endocrine Aesthetics & Clinical Nutrition</p>
        <button onclick="jumpTo(2)">Begin Clinical Intake</button>
        <div style="font-size: 0.8rem; text-align: center; margin-top: 20px; border: 1px dashed #B83280; padding: 10px;">
            ⚠️ Health Disclaimer: SHEALTH+ provides AI-assisted wellness data and is not a replacement for professional medical advisors.
        </div>
    </div>

    <div id="win-2" class="window-container">
        <h3>Patient Registration</h3>
        <input type="text" id="p_name" placeholder="Full Name">
        <select id="p_region">
            <option value="Uttar Pradesh">Uttar Pradesh</option>
            <option value="Punjab & Haryana">Punjab & Haryana</option>
        </select>
        <button onclick="jumpTo(3)">Lock Profile</button>
        <div style="font-size: 0.8rem; text-align: center; margin-top: 20px; border: 1px dashed #B83280; padding: 10px;">
            ⚠️ Health Disclaimer: SHEALTH+ provides AI-assisted wellness data and is not a replacement for professional medical advisors.
        </div>
    </div>

    <script>
        function jumpTo(winId) {
            document.querySelectorAll('.window-container').forEach(w => w.classList.remove('active-window'));
            document.getElementById('win-' + winId).classList.add('active-window');
        }
    </script>
</body>
</html>
"""

# Render
components.html(html_code, height=800, scrolling=True)
