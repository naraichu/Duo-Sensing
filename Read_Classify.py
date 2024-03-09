import serial
import numpy as np
import time
import pickle


# Files path for training data and saving the model
pickle_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year_3/CM30082_Individual_Project/Software/Duo_Tactile_Software/ML/SVM/SFCS_SVM.pkl"


input_data = [376, 347, 270, 246, 210, 205, 190, 191, 182, 186, 178, 178, 172, 176,
        173, 177, 170, 173, 169, 170, 164, 161, 159, 160, 159, 167, 160, 158,
        169, 165, 172, 177, 163, 179, 175, 168, 160, 167, 176, 172, 170, 189,
        180, 203, 194, 192, 188, 204, 207, 206, 214, 220, 226, 233, 231, 234,
        237, 245, 250, 255, 261, 271, 276, 285, 292, 302, 308, 318, 326, 335,
        341, 351, 361, 369, 376, 384, 392, 405, 411, 420, 427, 433, 441, 452,
        461, 464, 467, 470, 472, 477, 482, 490, 487, 483, 482, 482, 479, 478,
        480, 483, 488, 487, 479, 474, 471, 466, 463, 462, 463, 464, 465, 470,
        468, 458, 451, 448, 444, 440, 437, 436, 436, 436, 435, 437, 440, 443,
        441, 433, 426, 421, 418, 415, 411, 409, 408, 408, 407, 409, 410, 412,
        415, 418, 418, 419, 414, 405, 398, 395, 392, 391, 387, 386, 385, 384,
        383, 384, 383, 385, 386, 388, 388, 391, 395, 398, 399, 400, 401, 400,
         396, 387, 380, 377, 377, 375, 374, 372, 370, 370, 370, 371, 372, 371,
        372, 373, 373, 375, 376, 378, 379, 381, 384, 388, 390, 392, 393, 395,
        396, 398, 399, 399, 398]



# Load the saved model
with open(pickle_path, 'rb') as f:
    svm_model = pickle.load(f)

# Now you have your SVM model loaded and ready for predictions

# Assuming you have input data 'input_data', you can make predictions as follows:
predicted_actions = svm_model.predict(input_data)


print("Action  : " , predicted_actions)

# 'predicted_actions' will contain the predicted actions based on the input data

















'''
# Load the SVM model
pickle_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Arduino_Software/Duo_Tactile_Software/ML/SVM/SFCS_SVM.pkl"
with open(pickle_path, 'rb') as f:
    svm_model = pickle.load(f)

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

# Global variables to keep track of time steps and resistive values
time_steps = []
res_array = []

def classify_sfcs_data(sfcs_data):
    """
    Function to classify SFCS data using SVM model.
    
    Parameters:
        sfcs_data (array): SFCS data to be classified.
        
    Returns:
        str: Predicted action.
    """
    predicted_action = svm_model.predict([sfcs_data])[0]
    return predicted_action

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

                # Output values
                print("SFCS  :", cap_y_axis)
                print("Res   : ", res_value)

                # Classify SFCS data
                predicted_action = classify_sfcs_data(cap_y_axis)
                print("Predicted Action:", predicted_action)
                print("/n")

            # If not valid, return last known data
            else:
                # Restart the serial connection
                ser.close()
                ser.open()

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
        print(">> Waiting 6 seconds for Arduino to set up...")
        time.sleep(6)
        isStart = True

    read_serial()
'''

