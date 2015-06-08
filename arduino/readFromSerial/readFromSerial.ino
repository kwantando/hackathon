void setup() 
{
    Serial.begin(9600);  

    pinMode(13, OUTPUT);
    pinMode(12, OUTPUT);
    pinMode(11, OUTPUT);
    pinMode(10, OUTPUT);
    pinMode( 9, OUTPUT);
    pinMode( 8, OUTPUT);
    pinMode( 7, OUTPUT);
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

void lightBlues(bool on = false)
{
    if(on)
        digitalWrite( 7, HIGH);
    else
        digitalWrite( 7, LOW);    
}

void blinkGreens(int blinkNum = 5)
{
    int msDelay = 100;  
    
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


unsigned long oneMinuteInMs = 1*60*1000;
unsigned long fiveMinutesInMs = 5*60*1000;
unsigned long tenSecsInMs = 10*1000;
unsigned long thirtySecsInMs = 30*1000;
unsigned long msSinceComplete = 0;

void loop() 
{
    digitalWrite(7, HIGH);
    while(Serial.available() == 0)
    {
        if(msSinceComplete != 0) 
        {
//            if(millis() - msSinceComplete <= oneMinuteInMs)
            if(millis() - msSinceComplete <= thirtySecsInMs)
                digitalWrite(7, HIGH);
            else
                digitalWrite(7, LOW);
        }        
        else
            digitalWrite( 7, LOW);
    }
    
    
    String buildStatus = Serial.readString();
    
    if(buildStatus == "starting")
    {
        digitalWrite(7, LOW);
        msSinceComplete = 0;
        blinkReds();
    }
    else if(buildStatus == "inprocess")
    {
        digitalWrite(7, LOW);
        msSinceComplete = 0;
        toggleYellows();
        toggleYellows();
    }
    else if(buildStatus == "complete")
    {
        digitalWrite(7, LOW);
        blinkGreens();
        msSinceComplete = millis();
    }
    
    
    
}
