#include <Arduino.h>
#define sleep delay

//initalize drums high, they "trigger" on low
int kick_val  = 1;
int tom1_val  = 1;
int tom2_val  = 1;
int tom3_val  = 1;
int crash_val = 1;
int ride_val  = 1;
int snare_val = 1;

void setup() {
  Serial.begin(9600);
  Serial.println("drumset_setup");
}

void loop() {
    /*7 drums,  basically im going to use the internal pullup of each digitalpin and 
    watch if the value goes low then send the character of the drum over serial to whatever
    eg k t1 t2 ...
    */

    //set internal pullups
    pinMode(2, INPUT_PULLUP);
    pinMode(3, INPUT_PULLUP);
    pinMode(4, INPUT_PULLUP);
    pinMode(5, INPUT_PULLUP);
    pinMode(6, INPUT_PULLUP);
    pinMode(7, INPUT_PULLUP);
    pinMode(8, INPUT_PULLUP);

    //read each pin and watch for LOW
    kick_val  = digitalRead(2);
    tom1_val  = digitalRead(3);
    tom2_val  = digitalRead(4);
    tom3_val  = digitalRead(5);
    crash_val = digitalRead(6);
    ride_val  = digitalRead(7);
    snare_val = digitalRead(8);


    //not optomized yet
    if (kick_val == 0){
      Serial.println('k');
      kick_val = 1; //reset each val 1 after sending the byte
    }
    if (tom1_val == 0){
      Serial.println('1');
      tom1_val = 1;
    }
    if (tom2_val == 0){
      Serial.println('2');
      tom2_val = 0;
    }
    if (tom3_val == 0){
      Serial.println('3');
      tom3_val = 0; 
    }
    if (crash_val == 0){
      Serial.println('c');
      crash_val = 0;
    }
    if (ride_val == 0){
      Serial.println('r');
      ride_val = 0;
    }
    if (snare_val == 0){
      Serial.println('s');
      snare_val = 0;
    }
    
    sleep(30);

}


