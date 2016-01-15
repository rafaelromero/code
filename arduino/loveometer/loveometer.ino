
  const int sensorPin = A0;
  const float baseLineTemp = 22.00;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);


  for(int pinNumber = 2; pinNumber<5; pinNumber++){
     pinMode(pinNumber, OUTPUT);
     digitalWrite(pinNumber, LOW);
  }
  

}

void loop() {
  // put your main code here, to run repeatedly:
  //SENSOR RANGE 0 - 1024
  //VOLT RANGE   0 - 5
  //SENSOR Volt Range 0 - 1.75 = .01 per degree change
  //TEMP RANGE  -50 - 125 celcius
  //
  int sensorVal     = analogRead(sensorPin);
  float voltage     = (sensorVal/1024.0)*5.0;
  float temperatureC = (voltage - .5) *100;
  float temperatureF = (temperatureC * 1.8) + 32;

  Serial.print("Sensor Value: ");
  Serial.print(sensorVal);
  Serial.print(" ");
  Serial.print("Voltage : ");
  Serial.print(voltage);
  Serial.print(" ");
  Serial.print("Temperature(c) : ");
  Serial.print(temperatureC);
  Serial.print(" ");
  Serial.print("Temperature(f) : ");
  Serial.print(temperatureF);
  Serial.println("");
  delay(1500);


  if(temperatureC < baseLineTemp){
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }else if(temperatureC >= baseLineTemp+2 && temperatureC < baseLineTemp+4){
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }else if(temperatureC >= baseLineTemp +4 && temperatureC < baseLineTemp +6){
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
   }else if(temperatureC >= baseLineTemp +6){
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
  }
  
}
