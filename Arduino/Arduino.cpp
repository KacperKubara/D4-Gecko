/*
 * Version notes: version 2.5.1 impliments accelerometer functionality
 * 
 * 
 */


#include <EEPROM.h>
#include <Wire.h>

#include <Adafruit_MMA8451.h>
#include <Adafruit_Sensor.h>

Adafruit_MMA8451 mma = Adafruit_MMA8451();

char serIn;   //character stores input from serial (i.e pi)
bool sendReads;   //used to decide if adc values should be sent to pi


// assigns pins used by adc

const int sensorPin0 = A0; 
const int sensorPin1 = A1;
const int sensorPin2 = A2;
const int sensorPin3 = A3; 
const int sensorPin4 = A4;
const int sensorPin5 = A5;
 
const int sensorPins[] = {A0, A1, A2, A3, A4, A5};

float offset[3];
float idealRead[3];


bool state;


volatile bool shot_fired;   //boolean changed by microphone

volatile bool accelerometer_enabled = false;


const byte interruptPin = 2; // assigns pin conected to microphone for external interupt


//function protyping

void start_data();
void stop_data();

void reset();
void configure_sensors(int sensorNumber, float newOffset);



void setup() {

  setUpADC();
  
  //interupt pin defaults to logic high
  pinMode(interruptPin, INPUT);
  
  //extrernal interput assigned, triggered on rising edge
  attachInterrupt(0, pin_ISR, RISING);

  //led enabled
  pinMode(LED_BUILTIN, OUTPUT);

  //opens serial coms with baud rate of 9600
  
  Serial.begin(9600);

  //led on
  digitalWrite(LED_BUILTIN, HIGH);

}


void setUpADC(){

  mma.begin();
  mma.setRange(MMA8451_RANGE_2_G);
  
}

void loop() {

  
  digitalWrite(LED_BUILTIN, state);

  
  // checks buffer for new recieved data and reads if available
  if (Serial.available() > 0) {
    serIn = Serial.read();


    //calls correct function corresponding to recieved signal
    switch (serIn) {
    case 'A':
      start_data();
      break;
    case 'B':
      stop_data();
      break;
    case 'C':
      reset();
      break;
    case 'D':
      configure_sensors(1,1);
      break;
    }
  }

  // checks state of sendReads to determine if pi wants values
  if (sendReads) {

    sendData();    
  }
}

void start_data() {
  sendReads = true;
  blink();

}

void stop_data() {

  //stop sending data

  sendReads = false;
  blink();
}

void reset() {
  // reset
  blink();

  //  clears  EEPPROM
  for (int i = 0 ; i < EEPROM.length() ; i++) {
    EEPROM.write(i, 0);
  }
  
}

void calibrate(int sensorNumber){
  float actual;
  float newOffset;
  
  actual = readSensorData(sensorNumber);

  newOffset = idealRead[sensorNumber] - actual;
  
}

void runDebugConfig(){

  
  Serial.println("current offset = " + String(offset[1]));
  String newOffset;
  int address = 0;
  bool recieved = false;
  
    Serial.println(recieved);
  while(!recieved){
    if (Serial.available() > 0) {
      offset[1] = Serial.read();
      recieved = true;
    }
  }

  EEPROM.put(address, offset);
  Serial.println("RECIEVED");
  

  
}

void configure_sensors(int sensorNumber, float newOffset) {

  offset[sensorNumber] = newOffset;
  
}

void updateIdealReadValues(int sensorNumber, float newIdeal){

  idealRead[sensorNumber] = newIdeal;
  
}

int getXYtilt(){

  int tilt;

  mma.read();
  sensors_event_t event; 
  mma.getEvent(&event);


  return tilt;
}


int getYZtilt(){

  int tilt;

  mma.read();
  sensors_event_t event; 
  mma.getEvent(&event);


  return tilt;
}

int getXZtilt(){

  int tilt;

  mma.read();
  sensors_event_t event; 
  mma.getEvent(&event);



  return tilt;
}

void initialise(){

  int address = 0;

  //EEPROM.get(address, offset);

  
  
}

int readSensorData(int sensorNumber){

  int posDiff;
  int negDiff;
  float posDiffVolt;
  float negDiffVolt;
  int debug;
  float output = 0;
  float difference;
    
  negDiff = analogRead(sensorPins[(2 * sensorNumber)]);
  posDiff = analogRead(sensorPins[(2 * sensorNumber) + 1]);
  debug = analogRead(A0);

  negDiffVolt = voltage(negDiff);
  posDiffVolt = voltage(posDiff);
  
  difference = posDiffVolt - negDiffVolt;

  if (difference = 0){

    difference = 0.01;
    
  }
  output = negDiffVolt/difference;

  //Serial.println(debug);
  //Serial.println(String(negDiffVolt) + ' ' + String(posDiffVolt)  + ' ' + String(output));
  return output;

}

void sendData() {

  
 // variables to store the value read
  int values[3];

  String out = "";

  mma.read();
  sensors_event_t event; 
  mma.getEvent(&event);
  // reads each value from adc

  //Serial.println(String(readSensorData(0)));
  
 
 for (int i = 0; i < 3; i++){

    out = out + ',' + String(readSensorData(i));
    
  
 }

 out = out + "," + String(event.acceleration.x) + "," + String(event.acceleration.y) + "," + String(event.acceleration.z);
  

 

  // outputs concatanation off all values plus microphone state

 out = shot_fired + out;  
 Serial.println(out);

  //returns to false after sent
  shot_fired = false;
 
  // long delay for debuging purposes (I cant read more than 2 values a second)
  delay(500);

}


//blinks led once in responce to recieving comands for debugging purposes
void blink(){

digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);
  
}

float voltage(int value){

    float voltage = 0;

    voltage = (float(value)/1023) * 5;
    
    return voltage;
  
 }




//interupt service routine for microphone circuit
void pin_ISR() {

      shot_fired = true;

}

