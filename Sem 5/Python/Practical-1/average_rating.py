import pandas as pd
import json

csv_file = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/csv_datasets/combined_output.csv'
json_file = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/output_file.json'


# Read the CSV file into a dataframe
df = pd.read_csv(csv_file)

# Group by ProductID and calculate the average rating
avg_ratings = df.groupby('ProductID')['Review'].mean().reset_index()

# Convert the dataframe to a dictionary
avg_ratings_dict = avg_ratings.set_index('ProductID').to_dict()['Review']

# Write the dictionary to a JSON file
with open(json_file, 'w') as f:
    json.dump(avg_ratings_dict, f, indent=4)

