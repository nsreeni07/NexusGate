
You said: #include <SPI.
#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

#define SS_PIN 10
#define RST_PIN 8
#define SERVO_PIN 6

MFRC522 rfid(SS_PIN, RST_PIN);
Servo lockServo;

// Authorized UID (your card)
byte authorizedUID[4] = {0xB7, 0xBF, 0x9D, 0x31};

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();

  lockServo.attach(SERVO_PIN);
  lockServo.write(0);  // Locked position

  Serial.println("Scan authorized card...");
}

void loop() {

  if (!rfid.PICC_IsNewCardPresent())
    return;

  if (!rfid.PICC_ReadCardSerial())
    return;

  Serial.print("Scanned UID: ");

  for (byte i = 0; i < rfid.uid.size; i++) {
    Serial.print(rfid.uid.uidByte[i], HEX);
    Serial.print(" ");
  }
  Serial.println();

  if (isAuthorized()) {
    Serial.println("Access Granted");
    unlockDoor();
  } else {
    Serial.println("Access Denied");
  }

  rfid.PICC_HaltA();
}

bool isAuthorized() {
  for (byte i = 0; i < 4; i++) {
    if (rfid.uid.uidByte[i] != authorizedUID[i])
      return false;
  }
  return true;
}

void unlockDoor() {
  lockServo.write(0);   // Unlock 
  delay(3000);
  lockServo.write(90);    // Return to Lock
}
