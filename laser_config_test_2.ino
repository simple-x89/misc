//case1: config matches
//case2: config mismatch
//case3: laser fault
//case4: no laser

char input;
String output;
char laserBuffer;
int ndx;
int configFlag;
int laserCheck;
const int laserID = 1;


void setup() {
  Serial.begin(9600);                            //computer
  Serial3.begin(9600);                           //laser
  ndx = 0;                                       //initialize ndx
  configFlag = 0;                                //initialize configFlag
  laserCheck = 0;                                //initialize laserCheck

}
void loop() {}                                   // place holder to keep compiler happy
void smartConfigCheck() {

  Serial3.print("v1234");                    //ask laser for config (P21 AR200 user manual)

  while (Serial3.available()) {                //if laser responds

    laserBuffer = Serial3.read();              //from laser

    if (ndx > 500) {                           //infite loop insurance
      laserFixer(output);
      ndx = 0;
    }

    if (laserBuffer == '\n') {                 //look for newline and reset output variable
      serialParse(output);
      output = "";

      if (configFlag == 1) {
        configFlag = 0;
      }

      if (configFlag == 2) {
        laserFixer(output);
        configFlag = 0;
      }

    }

    else {
      output += laserBuffer;                   //if no newline found, append output variable
    }

    ndx++;                                     //increment index var
  }


}


void serialParse(String serialIn) {

  String inputString, trimString;
  String configArray[] = {"0", "50000", "2000", "OFF", "ON", "OFF", "9600", "ASCII: ENGLISH", "QUALITY"};



  inputString = serialIn.substring(serialIn.indexOf(":") + 1);  //If no laser fault found, Parse input by ':' and remove spaces
  inputString.trim();

  for (int i = 0; i <= 8; i++) {

    if (i <= 1) {                                               //The first 2 items of a config print out are not relevant and are ignored.
      configFlag = 1;
    }

    if (inputString.equalsIgnoreCase(configArray[i])) {         //input matches item in configArray set configFlag to 1
      configFlag = 1;
    }

    else {
      configFlag = 2;                                           // no match with the config array found. set configFlag to 2
    }

  }
}

void laserFixer(String serialIn) {

  String inputString;
  String faultMessage = "SAVED CONFIGUATION INVALID. USING DEFAULT SETTINGS";
  String message;
  inputString = serialIn;
  inputString.trim();


  if (inputString.equalsIgnoreCase(faultMessage)) {              //Before parse check for fault message
    message = "Press function button for Laser " + laserID;
   // OledPrintWarning(message);

  }

  Serial3.print("p1");                                           // sample priority set to "QUALITY"
  Serial3.print("a1");                                           //units set to "ASCII: ENGLISH"
  Serial3.print("x5");                                           //turn off analog output
  Serial3.print("h2");                                           //turn laser off
  Serial.print("w1234");                                         //carefull!!
  configFlag = 0;                                                //reset configFlag
}


