import csv

# Input and output file paths
input_file  = '20250708163843_Ankit neuro_EEG MAIN STUDY.easy'  # your .easy file
output_file = '20250708163843_Ankit neuro_EEG MAIN STUDY.csv'   # the resulting .csv

with open(input_file,  'r', newline='') as infile, \
     open(output_file, 'w', newline='') as outfile:

    # Treat the .easy as tab-delimited
    reader = csv.reader(infile, delimiter='\t')
    writer = csv.writer(outfile)  # defaults to comma delimiter

    # Copy every row in full
    for row in reader:
        writer.writerow(row)

print(f"Converted '{input_file}' → '{output_file}' successfully.")
