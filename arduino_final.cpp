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
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32



#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(11,12,13,3,4,5,6,7,8,9,10);
//-------Pins-----//
int up = 2;               //Up button
        //Down button
//---------Storage debounce function-----//
boolean current_up = LOW;          
boolean last_up=LOW;            
boolean last_down = LOW;
boolean current_down = LOW;
          // the number of the pushbutton pin
   // the number of the LED pin
   //Counter to change positions of pages
String data;
String data1;
String data2;
String data3;
String data4;
String data5;
String data6;
String data7;
String data8;
String data9;
String data10;
String data11;
String data12;
String data13;
String data14;
String data15;

int page_counter=1 ;

void setup() {
   Serial.begin(9600);
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
    pinMode(up, INPUT);
     display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS);
  display.clearDisplay();
  // Print a message to the LCD.
  //lcd.print("hello, world!");
}

   //---- De-bouncing function for all buttons----//
boolean debounce(boolean last, int pin)
{
boolean current = digitalRead(pin);
if (last != current)
{
delay(5);
current = digitalRead(pin);
}
return current;
}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
current_up = debounce(last_up, up);      
//Page Up
    if (last_up== LOW && current_up == HIGH){  //When up button is pressed
      lcd.clear();                     //When page is changed, lcd clear to print new page  
      if(page_counter <4){              //Page counter never higher than 3(total of pages)
      page_counter= page_counter +1;   //Page up
      
      }
      else{
      page_counter= 4;  
      }
  }
  
    last_up = current_up;

  // print the number of seconds since reset:

   if (Serial.available() > 0) {
  data = Serial.readStringUntil('\n');//cpu_str
  data1 = Serial.readStringUntil('\n');//memory
  data2 = Serial.readStringUntil('\n');//cpu_times
  data3 = Serial.readStringUntil('\n');//cpu_count
  data4 = Serial.readStringUntil('\n');//cpu_stats
  data5 = Serial.readStringUntil('\n');//cpu_freq
  data6 = Serial.readStringUntil('\n');//swap_mem
  data7 = Serial.readStringUntil('\n');//netiocounters
  data8 = Serial.readStringUntil('\n');//temperatures

   display.setTextSize(2); // Draw 2X-scale text
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(10, 0);
  display.println(data8);
  display.display();


 
  }
    switch (page_counter) {
   
    case 1:{     //Design of home page 1
    lcd.setCursor(0, 0);
    lcd.print(data);    
    lcd.setCursor(0, 1);
    lcd.print(data1);
    }
    break;

    case 2: { //Design of page 2 
      lcd.setCursor(0, 0);
    lcd.print(data2);    
    lcd.setCursor(0, 1);
    lcd.print(data3);
    }
    break;

    case 3: {   //Design of page 3 
      lcd.setCursor(0, 0);
    lcd.print(data4);    
    lcd.setCursor(0, 1);
    lcd.print(data5);
    }
    break;
    
        case 4: {   //Design of page 4
      lcd.setCursor(0, 0);
    lcd.print(data6);    
    lcd.setCursor(0, 1);
    lcd.print(data7);
    }
    break;

   

 
    
  }
}
