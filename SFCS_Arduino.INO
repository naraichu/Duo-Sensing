// Adapt from https://github.com/Illutron/AdvancedTouchSensing/tree/master

#define SET(x,y) (x |=(1<<y))				//-Bit set/clear macros
#define CLR(x,y) (x &= (~(1<<y)))       		//-+

float amplitude;
float result;
float freq;
int sizeOfArray = 190;  // Maximum at 200

int cmd = 0;

// Low-pass filter coefficients
float alpha = 0.5;  // You can adjust this value based on your filtering needs

// Each number in array is 32 bits or 4 bytes
// Therefore array of 10 integer is 320 bits or 40 bytes
int array1[] = {1,2,3,4,5,6,7,8,9,10};
int array2[] = {10,20,30,40,50,60,70,80,90,100};


void setup() {
  Serial.begin(115200);
}

void loop() {
  // Send the first array
  Serial.write((uint8_t*)array1, sizeof(array1));

  // Send the second array
  Serial.write((uint8_t*)array2, sizeof(array2));
  delay(100); // Add a delay to avoid flooding the serial port
}



/*
void setup() {
  TCCR1A = 0b10000010;        //-Set up frequency generator (130)
  TCCR1B = 0b00011001;        //-+ (25)
  ICR1 = 110;                 //
  OCR1A = 55;                 //

  pinMode(9, OUTPUT);        //-Signal generator pin
  pinMode(8, OUTPUT);        //-Sync (test) pin

  pinMode(2, OUTPUT);        // LED pin for serial indication

  Serial.begin(115200);
}


void loop() {
  // Start data stream
  unsigned int freq;
  for (unsigned int freq = 0; freq <= sizeOfArray; freq++) {
    int v = analogRead(0);      //-Read response signal
    CLR(TCCR1B, 0);             //-Stop generator
    TCNT1 = 0;                  //-Reload new frequency
    ICR1 = freq;                // |
    OCR1A = freq / 2;           //-+
    SET(TCCR1B, 0);             //-Restart generator

    // Simple Low-pass filter
    amplitude = amplitude * alpha + (float) (v) * alpha;

    // Make value larger by 10^2
    result = (amplitude / 2.0);

    Serial.print(int(freq));
    Serial.print(",");
    Serial.println(int(round(result)));
    //Serial.println(int(round(amplitude)));

    delayMicroseconds(5); // 0.005 sec
  }
}
*/
/*
void loop() {
  while (Serial.available() > 0) {
    cmd = Serial.read();

    if (cmd == "START") {
      digitalWrite(2, HIGH);
    }
    if (cmd == "END") {
      digitalWrite(2, LOW);
    }

  }
}*/

