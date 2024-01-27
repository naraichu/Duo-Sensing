// Adapt from https://github.com/Illutron/AdvancedTouchSensing/tree/master

#define SET(x,y) (x |=(1<<y))				//-Bit set/clear macros
#define CLR(x,y) (x &= (~(1<<y)))       		//-+
#define numFreq  200 // Number of frequency being swept (Max at 200)


// Low-pass filter coefficients
float alpha = 0.5;  // You can adjust this value based on your filtering needs


// Declare int array as a data packets to be sent to serial
// Each number in array is 32 bits or 4 bytes
int freq_array[numFreq + 1];
int amplitude_array[numFreq + 1];


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
  float result;

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
    result = (amplitude * 0.5); // int round it

    freq_array[freq] = freq;
    amplitude_array[freq] = int(round(result));
    delayMicroseconds(5); // 0.005 sec

    // Display value in Arduino
    /*
    Serial.print(int(freq));
    Serial.print(",");
    Serial.println(int(round(result)));
    //Serial.println(int(round(amplitude)));
    */
  }
  Serial.write((uint8_t*)amplitude_array, sizeof(amplitude_array));
  delay(1000);

}

