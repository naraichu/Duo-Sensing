import serial
import numpy as np
import time
import json

# Input number of frequency being swept
freq_len = 200

# Number of byte length to be decoded
# offset is 3 because for 0, -100, and resistive value
byte_len = (freq_len + 3) * 2

# Declare port number and baudrate
ser = serial.Serial('COM12', 115200)

# Flag when Arduino is ready
isStart = False

# File path that JSON is stored
file_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Arduino_Software/Duo_Tactile_Software/ML/datasets.json"

# Classified actions
action = ["None", "One_finger", "Two_fingers", "Three_fingers", "Palm"]

# Count number of datasets being stored
count = 0



def read_serial_JSON():
    global count
    
    try:

        # Add opening square bracket "[" at the start of the file
        with open(file_path, "a") as f:
            f.write("[")

        #while count <= 100:
        while True:
            # Read data from the serial port
            data = ser.read(byte_len)

            # Convert the received bytes back to signed integers array
            all_array = np.array([int.from_bytes(data[i:i + 2], byteorder='little', signed=True) for i in range(0, byte_len, 2)])

            # If valid then separate data and return
            if is_data_valid(all_array):

                # Separate data out into each category
                res_value, cap_y_axis = separate_data(all_array)

                # Increment count by 1
                count += 1


                # Output resistive sensing value
                print("SFCS   : ", cap_y_axis)
                print("Action : ", action[1])
                print("Count  : ", count)
                print("\n")



                json_dict = {
                    "sfcs_value": cap_y_axis.tolist(),  # Convert NumPy array to list
                    "action": action[1],
                }

                # Write to JSON
                with open(file_path, "a") as f:  # Open file in append mode
                    if f.tell() > 1:  # If not the first element, add a comma before appending
                        f.write(",\n")
                    json.dump(json_dict, f, separators=(",", ":"))
                    f.write("\n")


            # If not valid, return last known data
            else:
                # Restart the serial connection
                ser.close()
                ser.open()


    except KeyboardInterrupt:

        # Add closing square bracket "]" when keyboard interrupt occurs
        with open(file_path, "a") as f:
            f.write("\n]")

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
        print(">> Get ready to generate data!!!")
        time.sleep(6)
        isStart = True

    read_serial_JSON()
