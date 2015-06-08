void setup() 
{
    Serial.begin(9600);  

    pinMode(13, OUTPUT);
    pinMode(12, OUTPUT);
    pinMode(11, OUTPUT);
    pinMode(10, OUTPUT);
    pinMode( 9, OUTPUT);
    pinMode( 8, OUTPUT);
}

void blinkReds(int blinkNum = 5)
{
    int msDelay = 40;  
    
    for(int i = 0; i <  blinkNum; i++)
    {
        digitalWrite(13, HIGH);
        delay(msDelay);
        digitalWrite(13, LOW);
        delay(msDelay);
        digitalWrite(13, HIGH);
        delay(msDelay);
        digitalWrite(13, LOW);
        delay(msDelay);
    }      
}

void blinkGreens(int blinkNum = 5)
{
    int msDelay = 40;  
    
    for(int i = 0; i <  blinkNum; i++)
    {
        digitalWrite( 8, HIGH);
        delay(msDelay);
        digitalWrite( 8, LOW);
        delay(msDelay);
        digitalWrite( 8, HIGH);
        delay(msDelay);
        digitalWrite( 8, LOW);
        delay(msDelay);
    }      
}

void toggleYellows()
{
    int msDelay = 75;  
    
    digitalWrite(12, HIGH);
    delay(msDelay);
    digitalWrite(12, LOW);
  
    digitalWrite(11, HIGH);
    delay(msDelay);
    digitalWrite(11, LOW);
  
    digitalWrite(10, HIGH);
    delay(msDelay);
    digitalWrite(10, LOW);
  
    digitalWrite( 9, HIGH);
    delay(msDelay);
    digitalWrite( 9, LOW);
  
    delay(50);
  
    digitalWrite( 9, HIGH);
    delay(msDelay);
    digitalWrite( 9, LOW);
  
    digitalWrite(10, HIGH);
    delay(msDelay);
    digitalWrite(10, LOW);
  
    digitalWrite(11, HIGH);
    delay(msDelay);
    digitalWrite(11, LOW);
  
    digitalWrite(12, HIGH);
    delay(msDelay);
    digitalWrite(12, LOW);
  
    delay(50);
}


void loop2()
{
    blinkReds();
    toggleYellows();
    blinkGreens();
}
void loop() 
{
    
    while(Serial.available() == 0)
    {}
    String buildStatus = Serial.readString();
    
    if(buildStatus == "starting")
    {
        blinkReds();
    }
    else if(buildStatus == "inprocess")
    {
        toggleYellows();
        toggleYellows();
    }
    else if(buildStatus == "complete")
    {
        blinkGreens();
    }
    
    
    
}
