// This code has been adapt from https://github.com/Illutron/AdvancedTouchSensing/tree/master

#define SET(x,y) (x |=(1<<y))				//-Bit set/clear macros
#define CLR(x,y) (x &= (~(1<<y)))       		// |
#define TOG(x,y) (x^=(1<<y))            		//-+

#define numFreq  200 // Number of frequency being swept (Max at 200)


// Low-pass filter coefficients
float alpha = 0.5;  // You can adjust this value based on your filtering needs

// Declare int array as a data packets to be sent to serial
int amplitude_array[numFreq + 2];



void setup() {
  TCCR1A = 0b10000010;        //-Set up frequency generator
  TCCR1B = 0b00011001;        //-+
  ICR1 = 110;                 //
  OCR1A = 55;                 //

  pinMode(9, OUTPUT);         //-Signal generator pin
  pinMode(8, OUTPUT);         //-Sync (test) pin

  Serial.begin(115200);       // Setup baud rate
}


void loop() {
  for (unsigned int freq = 0; freq <= numFreq + 1; freq++) {
    int v = analogRead(0);      //-Read response signal
    CLR(TCCR1B, 0);             //-Stop generator
    TCNT1 = 0;                  //-Reload new frequency
    ICR1 = freq;                // |
    OCR1A = freq / 2;           //-+
    SET(TCCR1B, 0);             //-Restart generator

    // Simple Low-pass filter (LPF)
    float amplitude = amplitude * alpha + (float) (v) * alpha;

    // Round and cast amplitude float to integer and store in array
    amplitude_array[freq] = int(round(amplitude));

    // 0.005 sec delay
    delayMicroseconds(1);
  }

  // Add -100 for simple parity check
  amplitude_array[numFreq + 1] = -100;

  // Encode array into byte package for serial
  Serial.write((uint8_t*)amplitude_array, sizeof(amplitude_array));
  delay(250);

  TOG(PORTB,0);            //-Toggle pin 8 after each sweep (good for scope)
}
