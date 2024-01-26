import serial
import time


ser = serial.Serial('COM12', 115200, timeout = 1)  # Replace 'COMx' with the actual port your Arduino is connected to


try:
    time.sleep(1)
    while True:
        # Check if there is data available in the input buffer
        if ser.in_waiting > 0:
            # Read the data from the serial port
            data = ser.readline().decode(encoding = "utf-8").strip()
            
            # Process or print the received data
            print("Received data:", data)
        
        # Add a small delay to avoid high CPU usage
        time.sleep(0.005)

except KeyboardInterrupt:
    # Close the serial port on program exit
    ser.close()
    print("Serial port closed.")



'''
def read_serial():
    while True:
        if ser.readable():
            try:
                time.sleep(0.001)
                data = ser.readline().decode(encoding= "utf-8").strip()
                return data

            except UnicodeDecodeError as e:
                print(f"Error decoding data: {e}")
                # Add additional handling if needed, such as clearing the serial buffer
                ser.reset_input_buffer()

try:
    while True:
        read_value = read_serial()
        if read_value is not None:
            print(read_value)
            #print("Value:", read_value)
            # Do something with the float value

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")
'''

'''
ser = serial.Serial("COM12", 115200)

while True:
    ser.write(1.encode())
    time.sleep(1)
    ser.write("END".encode())
    time.sleep(1)
'''