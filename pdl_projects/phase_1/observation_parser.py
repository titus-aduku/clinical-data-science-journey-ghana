# PDL Project 1.1 - Clinical Observation Parser (Final Version)

# --- The Raw Data ---
raw_observation_string = "Patient: John Doe | Chief Complaint: headache, fever | Temp: 38.5C"

# --- Step 1: Separate the main string ---
observation_parts = raw_observation_string.split('|')

# --- Step 2: Process each part using the "Split -> Extract -> Strip" pattern ---

# Process the name
patient_part = observation_parts[0]
name_label, raw_name = patient_part.split(':') # A cool trick to unpack directly
patient_name = raw_name.strip()

# Process the complaint
complaint_part = observation_parts[1]
complaint_label, raw_complaint = complaint_part.split(':')
complaint = raw_complaint.strip()

# Process the temperature
temperature_part = observation_parts[2]
temperature_label, raw_temperature = temperature_part.split(':')
temperature = raw_temperature.strip()

# --- Step 3: Display the final, clean record ---
print("\n--- Final Parsed Record ---")
print(f"Patient Name: {patient_name}")
print(f"Complaint: {complaint}")
print(f"Temperature: {temperature}")