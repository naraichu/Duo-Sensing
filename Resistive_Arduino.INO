/*
For experimentation
Calibrate value to 0 is not good as the sensitive value drops
*/


#include <LapX9C10X.h>

// Analog read voltage pins
#define point_AB   A1  // Top bridge (Ra & Rb)
#define point_CD   A2  // Bottom bridge (Rv & Rd)


// Control LAPX9C10X_X9C103 (10k)
#define CS_R1    12
#define INC_R1   11
#define UDP_R1   10

#define CS_R2    8
#define INC_R2   7
#define UDP_R2   6

#define CS_R3    5
#define INC_R3   4
#define UDP_R3   3

LapX9C10X R1(INC_R1, UDP_R1, CS_R1, LAPX9C10X_X9C103);
LapX9C10X R2(INC_R2, UDP_R2, CS_R2, LAPX9C10X_X9C103);
LapX9C10X R3(INC_R3, UDP_R3, CS_R3, LAPX9C10X_X9C103);

// External resitors used (kΩ)
float ext_res = 22.0 + 10.0;

// Voltage value of Top and Bottom bridge
float volt_AB = 0.00;
float volt_CD = 0.00;

// Volttage difference between AB and CD (error value)
float volt_diff = 0.00;

// Same as volt_diff
float error = 0.00;

// Voltage value of bending;
float bend =  0.00;

// Set value using index position with lowest voltage difference
int set = 60;

// Store volt_diff in the array and use index as 'x'
float volt_array [101];


// Calibration button to balance the bridge to 2.5V
int cali_button = 13;
bool need_cali  = false;



void setup() {
  Serial.begin(115200);
  pinMode(cali_button, INPUT);

  Serial.println(">> Wait...");

  R1.begin(-1);
  R2.begin(-1);
  R3.begin(-1);

  delay(5000); // Give time for IC to setup and ready

  // Initilised IC with preset value
  R1.set(set);
  R2.set(set);
  R3.set(set);
  
  Serial.println("<<-- System is ready -->>");
}


void ReadButton() {
  // Check if the button is pressed
  if (digitalRead(cali_button) == HIGH) {
    need_cali = true;  // Set the boolean variable to true
    Serial.println(">> Calibration in progress...");
    delay(250);
  }
}


float ReadVoltage(int pin) {
  int raw = analogRead(pin);
  float volt = raw * (5.0 / 1023.0);
  return volt;
}



void loop() {
  ShowValue();         // Display all of the results
  ReadButton();        // Read button state and flag when pressed

  if (need_cali) {
    Serial.println(">> Calibrating now...");
    SweepRes();
  }
}


void ShowValue() {
  volt_AB = ReadVoltage(point_AB);
  volt_CD = ReadVoltage(point_CD);
  volt_diff = fabs(volt_CD - volt_AB);

  bend = fabs(volt_diff - error);

  Serial.print(set);
  Serial.print("\t");
  Serial.print(volt_AB);
  Serial.print("\t");
  Serial.print(volt_CD);
  Serial.print("\t");
  Serial.print(bend);
  Serial.println("\t");
  delay(50);
}



void SweepRes() {
  for (int i = 0; i <= 100; i++){
    R1.set(i);
    R2.set(i);
    R3.set(i);

    volt_AB = ReadVoltage(point_AB);
    volt_CD = ReadVoltage(point_CD);
    volt_diff = fabs(volt_CD - volt_AB);

    Serial.print(i);
    Serial.print("\t");
    Serial.print(volt_AB);
    Serial.print("\t");
    Serial.print(volt_CD);
    Serial.print("\t");
    Serial.print(volt_diff);
    Serial.println("\t");
    delay(10);

    volt_array[i] = volt_diff;

  }

  error = volt_array[0];

  for (int j = 0; j <= 100; j++) {
    if (volt_array[j] <= error) {
      error = volt_array[j];
      set = j;
    }
  }

  R1.set(set);
  R2.set(set);
  R3.set(set);

  need_cali = false;

  Serial.print(">> Lowest: ");
  Serial.print(set);
  Serial.print("\t");
  Serial.println(error);
  Serial.println("___________________________________");
}
