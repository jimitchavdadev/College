import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('dataset.csv')

# Function to plot data between two parameters
def plot_data(parameter1, parameter2):
    if parameter1 not in data.columns or parameter2 not in data.columns:
        print("Invalid parameters. Please select parameters from the following list:")
        print(data.columns)
        return
    
    plt.figure(figsize=(10, 6))
    plt.scatter(data[parameter1], data[parameter2], alpha=0.5)
    plt.title(f'{parameter1} vs {parameter2}')
    plt.xlabel(parameter1)
    plt.ylabel(parameter2)
    plt.grid(True)
    plt.show()

# Example usage
plot_data('age', 'medical charges')
