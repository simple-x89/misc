#
#
#This script is used to validate quench lab raw data is inline with expected values from HHT2
#KH 2018


import matplotlib.ticker as plticker
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as npy
import pandas as pd
pressure = npy.array([[20, 20, 20], [25, 25, 25], [30, 30, 30], [35, 35, 35],  [40, 40, 40]])
pressure_avg = npy.array([20, 25, 30, 35, 40])

time = npy.array([[4.67, 7.4, 6.95], [6.95, 6.75, 7], [6.95, 5.76, 6.3], [5.7, 5.65, 6.06], [5.5, 5.45, 5.64]])
time_avg = npy.mean(time, axis=1)
mass = npy.array([[2.6325, 3.677, 3.633], [3.791, 3.9325, 3.9585], [4.069, 3.606, 3.964], [3.756, 3.723, 3.801], [3.7995, 3.7885, 3.975]])
mass_avg = npy.mean(mass, axis=1)
conversion = npy.array([15.850323, 15.850323, 15.850323, 15.850323, 15.850323])
flow_rate = mass / time
flow_rate_gpm = [x*15.850323 for x in flow_rate]
flow_rate_avg = mass_avg/time_avg
flow_rate_avg_gpm = flow_rate_avg * conversion
print(flow_rate_avg, mass_avg, time_avg )
plt.subplot(1, 2, 2)
style.use('seaborn')  # style
plt.xlabel('Flow Rate (gpm)')  # x axis label
plt.ylabel('Pressure (PSI)')  # y axis label
#plt.title("Quench Lab flow curve", fontsize=20, loc = 'right')  # title
plt.gcf().subplots_adjust(bottom=0.25)  # slightly resizes window
loc = plticker.MultipleLocator(base=80.0)  # this locator puts ticks at regular intervals
plt.subplot(1, 2, 1)
style.use('seaborn')  # style
plt.xlabel('Flow Rate (gpm)')  # x axis label
plt.ylabel('Pressure (PSI)')  # y axis label
plt.title("Quench Lab flow curve", fontsize=20, loc = 'left')  # title
plt.gcf().subplots_adjust(bottom=0.25)  # slightly resizes window
loc = plticker.MultipleLocator(base=80.0)  # this locator puts ticks at regular intervals
# Plot it!
plt.subplot(1, 2, 2)
plt.scatter(flow_rate_avg_gpm, pressure_avg)
plt.plot(flow_rate_avg_gpm, pressure_avg)

plt.subplot(1, 2, 1)
plt.scatter(flow_rate_gpm, pressure)
plt.show()

