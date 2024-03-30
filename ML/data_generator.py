import serial
import numpy as np
import time
import json


'''
#NOTE
This code is for append SFCS value into JSON format for training the SVM.



#TO DO
1) Rewrite JSON with two actions None and two fingers
2) Troubleshoot the problem, is it from the model or in the file that send data for classification

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

# File path that JSON is stored
json_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/dataset_SFCS_Pad.JSON"

# Classified actions
action = ["None", "Fingers", "Fist", "Palm", "Side"] #<---- !!! Make sure to change based on use case

# Number of datasets per actions
step = 200

# Total length of the JSON
total_len = step * len(action)



def read_serial_JSON():
    global step, total_len
    try:

        # Add opening brackets with name at the start of the file
        with open(json_path, "a") as f:
            f.write('{\n\t"SFCS_pad": [\n') #<---- !!! Make sure to change based on use case
            f.close()
            
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
                        print("SFCS: \n      ", cap_y_axis)
                        print("Action      : ", act+1, "/", len(action))
                        print("Action type : ", action[act])
                        print("Count       : ", count, "/", step)
                        print("\n")
                        
                        # For adding 2D both x and y
                        cap_x_axis = np.arange(201, dtype=int)
                        sfcs_value = np.stack((cap_x_axis,cap_y_axis), axis=-1)
                        
                        json_dict = {
                            "sfcs_value": sfcs_value.tolist(),  # Convert NumPy array to list
                            "action": action[act],
                        }

                        # Write to JSON
                        with open(json_path, "a") as f:  # Open file in append mode
                            f.write("\t\t")
                            json.dump(json_dict, f, separators=(",", ":"))

                            # If last element, do not add ","
                            if (track == total_len):
                                f.write("\n")
                                f.close()
            
                            
                            # Else add ","
                            else:
                                f.write(",\n")
                                f.close()

                            
                    # If not valid, return last known data
                    else:
                        # Restart the serial connection
                        ser.close()
                        ser.open()

                # Give time for serial to re establish connection
                ser.close()
                time.sleep(5)
                ser.open()
            
                # Show next action to be stored in JSON and give time delay
                if act < len(action)-1:
                    act += 1
                    print("_________________________________________")
                    print("Get ready for next action...")
                    print("Next action : ", action[act])
                    time.sleep(2)
                    
                
                
                # In case of reaching limit then break loop
                else:
                    break
                
        
        # Add closing brackets when keyboard interrupt occurs
        with open(json_path, "a") as f:
            f.write("\t]\n}")
            f.close()


    except KeyboardInterrupt:
        # Add closing brackets when keyboard interrupt occurs
        with open(json_path, "a") as f:
            f.write("\t]\n}")
            f.close()
            # Make sure to remove "," on the last element manually at JSON file


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
        print(">> Get ready...")
        print("Total of", len(action), "actions with", step, "steps for each action")
        print("First action : ", action[0])
        time.sleep(6)
        isStart = True

    read_serial_JSON()