"""
Script for live plotting from keyboard values
"""


import keyboard
import time
import csv
import matplotlib.pyplot as plt
import numpy as np


# initialize plot
plot_window = 20
y_var = np.array(np.zeros([plot_window]))
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(y_var)

# create running loop
while True:

    # waits for keyboard inputs and turn to float for plotting
    keyb = keyboard.read_key()
    keyb = float(keyb)

    # open and write to csv file
    with open("test_data.csv", "a") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([time.time(), keyb])

    # append variable to end of array
    y_var = np.append(y_var, keyb)
    y_var = y_var[1:plot_window+1]

    # set array and plot in real time
    line.set_ydata(y_var)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()

# end of code
