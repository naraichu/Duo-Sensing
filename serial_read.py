import serial

ser = serial.Serial('COM12', 115200)  # Replace 'COMX' with the appropriate serial port on your computer

while True:
    # Read the first array
    data1 = ser.read(40)  # Assuming each integer is 2 bytes (int) and there are 5 elements in the array

    # Read the second array
    data2 = ser.read(40)  # Adjust the number based on the size of your second array

    '''
    // Each number in array is 32 bits or 4 bytes
    // Therefore array of 10 integer is 320 bits or 40 bytes

    int array1[] = {1,2,3,4,5,6,7,8,9,10};
    int array2[] = {10,20,30,40,50,60,70,80,90,100};
    '''

    # Convert the received bytes back to integers
    received_array1 = [int.from_bytes(data1[i:i+2], byteorder='little') for i in range(0, 20, 2)]
    received_array2 = [int.from_bytes(data2[i:i+2], byteorder='little') for i in range(20, 40, 2)]

    # Print the received arrays
    print("Received Array 1:", received_array1)
    print("Received Array 2:", received_array2)