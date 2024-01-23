import serial
import time

ser = serial.Serial('COM12', 115200, timeout=1)

def send_command(command):
    ser.write(command.encode('utf-8'))
    time.sleep(0.1)  # Allow time for the Arduino to process the command

def read_integer():
    while True:
        if ser.readable():
            try:
                data = ser.readline().decode(errors='replace').strip()
                if data.startswith('F') or data.startswith('V'):
                    return int(data[1:])
            except UnicodeDecodeError as e:
                print(f"Error decoding data: {e}")
                # Add additional handling if needed, such as clearing the serial buffer
                ser.reset_input_buffer()

try:
    # Send "START" command to Arduino to initiate data stream
    send_command("START")
    print("START sent")

    # Read data from Arduino
    while True:
        integer_value = read_integer()
        if integer_value is not None:
            print("Received integer value:", integer_value)
            # Do something with the integer value

except KeyboardInterrupt:
    # Send "STOP" command to Arduino to stop data stream
    send_command("STOP")
    ser.close()
    print("Serial connection closed.")
