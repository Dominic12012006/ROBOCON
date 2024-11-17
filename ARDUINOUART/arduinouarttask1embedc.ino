void setup() {
  Serial.begin(9600);
}
String data;
void loop() {
  if(Serial.available()){
    data=Serial.readStringUntil('\n');
    Serial.println(data);
  }
  delay(50);
}
