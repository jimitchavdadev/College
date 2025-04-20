import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

np.random.seed(42)

def simulate_sensor_data(sensor_type,n_points=1235):
    if sensor_type=='temperature':
        data=20+5*np.random.randn(n_points)
    elif sensor_type=='pressure':
        data=50+10*np.random.randn(n_points)
    else:
        raise ValueError('sensor_type must be temperature or pressure')
    return data

temperature_data=simulate_sensor_data('temperature')
pressure_data=simulate_sensor_data('pressure')

temperature_avg=np.mean(temperature_data)
pressure_avg=np.mean(pressure_data)
temperature_peak=np.max(temperature_data)
pressure_peak=np.max(pressure_data)


print(f"Temperature - Avg: {temperature_avg:.2f}, Peak: {temperature_peak:.2f}")
print(f"Pressure - Avg: {pressure_avg:.2f}, Peak: {pressure_peak:.2f}")

data={
    'Temperature':temperature_data,
    'Pressure':pressure_data
}

df=pd.DataFrame(data)

csv_file_path=os.path.join(os.getcwd(),'sensor_data.csv')

df.to_csv(csv_file_path,index=False)

print(f"Data saved to {csv_file_path}")

plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
plt.plot(temperature_data,label='Temperature',color='blue')
plt.axhline(y=temperature_avg,color='red',linestyle='--',label='Average')
plt.title('Temperature Sensor Data')
plt.xlabel("Time")
plt.ylabel("Temperature(Celcius)")
plt.legend()

plt.subplot(1,2,2)
plt.plot(pressure_data,label='Pressure',color='green')
plt.axhline(y=pressure_avg,color='red',linestyle='--',label='Average')
plt.title('Pressure Sensor Data')
plt.xlabel("Time")
plt.ylabel("Pressure(Pascal)")
plt.legend()

plt.savefig('sensor_data.png')

plt.show()

df_read=pd.read_csv(csv_file_path)

print("\nData read from CSV File:")
print(df_read.head())

df_read=pd.read_csv(csv_file_path)

print("\ndata read from csv file")
print(df_read.head())

temperature_std=np.std(df_read['Temperature'])
pressure_std=np.std(df_read['Pressure'])

print(f"\nadditional statistics:")
print(f"temperatue - std dev: {temperature_std:.2f}")
print(f"pressure - std dev: {pressure_std:.2f}")