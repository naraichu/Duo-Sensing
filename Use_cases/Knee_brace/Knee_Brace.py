import serial
import numpy as np
import scipy.signal
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''
#NOTE
This code is for limb joint wearable (best with knee) which only utlise 
resistive sensing. The step is count when there a siginificant peak of 
voltage for a short period of time.


#INFO
External resistors  : 22kΩ
3D model used       : Square_Net_V2 model

'''

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
cap_x_axis = np.arange(freq_len + 1, dtype=int)

# Backup value in case there is an error in data transmission
res_back_value = 0
cap_y_back_axis = np.zeros(freq_len + 2, dtype=int)

# Initialized matplotlib for visualization
fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'hspace': 1.0})


# Global variables to keep track of time steps and resistive values
time_steps = []
res_array = []



def read_serial():
    global cap_y_back_axis, res_back_value
    
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

                # Output resistive sensing values
                print("Act Res: ", res_value)
                print("    Res: ", res_value - 150)
                print("___________________________")

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



# Modify the update function to detect peaks and plot markers
def update(frame):
    # Read new data
    res_value, cap_y_axis = read_serial()

    # Check if read_serial() returned None
    if (res_value is None) or (cap_y_axis is None) or (len(cap_y_axis) != len(cap_x_axis)):
        return None

    # Update time steps
    time_steps.append(frame)
    # Update resistive values with -150 as the offset translation
    res_array.append(res_value -150)

    # Detect peaks in res_array
    peaks, _ = scipy.signal.find_peaks(res_array, width=1, distance=1, threshold=80)

    # Update plots
    ax1.clear()
    ax1.plot(cap_x_axis, cap_y_axis, 'b-', markersize=1)
    ax1.set(title='Swept Frequency Capacitive Sensing',
            xlabel='Frequency',
            ylabel='Amplitude',
            xlim=[0, freq_len + 1],
            ylim=[0, 1100])

    ax2.clear()
    ax2.plot(time_steps, res_array, 'g-', markersize=1)
    ax2.plot([time_steps[i] for i in peaks], [res_array[i] for i in peaks], 'o')  # Plot peaks with 'o'
    ax2.set(title='Resistive Sensing',
            xlabel='Time steps',
            ylabel='Voltage (10^-2)',
            xlim=[max(0, frame - 50), max(50, frame)],
            ylim=[-256, 256])



# Main function
if __name__ == "__main__":
    if not isStart:
        print(">> Waiting 6 seconds for Arduino to set up...")
        time.sleep(6)
        isStart = True

    ani = FuncAnimation(fig, update, interval=100, cache_frame_data=False)
    plt.show()
