import serial

ser = serial.Serial('COM12', 115200)  # Replace 'COMX' with the appropriate serial port on your computer



while True:
    # Read the first array
    data = ser.read(402)  # Each integer is 4 bytes or 8 bits

    # Convert the received bytes back to integers
    amp_array = [int.from_bytes(data[i:i+2], byteorder='little') for i in range(0, 402, 2)]

    # Print the received array
    print("Amplitude:", amp_array)