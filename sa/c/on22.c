#include <stdlib.h>
#include <wiringPi.h>
#include <stdio.h> 

int main(void) {
    // Inicializar WiringPi
    if (wiringPiSetup() == -1) {
        printf("No se pudo inicializar WiringPi\n");
        return 1;
    }

    const int pin = 3;

    pinMode(pin, OUTPUT);

    digitalWrite(pin, HIGH);
    delay(1000);
    printf("Encendido\n");

    FILE *pf = fopen("/home/sa/raspberry/estado22.txt", "w");

    // Evaluar si el archivo existe
    if (pf == NULL)
    {
        printf("<<< ERROR EN EL ARCHIVO >>>");
        return 1;
    }

    // Imprimir en el archivo el valor de 1
    fprintf(pf, "%d", 1);
    // Imrpimir espacio en blanco
    fprintf(pf, "\n");

    return 0;
}
