char letra;
int led1 = 8;
int led2 = 2;
void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  if(Serial.available() > 0){
    letra = Serial.read();
    
    if(letra == 'a'){
      digitalWrite(led1, 1);
      digitalWrite(led2, 0);
      }
      if(letra == 'b'){
        digitalWrite(led2, 1);
        digitalWrite(led1, 0);
      }
   }
}
