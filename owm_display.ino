/*
        Код ужасный, сам знаю )))
*/

#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <string.h>

uint8_t deg[8]  = {0xC, 0xC, 0x0, 0x0, 0x0, 0x0, 0x0};
uint8_t heart[8] = {0x0, 0xa, 0x1f, 0x1f, 0xe, 0x4, 0x0};
uint8_t left_top[8] =     { };

uint32_t previousMillis = 0;
uint32_t tMillis = 0;
uint8_t val = 0;

String inputString = "";         // a string to hold incoming data

char buffer[32];
String temp = "";
String wind = "";
String winddir = "";
String hum = "";
boolean stringComplete = false;  // whether the string is complete


LiquidCrystal_I2C lcd(0x3F, 16, 2);

void setup()
{
  lcd.begin();
  lcd.backlight();

  lcd.createChar(0, deg);
  lcd.createChar(1, heart);
  lcd.createChar(2, left_top);

  lcd.home();

  Serial.begin(9600);
  inputString.reserve(200);

  displayLoading();
}


void displayLoading(void) {
  lcd.clear();
  lcd.print("Loading");
  delay(100);

  for (uint8_t k = 0; k <= 7; k++) {
      lcd.print(".");
      delay(100);
  }

  delay(500);
  lcd.clear();

}

void loop()
{

  if (stringComplete) {

    inputString.toCharArray(buffer,32);
    temp=atoi(strtok(buffer," "));
    wind=atoi(strtok(NULL," "));
    winddir=atoi(strtok(NULL," "));
    hum=atoi(strtok(NULL," "));

    lcd.clear();
    lcd.print(temp);
    lcd.write(0);
    lcd.print("C   ");
    lcd.print(wind);
    lcd.print(" m/s");
    lcd.setCursor(0, 1);
    lcd.print("H: ");
    lcd.print(hum);
    lcd.print("% ");
    lcd.print(" D: ");
    lcd.print(winddir);

    inputString = "";
    stringComplete = false;

    }
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
