import serial

ser = serial.Serial('COM12', 115200)  # Replace 'COMx' with the actual port your Arduino is connected to

def read_float():
    while True:
        if ser.readable():
            try:
                data = ser.readline().decode().strip()
                if data.startswith('F') or data.startswith('V'):
                    return int(data[1:])
            except UnicodeDecodeError as e:
                print(f"Error decoding data: {e}")
                # Add additional handling if needed, such as clearing the serial buffer
                ser.reset_input_buffer()

try:
    while True:
        read_value = read_float()
        if read_value is not None:
            print("Value:", read_value)
            # Do something with the float value

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")