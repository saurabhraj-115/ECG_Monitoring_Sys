void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
  
}
 
void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue= analogRead(A0);
  float voltage= sensorValue * (3.3 / 1023.0);
/*float voltage= sensorValue * (3.3 / 1023.0);*/
  delay(5);
  Serial.println(voltage);
  
  /*Serial.println(sensorValue);*/
  /*digitalWrite(7, voltage);*/
  /*Serial.write(sensorValue);*/
  /*Serial.write(sensorValue);*/

}
