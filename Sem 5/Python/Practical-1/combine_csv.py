import os
import pandas as pd

folder_path = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/csv_datasets'
output_file = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/csv_datasets/combined_output.csv'

# List to hold dataframes
dataframes = []

# Iterate through all files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is a CSV file
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        # Read the CSV file into a dataframe
        df = pd.read_csv(file_path)
        dataframes.append(df)

# Combine all dataframes
combined_df = pd.concat(dataframes, ignore_index=True)
# Write the combined dataframe to a new CSV file
combined_df.to_csv(output_file, index=False)
