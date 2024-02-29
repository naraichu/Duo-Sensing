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
cap_x_axis = np.arange(freq_len + 1, dtype = int)


# Backup value in case there is error in data transmission
res_back_value = 0
cap_y_back_axis = np.zeros(freq_len + 2, dtype = int)


def read_serial():
    global cap_y_back_axis, res_back_value
    try:
        while True:
            # Read data from the serial port
            data = ser.read(byte_len)
            
            # Convert the received bytes back to signed integers array
            all_array = np.array([int.from_bytes(data[i:i + 2], byteorder = 'little', signed = True) for i in range(0, byte_len, 2)])
            
            # If valid then seperate data and return
            if is_data_valid(all_array):
                
                # Seperate data out into each catergory
                res_value, cap_y_axis = SeperateData(all_array)
                
                # Store latest value as the backup
                global cap_y_back_axis, res_back_value
                cap_y_back_axis = cap_y_axis
                res_back_value = res_value

                # Return reading values
                # return res_value, cap_y_axis

                
                # Display Duo-sensing values
                print("SFCS: ", cap_y_axis)
                print("Res:", res_value)
                print("\n")
                

            # If not valid, return last known data
            else:
                # Restart the serial connection
                ser.close()
                ser.open()

                # Return backup values
                #return res_back_value, cap_y_back_axis
                
                
                # Putput error message
                print(">> Invalid, display last known values...")
                
                # Display last known value of the data
                print("SFCS: ", cap_y_back_axis)
                print("Res:", res_back_value)
                print("\n")
                

    except KeyboardInterrupt:
        # Close the serial connection when the program is interrupted
        print("<-- Port closed -->")
        ser.close()


# Seperate data out from the array into appropriate sensing types
def SeperateData(all_array):
    all_array = np.delete(all_array, -2)    # Pop -100 (last 2 value) out
    res_value = all_array[-1]               # Get the resistive value in last index
    cap_y_axis = np.delete(all_array, -1)   # Pop res_value out

    return res_value, cap_y_axis

    
# Check whether the value is valid
def is_data_valid(all_array):
    if freq_len + 3 == len(all_array) and all_array[freq_len + 1] == -100:
        return True
    else:
        return False


# Main function
if __name__ == "__main__":

    if not isStart:
        print(">> Waiting 6 seconds for Arduino to setup...")
        time.sleep(6)
        isStart = True
        read_serial()