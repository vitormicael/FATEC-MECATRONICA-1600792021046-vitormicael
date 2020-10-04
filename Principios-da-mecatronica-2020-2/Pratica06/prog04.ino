const int LED_VERDE=10;
const int LED_AMARELO=11;
const int LED_VERMELHO=12;
const int BOTAO_1=9;
const int BOTAO_2=8;

void setup()
{
  pinMode(LED_VERMELHO, OUTPUT);
  pinMode(LED_AMARELO, OUTPUT);
  pinMode(LED_VERDE, OUTPUT);
  pinMode(BOTAO_1, INPUT);
  pinMode(BOTAO_2, INPUT);
}

void loop()
{
  if (digitalRead(BOTAO_1) == HIGH)
    digitalWrite(LED_VERMELHO, HIGH);
    else if(digitalRead(BOTAO_2) == HIGH)
    digitalWrite(LED_VERMELHO, LOW);
}
