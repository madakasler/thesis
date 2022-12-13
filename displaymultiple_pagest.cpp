
// NJarpa
// LCD 16x2 Multiple screens example

#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(11,12,13,3,4,5,6,7,8,9,10);

//Counter to change positions of pages

int page_counter=1 ;       //To move beetwen pages


//-------Pins-----//
int up = 2;               //Up button
        //Down button
//---------Storage debounce function-----//
boolean current_up = LOW;          
boolean last_up=LOW;            
boolean last_down = LOW;
boolean current_down = LOW;
        

void setup() {
  lcd.begin(16,2); 

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

current_up = debounce(last_up, up);         //Debounce for Up button
;   //Debounce for Down button

//----Page counter function to move pages----//

//Page Up
    if (last_up== LOW && current_up == HIGH){  //When up button is pressed
      lcd.clear();                     //When page is changed, lcd clear to print new page  
      if(page_counter <3){              //Page counter never higher than 3(total of pages)
      page_counter= page_counter +1;   //Page up
      
      }
      else{
      page_counter= 3;  
      }
  }
  
    last_up = current_up;

//Page Down
 
  
   

//------- Switch function to write and show what you want---// 
  switch (page_counter) {
   
    case 1:{     //Design of home page 1
      lcd.setCursor(5,0);
      lcd.print("This is");
      lcd.setCursor(3,1);
      lcd.print(" Home Page");
    }
    break;

    case 2: { //Design of page 2 
     lcd.setCursor(5,0);
     lcd.print("This is");
     lcd.setCursor(5,1);
     lcd.print("Page 2");
    }
    break;

    case 3: {   //Design of page 3 
     lcd.setCursor(1,0);
     lcd.print("You are now on");
     lcd.setCursor(4,1);
     lcd.print("Page 3");
    }
    break;
    
  }//switch end
  
}//loop end
