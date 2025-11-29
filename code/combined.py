import pandas as pd

# Define file paths
input_csv = "20250708163843_Ankit neuro_EEG MAIN STUDY.csv"
output_csv = "20250708163843_Ankit neuro_EEG MAIN STUDY.csv"

# Define headers based on .info file
headers = [
    'P8', 'T8', 'CP6', 'FC6', 'F8', 'F4', 'C4', 'P4', 'AF4', 'Fp2',
    'Fp1', 'AF3', 'Fz', 'FC2', 'Cz', 'CP2', 'PO3', 'O1', 'Oz', 'O2',
    'PO4', 'Pz', 'CP1', 'FC1', 'P3', 'C3','F3','F7', 'FC5', 'CP5', 'T7', 'P7',
    'Event_Marker', 'Aux1', 'Aux2', 'Marker_Flag', 'Timestamp'
]

# Load the original CSV (no headers)
df = pd.read_csv(input_csv, header=None)

# Assign new headers
df.columns = headers

# Save to a new CSV file with headers
df.to_csv(output_csv, index=False)

print("CSV file updated with headers and saved as:", output_csv)
