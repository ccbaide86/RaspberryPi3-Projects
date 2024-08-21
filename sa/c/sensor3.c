#include <stdio.h>
#include <wiringPi.h>
#include <stdlib.h>
#include <stdint.h>

// Definir pin para el sensor DHT11
#define DHT_PIN 7  // Pin GPIO 4 en BCM corresponde al pin 7 en WiringPi

// Función para leer datos del sensor DHT11
int readDHT(int *temperature, int *humidity) {
    uint8_t laststate = HIGH;
    uint8_t counter = 0;
    uint8_t j = 0, i;
    int data[5] = {0, 0, 0, 0, 0};

    // Configurar el pin como salida y enviar señal baja
    pinMode(DHT_PIN, OUTPUT);
    digitalWrite(DHT_PIN, LOW);
    delay(18);  // Mantener señal baja por 18 ms
    digitalWrite(DHT_PIN, HIGH);
    delayMicroseconds(40);

    // Configurar el pin como entrada y leer datos
    pinMode(DHT_PIN, INPUT);

    for (i = 0; i < MAX_TIMINGS; i++) {
        counter = 0;
        while (digitalRead(DHT_PIN) == laststate) {
            counter++;
            delayMicroseconds(1);
            if (counter == 255) {
                break;
            }
        }
        laststate = digitalRead(DHT_PIN);

        if (counter == 255) break;

        // Ignorar los primeros 3 transitorios
        if ((i >= 4) && (i % 2 == 0)) {
            data[j / 8] <<= 1;
            if (counter > 16)
                data[j / 8] |= 1;
            j++;
        }
    }

    // Verificar la suma de comprobación y asignar valores de temperatura y humedad
    if ((j >= 40) && 
        (data[4] == ((data[0] + data[1] + data[2] + data[3]) & 0xFF))) {
        *humidity = data[0];
        *temperature = data[2];
        return 1;
    } else {
        return 0;
    }
}

int main(void) {
    int temperature = 0;
    int humidity = 0;

    // Inicializar WiringPi
    if (wiringPiSetup() == -1) {
        printf("No se pudo inicializar WiringPi\n");
        return 1;
    }

    // Intentar leer datos del sensor
    if (readDHT(&temperature, &humidity)) {
        printf("Temperatura: %d°C\n", temperature);
        printf("Humedad: %d%%\n", humidity);
    } else {
        printf("Error al leer temperatura y humedad\n");
    }

    return 0;
}
