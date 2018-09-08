/*
 * The following takes an input from arduino_control.py through Serial and changes a bi-color led light based on the input.
 */
/*-----( Declare Constants)-----*/
const int ledPin1 =  13;
const int ledPin2 =  8;

/*-----( Declare Variables )-----*/
int ByteReceived;

void setup()   /****** SETUP: RUNS ONCE ******/
{
  Serial.begin(9600); 
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT); 
}
//--(end setup )---

void loop()   /****** LOOP: RUNS CONSTANTLY ******/
{
  if (Serial.available() > 0)
  {
    ByteReceived = Serial.read();
    Serial.print(ByteReceived);        
    Serial.print(char(ByteReceived));

    if(char(ByteReceived) == '3')
    {
      digitalWrite(ledPin1, HIGH);
      digitalWrite(ledPin2, HIGH);
      Serial.print(" LED ORANGE ON ");
    }

    if(char(ByteReceived) == '2') // Single Quote! This is a character.
    {
      digitalWrite(ledPin1, LOW);
      digitalWrite(ledPin2, HIGH);
      Serial.print(" LED YELLOW ON ");
    }
    
    if(char(ByteReceived) == '1') 
    {
      digitalWrite(ledPin1, HIGH);
      digitalWrite(ledPin2, LOW);
      Serial.print(" LED RED ON ");
    }
    
    if(char(ByteReceived) == '0')
    {
      digitalWrite(ledPin1, LOW);
      digitalWrite(ledPin2, LOW);
      Serial.print(" LED OFF");
    }
    
    Serial.println();    // End the line

  // END Serial Available
  }
}

//--(end main loop )---
