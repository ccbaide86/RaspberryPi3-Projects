#include <stdlib.h>
#include <wiringPi.h>
#include <stdio.h> 

int main(void) {
    // Inicializar WiringPi
    if (wiringPiSetup() == -1) {
        printf("No se pudo inicializar WiringPi\n");
        return 1;
    }

    const int pin = 0;

    pinMode(pin, OUTPUT);

    digitalWrite(pin, LOW);
    delay(1000);
    printf("Apagado\n");

    FILE *pf = fopen("/home/sa/raspberry/estado17.txt", "w");

    // Evaluar si el archivo existe
    if (pf == NULL)
    {
        printf("<<< ERROR EN EL ARCHIVO >>>");
        return 1;
    }

    // Imprimir en el archivo el valor de 0
    fprintf(pf, "%d", 0);
    // Imrpimir espacio en blanco
    fprintf(pf, "\n");

    return 0;
}
