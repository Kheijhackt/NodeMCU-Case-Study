#include "ESP_MICRO.h"

int buttonPin[4] = {D1, D2, D3, D4};
bool buttonState[4] = {false, false, false, false};
String signals;

void setup()

{
  Serial.begin(9600);
  start("KJACT Smartbro", "bd8e4d538dfa993960152da646");
  for(int a = 0; a < 4; a++){
    pinMode(buttonPin[a], INPUT_PULLUP); 
  }
}

void loop()

{
  waitUntilNewReq(); //Waits until a new request from python come 
  for(int a = 0; a < 4; a++){
    if(digitalRead(buttonPin[a]) == LOW){
      buttonState[a] = !buttonState[a];
      delay(200);
    }
  }
  signals = (String)buttonState[0] + "|" + (String)buttonState[1] + "|" + (String)buttonState[2] + "|" + (String)buttonState[3];
  Serial.println(signals);
  returnThisStr(signals);
}
