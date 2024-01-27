import serial

array_len = 200
byte_len = (array_len + 2) * 2



ser = serial.Serial('COM12', 115200)  # Replace 'COMX' with the appropriate serial port on your computer

while True:
    # Read the first array
    data = ser.read(byte_len)  # Each integer is 2 bytes or 16 bits

    # Convert the received bytes back to signed integers
    amp_array = [int.from_bytes(data[i:i+2], byteorder='little', signed = True) for i in range(0, byte_len, 2)]

    # Print the received array
    print("Data:", amp_array)
    print("Length: ", len(amp_array))
    print("\n")


'''
// Arduino code that is used to test against successfully
#define length 200

int array[length + 2];


void setup() {
  Serial.begin(115200);
}

void loop() {
  for (int i = 0; i <= length; i++) {
    array[i] = i;
    //Serial.println(i);
  }
  array[length + 1] = -100;
  Serial.write((uint8_t*)array, sizeof(array));
  /*
  Serial.println(-100);
  Serial.println("_______________________");
  */
  
  delay(100);
}
'''