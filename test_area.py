import serial
import struct
import numpy as np

'''
Read data from Duo-sensing
'''


data_len = 200

byte_len = (data_len + 3) * 2

ser = serial.Serial('COM12', 115200)


def read_serial_data():
    # Read data from the serial port
    data = ser.read(byte_len)
    
    # Convert the received bytes back to floats
    all_array = np.array([struct.unpack('f', data[i:i+4])[0] for i in range(0, byte_len, 4)])
    
    # Check if the data is correct
    if is_data_valid(all_array):
        all_array = np.delete(all_array, -2)  # Remove -100 from all_array
        print(all_array)
    
    else:
        # Close and reopen the serial connection
        print(">> Invalid data")
        ser.close()
        ser.open()



def is_data_valid(all_array):
    if data_len + 3 == len(all_array) and all_array[data_len + 1] == -100.0:
        return True
    else:
        return False


if __name__ == "__main__":
    read_serial_data()