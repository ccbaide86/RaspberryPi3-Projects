import RPi.GPIO as GPIO
import time

# Configuración de pines
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distancia():
    # Enviar pulso de activación
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # Calcular duración del pulso de retorno
    inicio = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        inicio = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        fin = time.time()

    duracion = fin - inicio

    # Calcular distancia
    distancia = (duracion * 34300) / 2

    return distancia

try:
    while True:
        print("Distancia: %.1f cm" % distancia())
        time.sleep(1)

except KeyboardInterrupt:
    print("Medición detenida por el usuario")
    GPIO.cleanup()
