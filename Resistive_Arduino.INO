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
// Do I need this external resistors?
float ext_res = 4.7 + 10.0;

// Voltage value of Top and Bottom bridge
float volt_AB = 0.00;
float volt_CD = 0.00;

// Volttage difference between AB and CD
float volt_diff = 0.00;


// Calibration button to balance the bridge to 2.5V
int cali_button = 13;
bool need_cali  = false;


// Boolean flag when hit at 2.50V


void setup() {
  Serial.begin(115200);
  pinMode(cali_button, INPUT);

  Serial.println(">> Wait...");
  R1.begin(-1);
  delay(5000); // Give time for IC to setup and ready
  
  Serial.println("<<-- System is ready -->>");
}


float ReadVoltage(int pin) {
  int raw = analogRead(pin);
  float volt = raw * (5.0 / 1023.0);
  return volt;
}



void loop() {
  
  volt_AB = ReadVoltage(point_AB);
  volt_CD = ReadVoltage(point_CD);
  volt_diff = volt_AB - volt_CD;

  
  Serial.print(volt_AB);
  Serial.print("\t");
  Serial.print(volt_CD);
  Serial.print("\t");
  Serial.println(volt_diff);
  
  delay(50);

  //test();


}


void SweepRes() {
  // This sh*t needs to be more sophisticated
  for (int count = 0; count <= 100; count++) {
    float value = ReadVoltage(point_CD); // Read volatage in bottom 
    
    if (value == 2.50) {
      break;

      // Equalise the resistance in the bridge
      R1.set(count);
      R2.set(count);
      R3.set(count);

    }
    else {
      R3.set(count);
      continue;
    }
  }
}



void test() {
  for(int count1 = 0; count1 <= 100; count1++) {
    int read12 = analogRead(2);
    float voltage12 = read12 * (5.0 / 1023.0);
    R3.set(count1);

    Serial.print(count1); // Increment count
    Serial.print("\t");
    Serial.print(R1.getK() + ext_res); // Actual resistance value
    Serial.print("\t");
    Serial.println(voltage12);  // Actual volatage value
    delay(25);
  }
  Serial.println("_______________________________");
}






