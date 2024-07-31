import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('dataset.csv')

# parameters
parameter1 = 'age'
parameter2 = 'bmi'

# graph details
plt.figure(figsize=(10, 6))
plt.scatter(data[parameter1], data[parameter2], alpha=0.5)
plt.title(f'{parameter1} vs {parameter2}')
plt.xlabel(parameter1)
plt.ylabel(parameter2)
plt.grid(True)
plt.show()
