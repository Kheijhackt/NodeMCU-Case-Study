#include "ESPControl.h"

int ledPin[4] = {D2, D3, D4, D5};
int control = 0, counter = 0;
String path = "nothing";

void setup() {
  Serial.begin(9600);
  start("KJACT Smartbro", "bd8e4d538dfa993960152da646"); //EDIT
  for(int a = 0; a < 4; a++){
    pinMode(ledPin[a], OUTPUT);
  }
}

void loop()
{
  if (CheckNewReq() == 1)
  {
    path = getPath();
    path.remove(0, 1);
    control = path.toInt();
    digitalWrite(ledPin[counter], control);
    counter++;
    if(counter > 3){
       counter = 0;
    }
  }
}
