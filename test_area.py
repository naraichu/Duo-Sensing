import serial
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# NOTE
# This is the duo-sensing program to read value from both resistive and capacitive sensing.

# Input number of frequency being swept
freq_len = 200

# Number of byte length to be decoded
# offset is 3 because for 0, -100, and resistive value
byte_len = (freq_len + 3) * 2

# Declare port number and baudrate
ser = serial.Serial('COM12', 115200)

# Flag when Arduino is ready
isStart = False

# Arrays for Capacitive sensing (SFCS)
cap_x_axis = np.arange(freq_len + 1)

# Backup value in case there is an error in data transmission
res_back_value = 0
cap_y_back_axis = np.zeros(freq_len + 2)

# Time steps array
t = np.arange(freq_len + 1)

# Initialize matplotlib for 2 graphs visualization
# Line 1 = SFCS
# Line 2 = Resistive
fig, (ax1, ax2) = plt.subplots(2)

ax1.set(title='Swept Frequency Capacitive Sensing',
        xlim=[0, freq_len + 1],
        ylim=[0, 1100],
        xlabel='Frequency',
        ylabel='Amplitude')

ax2.set(title='Resistive Sensing',
        xlim=[0, freq_len + 1],
        ylim=[-60, 60],
        xlabel='Time steps',
        ylabel='Voltage')

def read_serial():
    try:
        while True:
            # Read data from the serial port
            data = ser.read(byte_len)

            # Convert the received bytes back to signed integers array
            all_array = np.array([int.from_bytes(data[i:i + 2], byteorder='little', signed=True) for i in range(0, byte_len, 2)])

            # If valid then separate data and return
            if is_data_valid(all_array):
                # Separate data out into each category
                res_value, cap_y_axis = separate_data(all_array)

                # Store the latest value as the backup
                cap_y_back_axis = cap_y_axis
                res_back_value = res_value

                # Return reading values
                return res_value, cap_y_axis

            # If not valid, return last known data
            else:
                # Restart the serial connection
                ser.close()
                ser.open()

                # Return backup values
                return res_back_value, cap_y_back_axis

    except KeyboardInterrupt:
        # Close the serial connection when the program is interrupted
        print("<-- Port closed -->")
        ser.close()

# Separate data out from the array into appropriate sensing types
def separate_data(all_array):
    all_array = np.delete(all_array, -2)    # Pop -100 (last 2 value) out
    res_value = all_array[-1]               # Get the resistive value in the last index
    cap_y_axis = np.delete(all_array, -1)   # Pop res_value out

    return res_value, cap_y_axis

# Check whether the value is valid
def is_data_valid(all_array):
    return len(all_array) == freq_len + 3 and all_array[freq_len + 1] == -100

def update(frame):
    # Clear previous plot
    ax1.clear()
    ax2.clear()

    res_value, cap_y_axis = read_serial()

    # Plot SFCS data
    ax1.plot(cap_x_axis, cap_y_axis, 'b-', 'o', markersize=1)
    ax1.set_title('Swept Frequency Capacitive Sensing')
    ax1.set_xlim(0, freq_len + 1)
    ax1.set_ylim(0, 1100)
    ax1.set_xlabel('Frequency')
    ax1.set_ylabel('Amplitude')

    # Plot Resistive sensing data
    ax2.plot(t[:len(res_value)], res_value, 'g-', 'o', markersize=1)
    ax2.set_title('Resistive Sensing')
    ax2.set_xlim(0, freq_len + 1)
    ax2.set_ylim(-60, 60)
    ax2.set_xlabel('Time steps')
    ax2.set_ylabel('Voltage')

    return

# Main function
if __name__ == "__main__":
    if not isStart:
        print(">> Waiting 6 seconds for Arduino to setup...")
        time.sleep(6)
        isStart = True

    ani = FuncAnimation(fig, update, frames=100, interval=200)
    plt.show()
