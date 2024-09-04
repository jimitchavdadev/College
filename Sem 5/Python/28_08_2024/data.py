import random
import pandas as pd
from datetime import datetime, timedelta

# Constants
start_date = "2024-01-01"
end_date = "2024-12-31"
store_ids = [f"STORE{str(i).zfill(3)}" for i in range(1, 11)]  # 10 stores from STORE001 to STORE010
product_ids = [f"{1000+i}" for i in range(1, 21)]  # 20 products from 1001 to 1020

# Convert date strings to date objects
start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

# Generate list of all dates in the range
all_dates = [start_date_obj + timedelta(days=x) for x in range((end_date_obj - start_date_obj).days + 1)]

# Data population
data = [] 
for date in all_dates:
    for _ in range(random.randint(5, 15)):  # Randomly generate between 5 and 15 sales records per day
        store_id = random.choice(store_ids)
        product_id = random.choice(product_ids)
        quantity_sold = random.randint(1, 30)  # Quantity sold between 1 and 30
        data.append([date.strftime("%Y-%m-%d"), store_id, product_id, quantity_sold])

# Create DataFrame
df = pd.DataFrame(data, columns=["Date", "Store ID", "Product ID", "Quantity Sold"])

# Split the DataFrame into 12 parts, one for each month
monthly_data = {month: df[df['Date'].str.startswith(f"2024-{str(month).zfill(2)}")] for month in range(1, 13)}

# Save each month's data to a separate CSV file
for month, data in monthly_data.items():
    file_path = f"/mnt/data/sales_data_2024_{str(month).zfill(2)}.csv"
    data.to_csv(file_path, index=False)