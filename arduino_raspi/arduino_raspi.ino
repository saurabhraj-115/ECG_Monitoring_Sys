void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A3,OUTPUT);
  pinMode(8, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue= analogRead(A0);
  /*float voltage= sensorValue * (5.0 / 1023.0);*/
  float voltage= sensorValue * (5.0 / 1023.0);
  Serial.println(voltage);
  digitalWrite(8, voltage);

}
