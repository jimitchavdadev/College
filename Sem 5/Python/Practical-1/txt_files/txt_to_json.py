import pandas as pd
import json

txt_file = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/txt_files/combined_output.txt'
json_file = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/txt_files/avg_ratings.json'

# Read the TXT file into a DataFrame
# Assuming tab-separated values (TSV) format
df = pd.read_csv(txt_file, delimiter='\t')

# Check if required columns exist
if 'ProductID' not in df.columns or 'Review' not in df.columns:
    raise ValueError("TXT file must contain 'ProductID' and 'Review' columns")

# Calculate average ratings per ProductID
avg_ratings = df.groupby('ProductID')['Review'].mean()

# Convert the Series to a dictionary
avg_ratings_dict = avg_ratings.to_dict()

# Write the dictionary to a JSON file
with open(json_file, 'w') as f:
    json.dump(avg_ratings_dict, f, indent=4)
