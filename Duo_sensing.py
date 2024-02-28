import serial
import numpy as np
import time

#NOTE
# This is the duo-sensing program to read value from both resisitive and capacitive sensing.


# Input number of frequency being swept
freq_len = 200

# Number of byte length to be decoded
# offset is 3 because for 0, -100 and resistive value
byte_len = (freq_len + 3) * 2

# Declare port number and baudrate
ser = serial.Serial('COM12', 115200)

# Flag when Arduino is ready
isStart = False



def read_serial():
    try:
        while True:
            data = ser.read(byte_len)

            all_array = np.array([int.from_bytes(data[i:i+2], byteorder = 'little', signed = True) for i in range(0, byte_len, 2)])

            # Check if the data is correct
            if is_data_valid(all_array):
                all_array = np.delete(all_array, -2)  # Remove -100 (last value) from all_array
                print(all_array)

            else:
                # Close and reopen the serial connection
                print(">> Invalid data")
                ser.close()
                ser.open()
                
                '''
                # Generate zero values of amplitude
                all_array = np.zeros(freq_len + 1, dtype = int)
                return all_array
                '''

    except KeyboardInterrupt():
        print("<-- Port closed -->")
        ser.close()



def is_data_valid(all_array):
    if freq_len + 3 == len(all_array) and all_array[freq_len + 1] == -100:
        return True
    else:
        return False

  

# Main function
if __name__ == "__main__":
    if (isStart):
        read_serial()
    else:
        print(">> Waiting 5 seconds for Arduino to setup...")
        time.sleep(6)
        isStart = True
        read_serial()
    