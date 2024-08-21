#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>

#define GPIO_PIR 1 // Pin GPIO 18 en BCM corresponde al pin 1 en WiringPi

int main(void) {
    int status0 = 0;
    int status1 = 0;
    int num = 0;

    // Inicializar WiringPi
    if (wiringPiSetup() == -1) {
        printf("No se pudo inicializar WiringPi\n");
        return 1;
    }

    // Configurar el pin como entrada
    pinMode(GPIO_PIR, INPUT);

    printf("Listo para comenzar!\n");

    while (1) {
        status0 = digitalRead(GPIO_PIR);
        
        if (status0 == 1 && status1 == 0) {
            num++;
            printf("Atención, se ha detectado movimiento %d\n", num);
            system("sudo /./home/sa/raspberry/off21");  // Ejecutar script para apagar nand
            status1 = 1;
        } 
        else if (status0 == 0 && status1 == 1) {
            printf("Listo para comenzar!\n");
            system("sudo /./home/sa/raspberry/on21");  // Ejecutar script para encender nand
            status1 = 0;
        }
        
        usleep(100000);  // Dormir 100 ms
    }

    return 0;
}
