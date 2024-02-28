#include <LapX9C10X.h>

#define SET(x,y) (x |=(1<<y))				        //-Bit set/clear macros
#define CLR(x,y) (x &= (~(1<<y)))       		    // |
#define TOG(x,y) (x^=(1<<y))            		    //-+


// Analog read voltage pins
#define point_freq A0  // Reading frequency
#define point_AB   A1  // Top bridge (Ra & Rb)
#define point_CD   A2  // Bottom bridge (Rv & Rd)


// Control LAPX9C10X_X9C103 (10k)
#define CS_R1    12
#define INC_R1   11
#define UDP_R1   10

#define CS_R2    7
#define INC_R2   6
#define UDP_R2   5

#define CS_R3    4
#define INC_R3   3
#define UDP_R3   2

LapX9C10X R1(INC_R1, UDP_R1, CS_R1, LAPX9C10X_X9C103);
LapX9C10X R2(INC_R2, UDP_R2, CS_R2, LAPX9C10X_X9C103);
LapX9C10X R3(INC_R3, UDP_R3, CS_R3, LAPX9C10X_X9C103);

#define numFreq  200 // Number of frequency being swept (Max at 200)

// Low-pass filter coefficients
float alpha = 0.5;  // You can adjust this value based on your filtering needs

// Declare int array as a data packets to be sent to serial
int data_array[numFreq + 3];

// External resitors used (kΩ)
float ext_res = 4.70;

// Voltage value of Top and Bottom bridge
float volt_AB = 0.00;
float volt_CD = 0.00;

// Volttage difference between AB and CD (error value)
float volt_diff = 0.00;

// Same as volt_diff
float error = 0.00;

// Set value using index position with lowest voltage difference
int set = 0;

// Store volt_diff in the array and use index as 'x'
float volt_array [100];

// Calibration button to balance the bridge to 2.5V
int cali_button = 13;
bool need_cali  = false;




void setup() {
  Serial.begin(115200);         // Setup baud rate

  TCCR1A = 0b10000010;          //-Set up frequency generator
  TCCR1B = 0b00011001;          //-+
  ICR1 = 110;                   //
  OCR1A = 55;                   //

  pinMode(9, OUTPUT);           //-Signal generator pin
  pinMode(8, OUTPUT);           //-Sync (test) pin
  pinMode(cali_button, INPUT);

  //Initialised 3 IC potentiometer
  R1.begin(-1);
  R2.begin(-1);
  R3.begin(-1);

  delay(5000);                  // Give time for IC to setup and ready
  SweepRes();                   // Calibrate the circuit first
}


void loop() {
  FreqSwept();         // Store capactive sensing values
  ReadResValue();      // Store resistive sensing values
  ReadButton();        // Read button state and flag when pressed

  // Serial write the int data_array
  Serial.write((uint8_t*)data_array, sizeof(data_array));

  // Can be from 50 to 250
  delay(100);

  if (need_cali) {     // Check whether the button is pressed or not
    SweepRes();        // Sweep resistance for calibration
  }
}


void FreqSwept() {
  // Adapt from https://github.com/Illutron/AdvancedTouchSensing/tree/master

  for (unsigned int freq = 0; freq <= numFreq + 1; freq++) {
    int v = analogRead(point_freq);   //-Read response signal
    CLR(TCCR1B, 0);                   //-Stop generator
    TCNT1 = 0;                        //-Reload new frequency
    ICR1 = freq;                      // |
    OCR1A = freq / 2;                 //-+
    SET(TCCR1B, 0);                   //-Restart generator

    // Simple Low-pass filter (LPF)
    float amplitude = amplitude * alpha + (float) (v) * alpha;

    // Round to int and store amplitude in array
    data_array[freq] = int(round(amplitude));

    // 0.001 sec delay
    delayMicroseconds(1);
  }
  // Add -100 for simple parity check
  data_array[numFreq + 1] = -100;

  //-Toggle pin 8 after each sweep (good for scope)
  TOG(PORTB,0);
}


void ReadResValue() {
  volt_AB = ReadVoltage(point_AB);
  volt_CD = ReadVoltage(point_CD);
  volt_diff = volt_CD - volt_AB;

  // Store resistance sensing value
  data_array[numFreq + 2] = int(volt_diff * 100);
  
  // 0.001 sec delay
  delayMicroseconds(1);
}


// Read the state of the button for calibration
void ReadButton() {
  if (digitalRead(cali_button) == HIGH) { // Check if the button is pressed
    need_cali = true;  // Set the boolean variable to true
    //Serial.println(">> Calibration in progress...");
    delay(250);
  }
}


// Read analog and convert into actual voltage value
float ReadVoltage(int pin) {
  int raw = analogRead(pin);
  float volt = raw * (5.0 / 1023.0);
  return volt;
}


// Sweep resistance to find lowest voltage difference and set that resitance to 3 IC.
void SweepRes() {
  for (int i = 0; i < 100; i++){
    // Increment resistance to 3 IC
    R3.set(i);
    R1.set(i);
    R2.set(i);

    // Read and find voltage difference
    volt_AB = ReadVoltage(point_AB);
    volt_CD = ReadVoltage(point_CD);
    volt_diff = fabs(volt_CD - volt_AB);
  
    // Store each voltage value in the array
    volt_array[i] = volt_diff;

    // 0.001 sec delay
    delayMicroseconds(1);
  }

  error = volt_array[0];                // Assume that 1st element is the lowest

  for (int j = 0; j < 100; j++) {
    if (volt_array[j] <= error) {       // If find lower voltage different then store its set value and error (volt difference)
      error = volt_array[j];
      set = j;
    }
  }

  // When find optimal, set it to 3 IC
  R3.set(set);
  R1.set(set);
  R2.set(set);

  // Flag back to false to stop calibration process
  need_cali = false;
}



