import streamlit as st
import pandas as pd
import datetime

# --- 1. PAGE CONFIGURATION (Must be the first line) ---
st.set_page_config(page_title="PV Triage Engine", page_icon="🏥", layout="wide")

# --- 2. EXPANDED MOCK CLINICAL DATABASE ---
hospital_feed = [
    {"Case_ID": "IND-901", "Drug": "Paracetamol", "Reported_Date": "2026-05-25", "Narrative": "Patient reported minor stomach upset and nausea."},
    {"Case_ID": "IND-902", "Drug": "Atorvastatin", "Reported_Date": "2026-05-26", "Narrative": "Patient suffered a severe stroke and was rushed to the emergency room."},
    {"Case_ID": "IND-903", "Drug": "Amoxicillin", "Reported_Date": "2026-05-26", "Narrative": "Developed severe anaphylaxis, required immediate ICU hospitalization."},
    {"Case_ID": "IND-904", "Drug": "Metformin", "Reported_Date": "2026-05-27", "Narrative": "Routine checkup. Patient reported localized muscle pain."},
    {"Case_ID": "IND-905", "Drug": "Atorvastatin", "Reported_Date": "2026-05-27", "Narrative": "Mild muscle cramps reported after 2 weeks of dosage."},
    {"Case_ID": "IND-906", "Drug": "Ibuprofen", "Reported_Date": "2026-05-28", "Narrative": "Patient died due to fatal gastrointestinal bleeding."},
    {"Case_ID": "IND-907", "Drug": "Lisinopril", "Reported_Date": "2026-05-28", "Narrative": "Dry cough reported, no other significant symptoms."},
    {"Case_ID": "IND-908", "Drug": "Omeprazole", "Reported_Date": "2026-05-29", "Narrative": "Patient complained of mild headache and dizziness."},
    {"Case_ID": "IND-909", "Drug": "Metformin", "Reported_Date": "2026-05-29", "Narrative": "Patient hospitalized with life-threatening lactic acidosis."},
    {"Case_ID": "IND-910", "Drug": "Amoxicillin", "Reported_Date": "2026-05-30", "Narrative": "Slight skin rash on arms, prescribed topical cream."},
    {"Case_ID": "IND-911", "Drug": "Paracetamol", "Reported_Date": "2026-05-30", "Narrative": "Liver failure detected after accidental overdose, emergency care provided."},
    {"Case_ID": "IND-912", "Drug": "Lisinopril", "Reported_Date": "2026-05-30", "Narrative": "Blood pressure stabilized, patient feels fatigued."},
    {"Case_ID": "IND-913", "Drug": "Ibuprofen", "Reported_Date": "2026-05-30", "Narrative": "Heartburn and mild indigestion."},
    {"Case_ID": "IND-914", "Drug": "Atorvastatin", "Reported_Date": "2026-05-30", "Narrative": "No adverse events reported during follow up."},
    {"Case_ID": "IND-915", "Drug": "Omeprazole", "Reported_Date": "2026-05-30", "Narrative": "Severe allergic reaction, breathing difficulties, admitted to hospital."}
]

# --- 3. THE TRIAGE LOGIC ENGINE ---
serious_keywords = ["died", "hospital", "hospitalized", "fatal", "life-threatening", "emergency", "icu", "stroke", "anaphylaxis", "failure", "overdose"]
processed_data = []

for case in hospital_feed:
    case_text = case["Narrative"].lower()
    detected_triggers = [word for word in serious_keywords if word in case_text]
    
    received_date = datetime.datetime.strptime(case["Reported_Date"], "%Y-%m-%d").date()
    
    if len(detected_triggers) > 0:
        classification = "SERIOUS (15-Day)"
        deadline = received_date + datetime.timedelta(days=15)
        status_icon = "🚨"
    else:
        classification = "NON-SERIOUS (90-Day)"
        deadline = received_date + datetime.timedelta(days=90)
        status_icon = "✅"
        
    processed_data.append({
        "Status": status_icon,
        "Case ID": case["Case_ID"],
        "Target Drug": case["Drug"],
        "Classification": classification,
        "Regulatory Deadline": deadline.strftime("%Y-%m-%d"),
        "Triggers Found": ", ".join(detected_triggers).upper() if detected_triggers else "None",
        "Clinical Narrative": case["Narrative"]
    })

# Convert to Pandas DataFrame for a beautiful table
df = pd.DataFrame(processed_data)

# --- 4. FRONT-END AESTHETIC UI ---
st.title("🏥 PV Regulatory Triage & ICSR Processing Engine")
st.markdown("An automated NLP pipeline designed to scan clinical narratives, detect FDA seriousness criteria, and calculate regulatory submission deadlines.")
st.markdown("---")

# Metrics Dashboard
total_cases = len(df)
serious_cases = len(df[df["Classification"] == "SERIOUS (15-Day)"])
non_serious_cases = total_cases - serious_cases

col1, col2, col3 = st.columns(3)
col1.metric("Total ICSRs Processed", total_cases)
col2.metric("Critical Alerts (Serious)", serious_cases, delta="- Expedited Review Required", delta_color="inverse")
col3.metric("Standard Cases (Non-Serious)", non_serious_cases, delta="90-Day Queue", delta_color="normal")

st.markdown("---")

# UI Tabs for better organization
tab1, tab2 = st.tabs(["🗂️ Interactive Data Table", "📥 Export & Compliance"])

with tab1:
    st.subheader("Live Triage Results")
    # Filters
    selected_drug = st.selectbox("Filter by Suspect Drug:", ["All Drugs"] + sorted(list(df["Target Drug"].unique())))
    
    if selected_drug != "All Drugs":
        display_df = df[df["Target Drug"] == selected_drug]
    else:
        display_df = df
        
    # Display the dataframe with Streamlit's native styling
    st.dataframe(display_df, use_container_width=True, hide_index=True)

with tab2:
    st.subheader("Regulatory CSV Export")
    st.markdown("Download the fully processed triage log for upload into safety databases (Argus, ARISg, etc.).")
    
    # Convert DataFrame to CSV format in memory
    csv_data = df.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 Download Triage Log (CSV)",
        data=csv_data,
        file_name=f"PV_Triage_Log_{datetime.date.today()}.csv",
        mime="text/csv"
    )