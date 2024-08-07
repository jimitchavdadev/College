import pandas as pd

# path variables
txt_file = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/reviews.txt'
summary_file = '/home/rebel/Roger/College/Sem 5/Python/Practical-1/summary.txt'

# txt file into a DataFrame
# it will take the separator as tab instead of comma
df = pd.read_csv(txt_file, delimiter='\t')

# total number of reviews
total_reviews = len(df)

# dropna removes all rows with nan values and save it
valid_reviews = df.dropna()

# .any function checks if there is any null value through .isnull function
# axis=1 puts the condition that atleast one value is null
invalid_reviews = df[df.isnull().any(axis=1)]

# average ratings per ProductID
# reset_index is used to reset the indexes if any changes are made in the dataframe
avg_ratings = df.groupby('ProductID')['Review'].mean().reset_index()

# nlargest saves top 3 largest from the reviews section
top_products = avg_ratings.nlargest(3, 'Review')

# summary file
with open(summary_file, 'w') as file:
    # total number of reviews
    file.write(f"Total number of reviews: {total_reviews}\n\n")

    # valid reviews
    file.write(f"Valid reviews (total {len(valid_reviews)}):\n")
    for _, row in valid_reviews.iterrows():
        file.write(f"{row.to_dict()}\n")
    file.write("\n")

    # invalid reviews
    file.write(f"Invalid reviews (total {len(invalid_reviews)}):\n")
    for _, row in invalid_reviews.iterrows():
        file.write(f"{row.to_dict()}\n")
    file.write("\n")

    # top 3 products
    file.write("Top 3 products based on average rating:\n")
    for _, row in top_products.iterrows():
        file.write(f"ProductID: {row['ProductID']}, Average Rating: {row['Review']:.2f}\n")
