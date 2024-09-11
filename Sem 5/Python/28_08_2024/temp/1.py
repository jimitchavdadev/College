import os
import pandas as pd

base_dir = '/home/rebel/Roger/College/Sem 5/Python/28_08_2024/temp'

stores = [f'store00{i}' for i in range(1, 7)]

def filter_valid_sales(df, file_path):

    negative_sales = df[df['no_units_sold'] < 0]
    
    if not negative_sales.empty:
        print(f"Warning: Found negative 'no_units_sold' values in {file_path}:")
        print(negative_sales)
    
    #return rows 
    return df[df['no_units_sold'] >= 0]

def generate_report(store):
    store_dir = os.path.join(base_dir, store)
    all_data = []
    
    for i in range(1, 13):
        file_path = os.path.join(store_dir, f'{str(i).zfill(2)}.csv')
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()  #remove whitespace column names
            
            if 'product_name' in df.columns and 'no_units_sold' in df.columns:
                df = filter_valid_sales(df, file_path)
                all_data.append(df)
            else:
                print(f"Error: Columns not as expected in {file_path}")
    
    if all_data:
        all_data_df = pd.concat(all_data)
        
        #total slaes
        total_sales = all_data_df.groupby('product_name')['no_units_sold'].sum().reset_index()
        total_sales = total_sales.sort_values(by='no_units_sold', ascending=False)
        
        # Overall total sales
        overall_total_sales = total_sales['no_units_sold'].sum()
        
        #top 5 
        top_5_products = total_sales.head(5)
        
        #create report
        report = pd.DataFrame({
            'Total Sales': [overall_total_sales],
            'Top 5 Best Selling Products': [top_5_products.to_dict('records')]
        })
        
        #save report
        report_file_path = os.path.join(store_dir, f'{store}_report.csv')
        report.to_csv(report_file_path, index=False)
        
        print(f'Report generated for {store} and saved at {report_file_path}')
    else:
        print(f"No valid data found for {store}")

def generate_combined_report():
    combined_data = []
    
    for store in stores:
        store_dir = os.path.join(base_dir, store)
        for i in range(1, 13):
            file_path = os.path.join(store_dir, f'{str(i).zfill(2)}.csv')
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                df.columns = df.columns.str.strip()  #remove whitespace 
                
                if 'product_id' in df.columns and 'no_units_sold' in df.columns:
                    df = filter_valid_sales(df, file_path)
                    combined_data.append(df)
    
    if combined_data:
        all_data_df = pd.concat(combined_data)
        
        #total and average all store
        total_sales = all_data_df.groupby('product_id')['no_units_sold'].sum().reset_index()
        total_sales.columns = ['product_id', 'total_units_sold']
        
        num_stores = len(stores)
        total_sales['average_units_sold'] = (total_sales['total_units_sold'] / num_stores).round(2)
        
        #save combined report
        combined_report_path = os.path.join(base_dir, 'combined_report.csv')
        total_sales.to_csv(combined_report_path, index=False)
        
        print(f'Combined report saved at {combined_report_path}')
    else:
        print("No valid data found for any store.")

for store in stores:
    generate_report(store)
    generate_combined_report()
