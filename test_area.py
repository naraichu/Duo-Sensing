import serial
import numpy as np
import time
import json
import os


'''
#NOTE
This code is for showing SFCS array for a graph_visualiser.py
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

# Classified actions
action = ["None", "One finger", "Two fingers", "Three fingers", "Palm", "Full"] #<---- !!! Make sure to change based on use case

# Number of datasets per actions
step = 5

# Total length of the JSON
total_len = step * len(action)



def read_serial_JSON():
    global step, total_len
    try:
            
            # Track the last value append to not add ","
            track = 0

            # Track actions being append for classification
            act = 0

            while act < len(action):
                # Count number of datasets being stored
                count = 0

                while count < step:

                    # Read data from the serial port
                    data = ser.read(byte_len)

                    # Convert the received bytes back to signed integers array
                    all_array = np.array([int.from_bytes(data[i:i + 2], byteorder='little', signed=True) for i in range(0, byte_len, 2)])

                    # If valid then separate data and return
                    if is_data_valid(all_array):

                        # Separate data out into each category
                        res_value, cap_y_axis = separate_data(all_array)

                        # Increment by 1
                        count += 1
                        track += 1

                        # Output resistive sensing value
                        print("SFCS   : ", cap_y_axis.tolist())
                        print("Action type : ", action[act])
                        print("\n")


                    # If not valid, return last known data
                    else:
                        # Restart the serial connection
                        ser.close()
                        ser.open()
            
                # Show next action to be stored in JSON and give time delay
                if act < len(action)-1:
                    act += 1
                    print("Get ready for next action...")
                    print("Next action : ", action[act])
                    time.sleep(5)
                
                # In case of reaching limit then break loop
                else:
                    break


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



# Main function
if __name__ == "__main__":
    if not isStart:
        print(">> Get ready, total of", len(action), "actions")
        print("First action : ", action[0])
        time.sleep(6)
        isStart = True

    read_serial_JSON()