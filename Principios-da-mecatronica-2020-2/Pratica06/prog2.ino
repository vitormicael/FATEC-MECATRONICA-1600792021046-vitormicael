void setup()
{
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
}

void loop()
{
  if (digitalRead(8)==HIGH)
    digitalWrite(10, HIGH);
  else
    digitalWrite(10, LOW);
}
