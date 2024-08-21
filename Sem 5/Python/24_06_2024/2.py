import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('/home/rebel/Roger/College/Sem 5/Python/24_jul_2024/dataset.csv')

# Parameters
parameter1 = 'age'
parameter2 = 'bmi'

# Aggregate data
# grouping the mean of age and bmi 
aggregated_data = data.groupby(parameter1)[parameter2].mean().reset_index()

# Plot details
plt.figure(figsize=(12, 7))

# alpha controls the transparency of the bars
plt.bar(aggregated_data[parameter1], aggregated_data[parameter2], alpha=1, color='skyblue')
plt.title(f'Average {parameter2} by {parameter1}')
plt.xlabel(parameter1)
plt.ylabel(f'Average {parameter2}')
plt.xticks(rotation=45)  # Rotate x labels if necessary
plt.grid()
plt.show()
