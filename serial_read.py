import serial
import numpy as np


# Input number of frequency being swept
array_len = 200

# Number of byte length to be decoded
# offset is 2 because for 0 and -100
byte_len = (array_len + 2) * 2


# Declare port number and baudrate
ser = serial.Serial('COM12', 115200)



def read_serial_data():
    try:
        while True:
            # Read data from the serial port
            data = ser.read(byte_len)
            
            # Convert the received bytes back to signed integers
            array = np.array([int.from_bytes(data[i:i+2], byteorder='little', signed=True) for i in range(0, byte_len, 2)])
            
            # Check if the data is correct
            if is_data_valid(array):
                array = np.delete(array, -1)  # Remove -100 (last value) from array

                # received_serial()

                # Output result
                print(array)
                print("\n")

            else:
                # Close and reopen the serial connection
                print(">> Invalid data")
                ser.close()
                ser.open()

    except KeyboardInterrupt:
        # Close the serial connection when the program is interrupted
        print("<-- Port closed -->")
        ser.close()


def is_data_valid(array):
    if array_len + 2 == len(array) and array[array_len + 1] == -100:
        return True
    else:
        return False


if __name__ == "__main__":
    read_serial_data()
