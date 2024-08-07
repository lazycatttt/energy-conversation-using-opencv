char x; 

void setup() { 
  Serial.begin(9600);
  pinMode(5,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(8,OUTPUT);
  Serial.setTimeout(1); 
} 

void loop() { 
  while (!Serial.available()); 
  x = Serial.read();
   if(x=='A'){
    //Serial.println("1 ON");
    digitalWrite(5,HIGH);
    delay(10);
  }
   else if(x=='B'){
    //Serial.println("5 ON");
    digitalWrite(9,HIGH);
    delay(10);
  }
   else if(x=='C'){
    //Serial.println("3 ON");
    digitalWrite(10,HIGH);
    delay(10);
  }
   else if(x=='D'){
    //Serial.println("4 ON");
    digitalWrite(8,HIGH);
    delay(10);
  }
    digitalWrite(5,LOW);
    digitalWrite(10,LOW);
    digitalWrite(9,LOW);
    digitalWrite(8,LOW);
  } 
