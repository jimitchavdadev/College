# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Load the CSV file
csv_file_path = 'sensor_data.csv'
df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame
print("Initial Data:")
print(df.head())

# Data Cleaning and Preprocessing
# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values (if any)
df.dropna(inplace=True)

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Detect and handle outliers
# For simplicity, we'll use Z-score to detect outliers
z_scores = np.abs(zscore(df))
df_clean = df[(z_scores < 3).all(axis=1)]

print("\nData after removing outliers:")
print(df_clean.describe())

# Time-Series Analysis with data generated every 10 seconds starting from an absolute time of 0
df_clean['Time'] = np.arange(0, 10 * len(df_clean), 10)
df_clean.set_index('Time', inplace=True)

# Reset index to use Time as a column for regression analysis
df_clean_reset = df_clean.reset_index()

# Define different training/testing ratios
ratios = [0.7, 0.8, 0.9]  # 70% train - 30% test, 80% train - 20% test, 90% train - 10% test

# Create a list to store results
results_list = []

for ratio in ratios:
    print(f"\nTraining/Test Ratio: {ratio} / {1 - ratio}")

    # Linear Regression for Temperature vs. Time
    X_temp = df_clean_reset[['Time']]
    y_temp = df_clean_reset['Temperature']
    
    # Split the data
    X_train_temp, X_test_temp, y_train_temp, y_test_temp = train_test_split(X_temp, y_temp, train_size=ratio, shuffle=False)
    
    # Train the model
    model_temp = LinearRegression()
    model_temp.fit(X_train_temp, y_train_temp)
    y_temp_pred = model_temp.predict(X_test_temp)

    # Metrics for Temperature vs. Time
    rmse_temp = np.sqrt(mean_squared_error(y_test_temp, y_temp_pred))

    # Plotting Temperature vs. Time with Linear Regression
    plt.figure(figsize=(14, 6))
    plt.plot(df_clean_reset['Time'], df_clean_reset['Temperature'], label='Actual Temperature')
    plt.plot(X_test_temp, y_temp_pred, label='Predicted Temperature', color='red')
    plt.title(f'Linear Regression: Temperature vs. Time (Train/Test Ratio {ratio}/{1-ratio})', fontsize=18, fontweight='bold')
    plt.xlabel('Time (seconds)', fontsize=14)
    plt.ylabel('Temperature', fontsize=14)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Linear Regression for Pressure vs. Time
    X_press = df_clean_reset[['Time']]
    y_press = df_clean_reset['Pressure']
    
    # Split the data
    X_train_press, X_test_press, y_train_press, y_test_press = train_test_split(X_press, y_press, train_size=ratio, shuffle=False)
    
    # Train the model
    model_press = LinearRegression()
    model_press.fit(X_train_press, y_train_press)
    y_press_pred = model_press.predict(X_test_press)

    # Metrics for Pressure vs. Time
    rmse_press = np.sqrt(mean_squared_error(y_test_press, y_press_pred))

    # Plotting Pressure vs. Time with Linear Regression
    plt.figure(figsize=(14, 6))
    plt.plot(df_clean_reset['Time'], df_clean_reset['Pressure'], label='Actual Pressure')
    plt.plot(X_test_press, y_press_pred, label='Predicted Pressure', color='red')
    plt.title(f'Linear Regression: Pressure vs. Time (Train/Test Ratio {ratio}/{1-ratio})', fontsize=18, fontweight='bold')
    plt.xlabel('Time (seconds)', fontsize=14)
    plt.ylabel('Pressure', fontsize=14)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Append results to the list
    results_list.append({'Ratio': f'{ratio}/{1-ratio}', 'RMSE_Temperature': rmse_temp, 'RMSE_Pressure': rmse_press})

# Convert results list to DataFrame
results = pd.DataFrame(results_list)

# Print the results table
print("\nResults Table:")
print(results)