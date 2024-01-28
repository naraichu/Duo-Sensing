import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Input number of frequency being swept
freq_len = 200

# Number of byte length to be decoded
# offset is 2 because for 0 and -100
byte_len = (freq_len + 2) * 2

# Declare port number and baudrate
ser = serial.Serial('COM12', 115200)

# Generate frequency array (+1 because of 0)
x_axis = np.arange(freq_len + 1)

# Generate zero value array first
y_axis = np.zeros((freq_len + 1), dtype = int)


# Initialise matplotlib
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o', markersize = 1)  # Initialize an empty line
ax.set(xlim=[0, freq_len], ylim=[0, 800], xlabel='Frequency', ylabel='Amplitude')



def read_serial_data():
    try:
        while True:
            # Read data from the serial port
            data = ser.read(byte_len)
            
            # Convert the received bytes back to signed integers
            y_axis = np.array([int.from_bytes(data[i:i+2], byteorder='little', signed=True) for i in range(0, byte_len, 2)])
            
            # Check if the data is correct
            if is_data_valid(y_axis):
                y_axis = np.delete(y_axis, -1)  # Remove -100 (last value) from y_axis

                return y_axis

                # Output result
                #print(y_axis)
                #print("\n")

            else:
                # Close and reopen the serial connection
                print(">> Invalid data")
                ser.close()
                ser.open()

    except KeyboardInterrupt:
        # Close the serial connection when the program is interrupted
        print("<-- Port closed -->")
        ser.close()


def is_data_valid(y_axis):
    if freq_len + 2 == len(y_axis) and y_axis[freq_len + 1] == -100:
        return True
    else:
        return False


def update(frame):
    line.set_ydata(read_serial_data())
    return line,


if __name__ == "__main__":
    line, = ax.plot(x_axis, read_serial_data())
    ani = FuncAnimation(fig, update, frames = None, interval = 200, cache_frame_data = False)

    # Show the plot
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.title('SFCS')
    plt.show()
