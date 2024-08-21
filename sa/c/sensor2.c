#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>

#define GPIO_TRIGGER 4  // Pin GPIO 23 en BCM corresponde al pin 4 en WiringPi
#define GPIO_ECHO 5     // Pin GPIO 24 en BCM corresponde al pin 5 en WiringPi

// Función para medir la distancia
double medir_distancia() {
    // Enviar pulso de activación
    digitalWrite(GPIO_TRIGGER, HIGH);
    usleep(10);  // 10 microsegundos
    digitalWrite(GPIO_TRIGGER, LOW);

    // Calcular la duración del pulso de retorno
    while (digitalRead(GPIO_ECHO) == LOW);
    long inicio = micros();

    while (digitalRead(GPIO_ECHO) == HIGH);
    long fin = micros();

    long duracion = fin - inicio;

    // Calcular distancia
    double distancia = (duracion * 34300.0) / 2000000.0;  // Convertir microsegundos a segundos y dividir por 2

    return distancia;
}

int main(void) {
    // Inicializar WiringPi
    if (wiringPiSetup() == -1) {
        printf("No se pudo inicializar WiringPi\n");
        return 1;
    }

    // Configuración de pines
    pinMode(GPIO_TRIGGER, OUTPUT);
    pinMode(GPIO_ECHO, INPUT);

    digitalWrite(GPIO_TRIGGER, LOW);  // Asegurarse de que el trigger esté bajo inicialmente
    delay(30);  // Esperar 30 ms para estabilizar el sensor

    try {
        while (1) {
            double dist = medir_distancia();
            printf("Distancia: %.1f cm\n", dist);
            delay(1000);  // Esperar 1 segundo antes de la próxima medición
        }
    } catch (...) {
        printf("Medición detenida por el usuario\n");
        digitalWrite(GPIO_TRIGGER, LOW);  // Apagar el trigger
        GPIO.cleanup();
    }

    return 0;
}
