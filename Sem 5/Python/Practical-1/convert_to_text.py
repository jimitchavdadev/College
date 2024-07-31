import os
import pandas as pd

input_folder = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/csv_datasets'
output_folder = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/txt_files'


# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Iterate through all files in the input folder
for file_name in os.listdir(input_folder):
    # Check if the file is a CSV file
    if file_name.endswith('.csv'):
        csv_file_path = os.path.join(input_folder, file_name)
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)

        # Create the output file path with .txt extension
        txt_file_name = file_name.replace('.csv', '.txt')
        txt_file_path = os.path.join(output_folder, txt_file_name)

        # Write the DataFrame to a TXT file
        with open(txt_file_path, 'w') as txt_file:
            # Write the header
            txt_file.write('\t'.join(df.columns) + '\n')

            # Write the rows
            for _, row in df.iterrows():
                txt_file.write('\t'.join(map(str, row.values)) + '\n')
