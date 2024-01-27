import serial

array_len = 200
byte_len = (array_len + 2) * 2



ser = serial.Serial('COM12', 115200)  # Replace 'COMX' with the appropriate serial port on your computer


def read_serial_data():
    try:
        while True:
            # Read data from the serial port
            data = ser.read(byte_len)
            
            # Convert the received bytes back to signed integers
            array = [int.from_bytes(data[i:i+2], byteorder='little', signed = True) for i in range(0, byte_len, 2)]
            
            # Check if the data is correct
            if is_data_valid(array):
                array.pop()  # Remove -100 checker from the array
                print(array)
                print("\n")

            else:
                # Close and reopen the serial connection
                print("Invalid data")
                ser.close()
                ser.open()
              

    except KeyboardInterrupt:
        # Close the serial connection when the program is interrupted
        print("<-- Port closed -->")
        ser.close()


def is_data_valid(array):
    if ((array[array_len + 1] == -100) and (array_len + 2)):
        return True
    
    else:
        return False
        

if __name__ == "__main__":
    read_serial_data()




'''
// Successfully test against this Arduino code

// Adapt from https://github.com/Illutron/AdvancedTouchSensing/tree/master

#define SET(x,y) (x |=(1<<y))				//-Bit set/clear macros
#define CLR(x,y) (x &= (~(1<<y)))       		//-+
#define numFreq  200 // Number of frequency being swept (Max at 200)


// Low-pass filter coefficients
float alpha = 0.3;  // You can adjust this value based on your filtering needs


// Declare int array as a data packets to be sent to serial
// Each number in array is 32 bits or 4 bytes
//int freq_array[numFreq + 1];
int amplitude_array[numFreq + 2];


void setup() {
  TCCR1A = 0b10000010;        //-Set up frequency generator
  TCCR1B = 0b00011001;        //-+
  ICR1 = 110;                 //
  OCR1A = 55;                 //

  pinMode(9, OUTPUT);        //-Signal generator pin
  pinMode(8, OUTPUT);        //-Sync (test) pin

  pinMode(2, OUTPUT);        // LED pin for serial indication

  Serial.begin(115200);
}


void loop() {
  // Start data stream
  float amplitude;
  //float result;

  for (unsigned int freq = 0; freq <= numFreq + 1; freq++) {
    int v = analogRead(0);      //-Read response signal
    CLR(TCCR1B, 0);             //-Stop generator
    TCNT1 = 0;                  //-Reload new frequency
    ICR1 = freq;                // |
    OCR1A = freq / 2;           //-+
    SET(TCCR1B, 0);             //-Restart generator

    // Simple Low-pass filter
    amplitude = amplitude * alpha + (float) (v) * alpha;

    // Modified value to be smaller
    //amplitude = (amplitude * 0.8); // int round it

    //freq_array[freq] = freq;
    amplitude_array[freq] = int(round(amplitude));
    delayMicroseconds(5); // 0.005 sec
    
  }
  amplitude_array[numFreq + 1] = -100;
  // Serial.write((uint8_t*)freq_array, sizeof(freq_array));
  Serial.write((uint8_t*)amplitude_array, sizeof(amplitude_array));
  delay(200);

}
'''