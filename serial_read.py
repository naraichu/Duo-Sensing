import serial
import numpy as np


# Specify the COM port and baud rate
com_port = 'COM12'    # Change this to the appropriate COM port
baud_rate = 115200    # Change this to the baud rate used by your Arduino

# Arrays for graph plotting
freq_array = np.zeros(200)
value_array = np.zeros(200)

# Flag boolean
isFreq = False


# Open the serial port
ser = serial.Serial(com_port, baud_rate, timeout = 1)

try:
    while True:
        # Read a line of data from the serial port as bytes
        data_bytes = ser.read()


        try:
            data_value = int.from_bytes(data_bytes, byteorder = 'little', signed = False)
            
            #if (isFreq):
                #freq_array
            print(data_value)
            
       

        except ValueError:
            # Handle the case where the received data is not a valid integer
            print("Invalid data received:", x_value)

except KeyboardInterrupt:
    # Close the serial port on KeyboardInterrupt (Ctrl+C)
    ser.close()
    print("Serial port closed.")