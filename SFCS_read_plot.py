import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# NOTE
# Adjust potentiometer on the circuit to reduce input signal from 5.12V to 3.00V


# Input number of frequency being swept
freq_len = 200

# Number of byte length to be decoded
# offset is 2 because for 0 and -100
byte_len = (freq_len + 2) * 2

# Declare port number and baudrate
ser = serial.Serial('COM14', 115200)

# Generate frequency array (+1 because of 0)
x_axis = np.arange(freq_len + 1)



# Initialise matplotlib
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o', markersize = 1)  # Initialize an empty line
ax.set(xlim = [0, freq_len + 1], ylim = [0, 1100], xlabel = 'Frequency', ylabel = 'Amplitude')



def read_serial_data():
    try:
        while True:
            # Read data from the serial port
            data = ser.read(byte_len)
            
            # Convert the received bytes back to signed integers
            y_axis = np.array([int.from_bytes(data[i:i+2], byteorder = 'little', signed = True) for i in range(0, byte_len, 2)])
            
            # Check if the data is correct
            if is_data_valid(y_axis):
                y_axis = np.delete(y_axis, -1)  # Remove -100 (last value) from y_axis
                return y_axis

            else:
                # Close and reopen the serial connection
                print(">> Invalid data")
                ser.close()
                ser.open()

                '''
                May want to change by sending the previous valid y_axis
                '''
                
                # Generate zero values of amplitude
                y_axis = np.zeros(freq_len + 1, dtype = int)
                return y_axis


    except KeyboardInterrupt:
        # Close the serial connection when the program is interrupted
        print("<-- Port closed -->")
        ser.close()


def is_data_valid(y_axis):
    if freq_len + 2 == len(y_axis) and y_axis[freq_len + 1] == -100:
        return True
    else:
        return False


def update(frame):
    line.set_ydata(read_serial_data())
    return line,


if __name__ == "__main__":
    line, = ax.plot(x_axis, read_serial_data())
    ani = FuncAnimation(fig, update, frames = None, interval = 200, cache_frame_data = False)

    # Show the plot
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.title('Swept Frequency Capacitive Sensing')
    plt.show()



'''
// This is the version that works successfully with Python


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
'''