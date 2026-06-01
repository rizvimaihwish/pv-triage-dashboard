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

        /* --- FLOATING DOODLES --- */
        .doodle { position: fixed; pointer-events: none; opacity: 0.65; z-index: -1; }
        .doodle-bow { top: 5%; right: 10%; width: 70px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.15)); animation: float1 6s ease-in-out infinite; }
        .doodle-pill { bottom: 15%; left: 6%; width: 60px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.15)); animation: float2 7s ease-in-out infinite; }
        .doodle-sparkle { top: 18%; right: 25%; width: 45px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1)); animation: float1 5s ease-in-out infinite; }
        .doodle-heart { bottom: 25%; right: 12%; width: 45px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1)); animation: float2 6s ease-in-out infinite; }
        .doodle-water { top: 35%; left: 8%; width: 40px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1)); animation: float1 5.5s ease-in-out infinite; }
        .doodle-flower { top: 70%; left: 18%; width: 55px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1)); animation: float2 8s ease-in-out infinite; }
        
        .doodle-plant { position: fixed; bottom: 15px; right: 25px; width: 55px; transition: width 1.5s ease; z-index: 100; pointer-events: none;}

        @keyframes float1 { 0%, 100% { transform: translateY(0px) rotate(0deg); } 50% { transform: translateY(-15px) rotate(5deg); } }
        @keyframes float2 { 0%, 100% { transform: translateY(0px) rotate(-15deg); } 50% { transform: translateY(-12px) rotate(-5deg); } }

        /* Window Container */
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

        /* Chart & Date Cards */
        .chart-container { display: flex; align-items: flex-end; height: 180px; gap: 15px; margin: 30px 0; padding-bottom: 15px; border-bottom: 3px solid rgba(138, 28, 95, 0.2); }
        .bar-col { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; }
        .bar { width: 100%; border-radius: 15px 15px 0 0; box-shadow: 0 -4px 15px rgba(0,0,0,0.1); transition: height 1.2s ease; position: relative;}
        .bar-red { background: linear-gradient(to top, #ef4444, #fca5a5); }
        .bar-purple { background: linear-gradient(to top, #9333ea, #d8b4fe); }
        .bar-yellow { background: linear-gradient(to top, #eab308, #fef08a); }
        .bar-peach { background: linear-gradient(to top, #f97316, #fdba74); }
        .bar-label { margin-top: 12px; font-weight: 800; font-size: 0.95rem; text-align: center; color: var(--deep-magenta); }

        .date-card { background: rgba(255,255,255,0.8); border-radius: 20px; padding: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-top: 10px; border: 1px solid rgba(244,114,182,0.3);}
        .date-title { font-size: 0.9rem; font-weight: 700; color: #8A1C5F; text-transform: uppercase; letter-spacing: 1px; }
        .date-value { font-size: 1.4rem; font-weight: 900; color: #2D0A22; margin-top: 5px; }

        .history-log { max-height: 150px; overflow-y: auto; padding-right: 10px; margin-top: 20px; }
        .history-item { background: rgba(255,255,255,0.6); padding: 10px 15px; border-radius: 12px; margin-bottom: 8px; font-weight: 600; display: flex; justify-content: space-between; border: 1px solid rgba(255,255,255,0.8); }

        .disclaimer { background: rgba(255, 255, 255, 0.7); border: 2px dashed var(--primary-
