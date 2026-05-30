import streamlit as st
import pandas as pd
import datetime

# --- 1. CORE SYSTEM INITIALIZATION ---
st.set_page_config(page_title="SHEALTH | AI Precision Coach", page_icon="🩸", layout="wide")

# --- 2. LAVENDER-CRIMSON AESTHETIC STYLE SHEET ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&family=Playfair+Display&family=Plus+Jakarta+Sans&display=swap');
    
    .stApp {
        background-image: linear-gradient(to bottom, rgba(254, 242, 242, 0.88), rgba(245, 243, 255, 0.92)), 
                          url('https://images.unsplash.com/photo-1557672172-298e090bd0f1?w=1600');
        background-size: cover; background-attachment: fixed;
    }
    
    /* Layered Doodles: Pills, Fruits, and Lavender Sticker Accents */
    .stApp::before {
        content: ""; position: fixed; top: 5%; left: 2%; width: 120px; height: 120px;
        background-image: url('https://img.icons8.com/external-icongeek26-outline-icongeek26/100/991B1B/external-pills-medical-icongeek26-outline-icongeek26.png');
        opacity: 0.12; pointer-events: none;
    }
    .stApp::after {
        content: ""; position: fixed; bottom: 5%; right: 2%; width: 100px; height: 100px;
        background-image: url('https://img.icons8.com/ios/100/7E22CE/lavender.png');
        opacity: 0.15; pointer-events: none;
    }
    
    .window-container { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(15px); border-radius: 30px; padding: 40px; border: 1px solid rgba(254, 202, 202, 0.5); }
    
    /* Cozy List Styles */
    .pamper-box { background: #F5F3FF; padding: 20px; border-radius: 20px; border-left: 5px solid #7E22CE; margin-top: 15px; }
    
    /* Buttons */
    div.stButton > button { background: linear-gradient(135deg, #F87171 0%, #991B1B 100%); color: white; border-radius: 25px; border: none; padding: 10px 25px; }
    </style>
""", unsafe_allow_html=True)

# [LOGO, TIME, AND STATE CORES REMAIN THE SAME - RE-PASTE LOGIC HERE]

# ==========================================
# WINDOW 6: COMPLIANCE & PAMPER KIT
# ==========================================
elif st.session_state.active_window == 6:
    st.markdown("<div class='window-container'>", unsafe_allow_html=True)
    st.markdown("<h3>🚨 Adherence & Comfort Hub</h3>", unsafe_allow_html=True)
    
    hud1, hud2 = st.columns(2)
    with hud1:
        # FEMALE PROFILE COZY PAMPER KIT
        if st.session_state.p_gender == "Female Profile":
            st.markdown("<h4 style='color:#7E22CE;'>🌸 The 'Cozy Reds' Pamper Kit</h4>", unsafe_allow_html=True)
            st.markdown("""
            <div class='pamper-box'>
                <p><strong>✨ For the 'Moody' Days (Indian Style):</strong></p>
                <ul>
                    <li><strong>Dark Chocolate therapy:</strong> For those 'Chup-chap rehne ka mann' vibes.</li>
                    <li><strong>Sanitary Essentials:</strong> Keeping it 'Safe-side' with top-tier comfort pads.</li>
                    <li><strong>Hot Water Bottle:</strong> 'Pet-dard ka asli sukoon'.</li>
                    <li><strong>Herbal Kadha:</strong> 'Mummy ke nuskhon wala magic'.</li>
                    <li><strong>Comfy Socks:</strong> 'Pyaar aur warmth ka dose'.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # [REMAINING ALARM AND TRACKER LOGIC...]
