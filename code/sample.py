import csv

# Input and output file paths
input_file = '20250708163843_Ankit neuro_EEG MAIN STUDY.easy'   # Replace with your input file path
output_file = '20250708163843_Ankit neuro_EEG MAIN STUDY.csv' # Replace with your output file path

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    for line in infile:
        # Split the line into fields using tab as the delimiter
        fields = line.strip().split('\t')
        
        # Extract the second-to-last field if available
        if len(fields) >= 2:
            column_value = fields[-2]  # Second-to-last field
        else:
            column_value = ''
        
        # Write the value to the CSV
        writer.writerow([column_value])

print(f"CSV file '{output_file}' has been created with the extracted column.")