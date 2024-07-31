import os
import pandas as pd

csv_file = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/csv_datasets/combined_output.csv'
summary_file = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/summary.txt'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Count total number of reviews
total_reviews = len(df)

# Identify valid and invalid reviews
valid_reviews = df.dropna()
invalid_reviews = df[df.isnull().any(axis=1)]

# Calculate average ratings per ProductID
avg_ratings = df.groupby('ProductID')['Review'].mean().reset_index()

# Find top 3 products based on average rating
top_products = avg_ratings.nlargest(3, 'Review')

# Write the summary to a file
with open(summary_file, 'w') as file:
    # Total number of reviews
    file.write(f"Total number of reviews: {total_reviews}\n\n")

    # Valid reviews
    file.write(f"Valid reviews (total {len(valid_reviews)}):\n")
    for _, row in valid_reviews.iterrows():
        file.write(f"{row.to_dict()}\n")
    file.write("\n")

    # Invalid reviews
    file.write(f"Invalid reviews (total {len(invalid_reviews)}):\n")
    for _, row in invalid_reviews.iterrows():
        file.write(f"{row.to_dict()}\n")
    file.write("\n")

    # Top 3 products
    file.write("Top 3 products based on average rating:\n")
    for _, row in top_products.iterrows():
        file.write(f"ProductID: {row['ProductID']}, Average Rating: {row['Review']:.2f}\n")
