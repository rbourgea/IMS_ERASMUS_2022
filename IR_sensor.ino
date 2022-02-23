// Define connection pins:
#define pirPin 2
#define ledPin 13

int val = 0;
bool motionState = false;

void setup() {
  // Configure the pins as input or output:
  pinMode(ledPin, OUTPUT);
  pinMode(pirPin, INPUT);

  // Begin serial communication at a baud rate of 9600:
  Serial.begin(9600);
}

void loop() {
  // Read out the pirPin and store as val
  val = digitalRead(pirPin);

  // If motion is detected (pirPin = HIGH)
  if (val == HIGH) {
    digitalWrite(ledPin, HIGH); // Turn on the on-board LED.

    // Change the motion state to true
    if (motionState == false) {
      Serial.println("Motion detected!");
      motionState = true;
    }
  }

  // If no motion is detected (pirPin = LOW)
  else {
    digitalWrite(ledPin, LOW); // Turn off the on-board LED.

    // Change the motion state to false
    if (motionState == true) {
      Serial.println("Motion ended!");
      motionState = false;
    }
  }
}
