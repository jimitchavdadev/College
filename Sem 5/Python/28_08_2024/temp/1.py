import os
import pandas as pd

# Define the base directory where store data is located.
base_dir = '/home/rebel/Roger/College/Sem 5/Python/28_08_2024/temp'

# Create a list of store names (store001 to store006).
stores = [f'store00{i}' for i in range(1, 7)]

def filter_valid_sales(df, file_path):
    # Identify rows with negative sales.
    negative_sales = df[df['no_units_sold'] < 0]
    
    # If there are negative sales, print a warning message with details.
    if not negative_sales.empty:
        print(f"Warning: Found negative 'no_units_sold' values in {file_path}:")
        print(negative_sales)
    
    # Return only rows with non-negative sales.
    return df[df['no_units_sold'] >= 0]

def generate_report(store):
    # Create the directory path for the specific store.
    store_dir = os.path.join(base_dir, store)
    all_data = []  # Initialize a list to collect data from all months.
    
    # Loop through each month (1 to 12).
    for i in range(1, 13):
        # Construct the file path for the monthly sales data.
        file_path = os.path.join(store_dir, f'{str(i).zfill(2)}.csv')
        
        # Check if the file exists.
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)  # Read the CSV file into a DataFrame.
            df.columns = df.columns.str.strip()  # Remove whitespace from column names.
            
            # Check if required columns are present in the DataFrame.
            if 'product_name' in df.columns and 'no_units_sold' in df.columns:
                df = filter_valid_sales(df, file_path)  # Filter out invalid sales data.
                all_data.append(df)  # Append the valid DataFrame to the list.
            else:
                print(f"Error: Columns not as expected in {file_path}")  # Print an error message if columns are missing.
    
    # If there is any valid data collected, proceed to generate the report.
    if all_data:
        all_data_df = pd.concat(all_data)  # Concatenate all DataFrames into one.
        
        # Calculate total sales by product name.
        total_sales = all_data_df.groupby('product_name')['no_units_sold'].sum().reset_index()
        total_sales = total_sales.sort_values(by='no_units_sold', ascending=False)  # Sort by total sales in descending order.
        
        # Calculate overall total sales across all products.
        overall_total_sales = total_sales['no_units_sold'].sum()
        
        # Get the top 5 best-selling products.
        top_5_products = total_sales.head(5)
        
        # Create a report DataFrame with total sales and top 5 products.
        report = pd.DataFrame({
            'Total Sales': [overall_total_sales],
            'Top 5 Best Selling Products': [top_5_products.to_dict('records')]
        })
        
        # Save the report to a CSV file in the store's directory.
        report_file_path = os.path.join(store_dir, f'{store}_report.csv')
        report.to_csv(report_file_path, index=False)  # Write the report to a CSV file.
        
        print(f'Report generated for {store} and saved at {report_file_path}')  # Print confirmation of report generation.
    else:
        print(f"No valid data found for {store}")  # Inform if no valid data was found.

def generate_combined_report():
    combined_data = []  # Initialize a list to collect data from all stores.
    
    # Loop through each store.
    for store in stores:
        store_dir = os.path.join(base_dir, store)  # Create the directory path for the store.
        
        # Loop through each month (1 to 12).
        for i in range(1, 13):
            # Construct the file path for the monthly sales data.
            file_path = os.path.join(store_dir, f'{str(i).zfill(2)}.csv')
            
            # Check if the file exists.
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)  # Read the CSV file into a DataFrame.
                df.columns = df.columns.str.strip()  # Remove whitespace from column names.
                
                # Check if required columns are present in the DataFrame.
                if 'product_id' in df.columns and 'no_units_sold' in df.columns:
                    df = filter_valid_sales(df, file_path)  # Filter out invalid sales data.
                    combined_data.append(df)  # Append the valid DataFrame to the list.
    
    # If there is any valid data collected, proceed to generate the combined report.
    if combined_data:
        all_data_df = pd.concat(combined_data)  # Concatenate all DataFrames into one.
        
        # Calculate total sales by product ID across all stores.
        total_sales = all_data_df.groupby('product_id')['no_units_sold'].sum().reset_index()
        total_sales.columns = ['product_id', 'total_units_sold']  # Rename columns for clarity.
        
        # Calculate the average units sold across all stores.
        num_stores = len(stores)
        total_sales['average_units_sold'] = (total_sales['total_units_sold'] / num_stores).round(2)
        
        # Save the combined report to a CSV file.
        combined_report_path = os.path.join(base_dir, 'combined_report.csv')
        total_sales.to_csv(combined_report_path, index=False)  # Write the combined report to a CSV file.
        
        print(f'Combined report saved at {combined_report_path}')  # Print confirmation of combined report generation.
    else:
        print("No valid data found for any store.")  # Inform if no valid data was found.

# Generate individual reports for each store and the combined report.
for store in stores:
    generate_report(store)  # Generate report for the current store.
    generate_combined_report()  # Generate combined report for all stores.