import serial
from time  import  sleep
ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=1,
                     xonxoff=0,
                     rtscts=0
                     )
counter = 0
print(ser.name)
while True:
     counter +=1
     ser.write(b'1') # Convert the decimal number to ASCII then send it to the Arduino
     print(ser.readline()) # Read the newest output from the Arduino
     # Delay for one tenth of a second
     print('yesss')
     if counter == 255:

        with ser:  # the reset part is actually optional but the sleep is nice to have either way.
            ser.setDTR(False)
            sleep(1)
            ser.flushInput()
            ser.setDTR(True)
            print('py', counter)
        #ser.close()


"""
Import serial

arduino = serial.Serial('/dev/ttyS0',
                     baudrate=9600,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=1,
                     xonxoff=0,
                     rtscts=0
                     )
# Toggle DTR to reset Arduino
arduino.setDTR(False)
sleep(1)
# toss any data already received, see
# http://pyserial.sourceforge.net/pyserial_api.html#serial.Serial.flushInput
arduino.flushInput()
arduino.setDTR(True)

with arduino:
    while True:
        print(arduino.readline())
I would also add the compliment to the DTR for the Arduino's with AVR's using built-in USB, such as the Leonoardo, Esplora and alike. The setup() should have the following while, to wait for the USB to be opened by the Host.

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
}"""
# cod  arduino
"""int reli1 = 2;
int reli2 = 3;
int reli3 = 4;


// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  Serial.begin(9600); // set the baud rate
  pinMode(reli1, OUTPUT);    
  pinMode(reli2, OUTPUT);  
  pinMode(reli3, OUTPUT);   
}

// the loop routine runs over and over again forever:
void loop() {
//digitalWrite(reli3, HIGH);
if (Serial.available())

{

char state = Serial.read(); 

//Serial.println(state);
if (state == '1')

{

digitalWrite(reli1, HIGH);

//Serial.println("reli1 on");

}

if (state == '2')

{

digitalWrite(reli2, HIGH);

//Serial.println("reli 2 on ");

}
if (state == '3')

{

digitalWrite(reli3, HIGH);

//Serial.println("reli 3 on  ");

}

}
delay(100);
}"""