import serial
import numpy as np
import time
import pickle


# Load file paths for each model
SVM_pickle_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/SVM_SFCS_Pad.pkl"
LR_pickle_path  = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/LR_SFCS_Pad.pkl"
NB_pickle_path  = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/NB_SFCS_Pad.pkl"
NN_pickle_path  = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/NN_SFCS_Pad.pkl"
RF_pickle_path  = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/RF_SFCS_Pad.pkl"


# Load pickle SVM
with open(SVM_pickle_path, 'rb') as f:
    svm_model = pickle.load(f)


# Load pickle Logistic regression
with open(LR_pickle_path, 'rb') as f:
    lr_model = pickle.load(f)


# Load pickle Naive Bayes
with open(NB_pickle_path, 'rb') as f:
    nb_model = pickle.load(f)


# Load pickle neural network
with open(NN_pickle_path, 'rb') as f:
    nn_model = pickle.load(f)


# Load pickle random forest
with open(RF_pickle_path, 'rb') as f:
    rf_model = pickle.load(f)



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


def read_classify():
    global cap_x_axis, cap_y_back_axis, res_back_value
    
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

                # Process array into SVM format
                SFCS_value = Array_2D(cap_x_axis,cap_y_axis)
                
                # Output predictions
                svm_predict = svm_model.predict(SFCS_value)
                lr_predict = lr_model.predict(SFCS_value)
                nb_predict = nb_model.predict(SFCS_value)
                nn_predict = nn_model.predict(SFCS_value)
                rf_predict = rf_model.predict(SFCS_value)
                
                print("SVM : ", svm_predict)
                print("LR  : ", lr_predict)
                print("NB  : ", nb_predict)
                print("NN  : ", nn_predict)
                print("RF  : ", rf_predict)
                print("\n")
    

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


def Array_2D(x,y):
    y = np.stack((x,y), axis=-1)  # Stack into 2D array        [x0,x1...x200] + [y0, y1...y200] --> [[x0,y0],[x1,y1]...[x200,y200]]
    y = y.reshape(1,-1)           # Reshape to form 1D array   [[x0,y0],[x1,y1]...[x200,y200]]  --> [[x0,y0,x1,y1...x200,y200]]
    return y



# Main function
if __name__ == "__main__":
    if not isStart:
        print(">> Waiting 6 seconds for Arduino to set up...")
        time.sleep(6)
        isStart = True

    read_classify()

