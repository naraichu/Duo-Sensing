import serial as s

# Replace 'COM3' with the actual serial port your Arduino is connected to
serial_port = 'COM12'

# Replace 9600 with the baud rate your Arduino is using
baud_rate = 9600

# Open the serial port
ser = s.Serial(serial_port, baud_rate)

try:
    while True:
        # Read a line from the serial port and decode it
        line = ser.readline()

        # Print the received data
        print(line)

except KeyboardInterrupt:
    # Close the serial port when the script is interrupted (Ctrl+C)
    ser.close()






'''
# Credit from https://www.youtube.com/watch?v=PFPwcolQho0&t=743s

from typing import List, Tuple
import serial as s

ARRAY_SIZE = 160

def get_from_serial(port: s.Serial) -> Tuple[List, List]:
    x_axis = []
    y_axis = []
    flag = 0
    n = 0
    
    while True:
        dat = port.read(1).hex()
        if dat == "00":
            n += 1
            ar = []
            for j in range(7):
                ar.append(port.read(1).hex())
            e = int(ar[6], base = 16)

            # Check for command word
            cmd = int(ar[0], base = 16)

            if (cmd == 2):
                print("Start of array")
                x_axis = []
                y_axis = []
                flag = 1
                continue
            
            elif (cmd == 3):
                print("End of array")
                if flag == 1:
                    return (x_axis, y_axis)

            # Run checksum by adding all the bytes except the checksum
            check_sum = sum([int(d, base =16) for d in ar[0:6]]) % 255

            # If the checksums do not match then exit
            if check_sum != e:
                print(">> Checksum Error: ", check_sum)
                flag = 0
                continue

            z = int(ar[5], base = 16)

            # Parsing the zero byte and updating zeroes
            if (z & 1 != 0):
                ar[2] = "00"
            if (z & 2 != 0):
                ar[1] = "00"
            if (z & 4 != 0):
                ar[4] = "00"
            if (z & 8 != 0):
                ar[3] = "00"

            y = int(ar[1] + ar[2], base = 16)
            x = int(ar[3] + ar[4], base = 16)
            x_axis.append(x)
            y_axis.append(y)


if __name__ == "__main__":
    port = s.Serial("COM12", 115200)
    print(get_from_serial(port))
'''