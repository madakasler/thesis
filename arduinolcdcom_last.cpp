/*
  LiquidCrystal Library - Hello World

 Demonstrates the use a 16x2 LCD display.  The LiquidCrystal
 library works with all LCD displays that are compatible with the
 Hitachi HD44780 driver. There are many of them out there, and you
 can usually tell them by the 16-pin interface.

 This sketch prints "Hello World!" to the LCD
 and shows the time.

  The circuit:
 * LCD RS pin to digital pin 12
 * LCD Enable pin to digital pin 11
 * LCD D4 pin to digital pin 5
 * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin to digital pin 2
 * LCD R/W pin to ground
 * LCD VSS pin to ground
 * LCD VCC pin to 5V
 * 10K resistor:
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)

 Library originally added 18 Apr 2008
 by David A. Mellis
 library modified 5 Jul 2009
 by Limor Fried (http://www.ladyada.net)
 example added 9 Jul 2009
 by Tom Igoe
 modified 22 Nov 2010
 by Tom Igoe
 modified 7 Nov 2016
 by Arturo Guadalupi

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/LiquidCrystalHelloWorld

*/

// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(11,12,13,3,4,5,6,7,8,9,10);
unsigned buttonCounter = 0;
unsigned buttonStartTime = 0;
int buttonState = 0;  
int setButton = LOW;
int lastButtonState = 0;
 // variable for reading the pushbutton status
bool firstPress = true;
const int buttonPin = 2;  // the number of the pushbutton pin
   // the number of the LED pin

void setup() {
   Serial.begin(9600);
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
    pinMode(buttonPin, INPUT);
  // Print a message to the LCD.
  //lcd.print("hello, world!");
}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):

  // print the number of seconds since reset:

   if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    String data1 = Serial.readStringUntil('\n');
    String data2 = Serial.readStringUntil('\n');
    String data3 = Serial.readStringUntil('\n');
    String data4 = Serial.readStringUntil('\n');
    String data5 = Serial.readStringUntil('\n');
    String data6 = Serial.readStringUntil('\n');
    String data7 = Serial.readStringUntil('\n');
    String data8 = Serial.readStringUntil('\n');
    String data9 = Serial.readStringUntil('\n');
    String data10 = Serial.readStringUntil('\n');
    String data11 = Serial.readStringUntil('\n');
    String data12 = Serial.readStringUntil('\n');
    String data13 = Serial.readStringUntil('\n');
    String data14 = Serial.readStringUntil('\n');
    String data15 = Serial.readStringUntil('\n');
    String data16 = Serial.readStringUntil('\n');
    String data17 = Serial.readStringUntil('\n');
    String data18 = Serial.readStringUntil('\n');
    String data19 = Serial.readStringUntil('\n');
     buttonState = digitalRead(buttonPin);
     if (buttonState != lastButtonState)
    {
    lastButtonState=buttonState;    
             
        if (buttonState == HIGH)
      {
        buttonCounter++;        // count one up 
        Serial.println(buttonCounter);
      
        buttonStartTime = millis(); //Start timer to count how long the button is held
        firstPress = false; //set flag to skip this if statement until after the button has been released
      }
         if(buttonCounter % 6 == 0)
          {
              lcd.setCursor(0, 0);
            lcd.print(data);
            
               lcd.setCursor(0, 1);
              lcd.print(data1);
              delay(250);
          }
              if(buttonCounter % 6 == 1)
          {
               lcd.setCursor(0, 0);
             lcd.print(data2);
               lcd.setCursor(0, 1);
              lcd.print(data3);
              delay(250);
          }
              if(buttonCounter % 6 == 2)
          {
             lcd.setCursor(0, 0);
            lcd.print(data4);
               lcd.setCursor(0, 1);
              lcd.print(data5);
              delay(250);
          }
              if(buttonCounter % 6 == 3)
          {
            lcd.setCursor(0, 0);
             lcd.print(data6);
               lcd.setCursor(0, 1);
             lcd.print(data7);
              delay(250);
          }
              if(buttonCounter % 6 == 4)
          {
              lcd.setCursor(0, 0);
              
             lcd.print(data8);
               lcd.setCursor(0, 1);
              lcd.print(data9);
              delay(250);
          }
    }

 
    
   
  }
}
