import datetime
import csv # Built-in Python module for handling spreadsheets

def run_batch_pv_triage(patient_database, received_date_str):
    # This list will hold our final processed reports to write to the CSV
    processed_data = []

    received_date = datetime.datetime.strptime(received_date_str, "%Y-%m-%d").date()
    serious_keywords = ["died", "hospital", "hospitalized", "fatal", "life-threatening", "emergency", "icu", "stroke"]

    print("=== STARTING BATCH EXTRACTION & TRIAGE ===")

    for case in patient_database:
        case_text_lower = case["notes"].lower()
        is_serious = False
        detected_triggers = []

        # Scan for safety triggers
        for word in serious_keywords:
            if word in case_text_lower:
                is_serious = True
                detected_triggers.append(word)

        # Apply regulatory timeline rules
        if is_serious:
            classification = "SERIOUS"
            deadline = received_date + datetime.timedelta(days=15)
            action = "EXPEDITE - MEDICAL REVIEW REQUIRED"
        else:
            classification = "NON-SERIOUS"
            deadline = received_date + datetime.timedelta(days=90)
            action = "STANDARD PROCESSING QUEUE"

        # Create a clean row for our spreadsheet
        report_row = {
            "Patient_ID": case["id"],
            "Drug_Name": case["drug"],
            "Classification": classification,
            "Detected_Triggers": ", ".join(detected_triggers) if detected_triggers else "None",
            "Submission_Deadline": deadline.strftime("%Y-%m-%d"),
            "Action_Required": action
        }
        processed_data.append(report_row)

    # ==========================================
    # 💾 THE CSV EXPORT CORE LOGIC
    # ==========================================
    csv_filename = "PV_Regulatory_Triage_Log.csv"

    # Column Headers for the spreadsheet
    headers = ["Patient_ID", "Drug_Name", "Classification", "Detected_Triggers", "Submission_Deadline", "Action_Required"]

    # Open the file and write the dictionaries row by row
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        # Write the top header row
        writer.writeheader()

        # Write all our processed data rows at once
        writer.writerows(processed_data)

    print(f"\n✅ SUCCESS: Processed {len(processed_data)} cases successfully.")
    print(f"💾 File generated and saved as: [ {csv_filename} ]")


# ==========================================
# MOCK INCOMING DATA STREAM
# ==========================================
hospital_feed = [
    {"id": "IND-901", "drug": "Paracetamol", "notes": "Patient reported minor stomach upset and nausea."},
    {"id": "IND-902", "drug": "Atorvastatin", "notes": "Patient suffered a severe stroke and was rushed to the emergency room."},
    {"id": "IND-903", "drug": "Amoxicillin", "notes": "Developed severe anaphylaxis, required immediate hospitalization."},
    {"id": "IND-904", "drug": "Metformin", "notes": "Routine checkup. Patient reported localized muscle pain but no other issues."}
]

# Run the system
run_batch_pv_triage(patient_database=hospital_feed, received_date_str="2026-05-30")