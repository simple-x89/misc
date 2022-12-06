//------global var-------
char laserValue;


void setup() {
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);


  Serial1.begin(9600); //arduino
  Serial.begin(9600); //Laser
  Serial.print("p1"); // sample priority set to quality
  Serial.print("a1"); // units set to english
  Serial.print("x5"); //turn off analog signal
  Serial.print("h2"); // turn off laser
}


void loop() {
  while (Serial1.available() > 0) {
    
    Serial1.read();// clear serial1(arduino) rx buffer
    Serial.print("E"); //one shot laser fire
    Serial.flush(); // clear serial(laser) tx buffer
    goodVibes(); //indicate loop passed

    while (Serial.available() > 0 ) {
      laserValue = Serial.read();//read from laser RX buffer. also clears out one rx buffer byte. 8 total 
      Serial1.write(laserValue);//write to arduino tx buffer
      //Serial1.flush();//clear arduino tx buffer
      //badVibes(); //indicate loop passed
    }
    if (Serial1.available() == 0 ) {

      otherVibes(); //laser buffer empty
    }


  }
  
    allVibes();//looking/waiting for data in the arduino rx buffer 
  
}




//-------------functions-------------------------------------------------
void goodVibes() { //function to indicate good vibes
  for (int i = 0; i < 5; i++) {
    delay(75);
    digitalWrite(A0, HIGH);
    delay(150);
    digitalWrite(A0, LOW);
    delay(75);
  }
}

void badVibes() {
  for (int i = 0; i < 5; i++) {
    delay(75);
    digitalWrite(A2, HIGH);
    delay(150);
    digitalWrite(A2, LOW);
    delay(75);
  }
}

void otherVibes() {
  for (int i = 0; i < 5; i++) {
    delay(75);
    digitalWrite(A1, HIGH);
    delay(150);
    digitalWrite(A1, LOW);
    delay(75);
  }
}
void shortVibes() {
  for (int i = 0; i < 3; i++) {
    delay(25);
    digitalWrite(A0, HIGH);
    delay(50);
    digitalWrite(A0, LOW);
    delay(25);
  }
}
void allVibes() {
  for (int i = 0; i < 3; i++) {
    delay(20);
    digitalWrite(A0, HIGH);
    delay(40);
    digitalWrite(A1, HIGH);
    delay(40);
    digitalWrite(A2, HIGH);
    delay(60);
    digitalWrite(A0, LOW);
    delay(40);
    digitalWrite(A1, LOW);
    delay(40);
    digitalWrite(A2, LOW);
    delay(20);
  }
}



