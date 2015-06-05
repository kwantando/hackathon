void setup() {
  // put your setup code here, to run once:
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  Serial.begin(9600);
}


void blink(int pin)
{
  for(int i = 0; i < 10; i++)
  {
    digitalWrite(pin, HIGH);
    delay(50);
    digitalWrite(pin, LOW);
    delay(50);
  }
}


void loop() {
  // put your main code here, to run repeatedly:
  char serial_message = Serial.read();
  if (serial_message == '0') {
      blink(12);
  } else if (serial_message == '1') {
      blink(11);
  } else if (serial_message == '2') {
      blink(10);
  }
}
