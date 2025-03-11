import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_sensor_data(n_points=100):
    temperature = 20 + 5 * np.random.randn(n_points)
    pressure = 1000 + 20 * np.random.randn(n_points)
    return temperature, pressure

def save_to_csv(temperature, pressure, filename="sensor_data.csv"):
    df = pd.DataFrame({"Temperature": temperature, "Pressure": pressure})
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def visualize_data(filename="sensor_data.csv"):
    df = pd.read_csv(filename)
    
    # Scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Temperature"], df["Pressure"], alpha=0.7, label="Sensor Data")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Pressure (hPa)")
    plt.title("Temperature vs Pressure")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Histograms
    df.hist(figsize=(10, 5), bins=20)
    plt.suptitle("Temperature and Pressure Distributions")
    plt.show()

if __name__ == "__main__":
    temp, press = generate_sensor_data()
    save_to_csv(temp, press)
    visualize_data()
