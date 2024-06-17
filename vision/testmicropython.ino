#include <Servo.h>

Servo miServo;          // Objeto de la clase Servo

void setup() {
  miServo.attach(18);     // El servo se conecta al pin 5
  miServo.write(100);
  Serial.begin(115200);
}

void loop() {
  if(Serial.available()>0){
    if(Serial.read() == '0'){
      miServo.write(0); // Mueve el servo a la nueva posición
      delay(3000); // Espera para evitar lecturas múltiples debido al rebote del botón
      miServo.write(100);
      }
   }
}
