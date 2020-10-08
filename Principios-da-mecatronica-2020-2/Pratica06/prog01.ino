void setup()
{
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, INPUT);
  pinMode(8, INPUT);
}

void loop()
{
  if (digitalRead(8) == HIGH)
    digitalWrite(10, HIGH);
   else 
    digitalWrite(10, LOW);
}
