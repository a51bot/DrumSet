/*
This code is not mine but it has been edited.  So credit goes where credit due
https://blog.eikeland.se/2015/04/24/banana-piano/

*/



const int PORTS[8] = { 2, 3, 4, 5, 6, 7, 8, 9 };
const int THRESHOLDS[8] = { 13, 13, 13, 13, 13, 13, 13, 13 };

bool touched[8];

uint8_t readCapacitivePin(int pinToMeasure) {
  volatile uint8_t* port;
  volatile uint8_t* ddr;
  volatile uint8_t* pin;
  byte bitmask;

  port = portOutputRegister(digitalPinToPort(pinToMeasure));
  ddr = portModeRegister(digitalPinToPort(pinToMeasure));
  bitmask = digitalPinToBitMask(pinToMeasure);
  pin = portInputRegister(digitalPinToPort(pinToMeasure));

  // Discharge the pin first by setting it low and output
  *port &= ~(bitmask);
  *ddr  |= bitmask;
  delay(1);

  // Prevent the timer IRQ from disturbing our measurement
  noInterrupts();

  // Make the pin an input with the internal pull-up on
  *ddr &= ~(bitmask);
  *port |= bitmask;

  // Now see how long the pin to get pulled up. This manual unrolling of the loop
  // decreases the number of hardware cycles between each read of the pin,
  // thus increasing sensitivity.

  uint8_t cycles = 17;
       if (*pin & bitmask) { cycles =  0;}
  else if (*pin & bitmask) { cycles =  1;}
  else if (*pin & bitmask) { cycles =  2;}
  else if (*pin & bitmask) { cycles =  3;}
  else if (*pin & bitmask) { cycles =  4;}
  else if (*pin & bitmask) { cycles =  5;}
  else if (*pin & bitmask) { cycles =  6;}
  else if (*pin & bitmask) { cycles =  7;}
  else if (*pin & bitmask) { cycles =  8;}
  else if (*pin & bitmask) { cycles =  9;}
  else if (*pin & bitmask) { cycles = 10;}
  else if (*pin & bitmask) { cycles = 11;}
  else if (*pin & bitmask) { cycles = 12;}
  else if (*pin & bitmask) { cycles = 13;}
  else if (*pin & bitmask) { cycles = 14;}
  else if (*pin & bitmask) { cycles = 15;}
  else if (*pin & bitmask) { cycles = 16;}

  // End of timing-critical section
  interrupts();

  // Discharge the pin again by setting it low and output
  *port &= ~(bitmask);
  *ddr  |= bitmask;

  return cycles;
}

void setup() {
  Serial.begin(9600);
}

void handlePort(int index) {
  int cycles = readCapacitivePin(PORTS[index]);

  if (!touched[index] && cycles >= THRESHOLDS[index]) {
    touched[index] = true;

    //mapping the characters to pins
    char c = ' ';
    switch(index){
      case 0:
          c = 'k';
          break;
      case 1:
          c = '1';
          break;
      case 2:
          c = '2';
          break;
      case 3:
          c = '3';
          break;
      case 4:
          c = 'c';
          break;
      case 5:
          c = 'r';
          break;
      case 6:
          c = 's';
          break;
      case 7: //isnt need swap out with whatever
          c = 'k';
          break;

    }



    Serial.println(c);
  }

  if (touched[index] && cycles < THRESHOLDS[index]) {
    touched[index] = false;
  }
}

void loop() {
  for (int i = 0; i < 8; i++) {
    handlePort(i);
  }
  delay(25); // cheap-ass debounce..
}
