#include "DHT.h"

#define DHTPIN 26        // GPIO pin connected to the sensor
#define DHTTYPE DHT11 // Change to DHT11 if needed
#define ldrpin 4   

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  pinMode(ldrpin,INPUT);
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature(); // Celsius
  int ldrStatus = analogRead(ldrpin);

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  if (isnan(ldrStatus)){
    Serial.println("Failed to read data from LDR");
  }

  // Send clean CSV format
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.println(ldrStatus);

  delay(5000); // Send every 2 seconds
}

