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
float ext_res = 22.0;

// Voltage value of Top and Bottom bridge
float volt_AB = 0.00;
float volt_CD = 0.00;

// Volttage difference between AB and CD (error value)
float volt_diff = 0.00;

// Set value using index position with lowest voltage difference
int set_value = 50;

// Store volt_diff in the array and use index as 'count'
float volt_array [100+1];


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
  R1.set(set_value);
  R2.set(set_value);
  R3.set(set_value);
  
  Serial.println("<<-- System is ready -->>");
}


float ReadVoltage(int pin) {
  int raw = analogRead(pin);
  float volt = raw * (5.0 / 1023.0);
  return volt;
}



void loop() {
  // Display all of the results
  ShowValue();
  
  // Read button state and flag when pressed
  ReadButton();

  // If true then calibrate the process
  if (need_cali) {
    for(int count = 0; count <= 100; count++) {

      // Set same resistance value to 3 IC
      R1.set(count);
      R2.set(count);
      R3.set(count);

      volt_AB = ReadVoltage(point_AB);      // Reading voltage at point AB
      volt_CD = ReadVoltage(point_CD);      // Reading voltage at point CD
      volt_diff = fabs(volt_CD - volt_AB);  // Voltage different (error rate)


      volt_array[count] = volt_diff;        // Store voltage difference (error rate) in array
    }

    error = volt_array[0];                  // Assume that 1st element is the lowest

    for (int i = 0; i <= 100; i++) {        // Finding lowest error and set (index) values
      if (volt_array[i] < error) {
        error = fabs(volt_array[i]);        // Store lowest error rate
        set_value = i;                      // Store set value (index) of the lowest error rate
      }
    }
    // Set the new resistance
    R1.set(set_value);
    R2.set(set_value);
    R3.set(set_value);

    // Flag boolean back to stop calibration process
    need_cali = false;

    Serial.println(">> Calibration complete...");
  }
}


void ShowValue() {
  volt_AB = ReadVoltage(point_AB);      // Reading voltage at point AB
  volt_CD = ReadVoltage(point_CD);      // Reading voltage at point CD
  volt_diff = fabs(volt_CD - volt_AB);  // Voltage different (error rate)

  
  Serial.print(set_value);
  Serial.print("\t");

  Serial.print(R3.getK() + ext_res);
  Serial.print("\t");

  Serial.print(volt_AB);
  Serial.print("\t");

  Serial.print(volt_CD);
  Serial.print("\t");
  
  Serial.println(fabs(volt_diff - error));
  delay(50);
}


void ReadButton() {
  // Check if the button is pressed
  if (digitalRead(cali_button) == HIGH) {
    need_cali = true;  // Set the boolean variable to true
    Serial.println(">> Calibration in progress...");
    delay(250);
  }
}






