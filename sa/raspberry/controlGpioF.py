#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from tkinter import font
import os
import time
import RPi.GPIO as GPIO
import Adafruit_DHT

# Configuración del GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configuración de pines
GPIO_PIR = 18
GPIO_TRIGGER = 23
GPIO_ECHO = 24

movimientos = 0

GPIO.setup(GPIO_PIR, GPIO.IN)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Crear ventana
v0 = Tk()
v0.title("Control GPIO 2024")
v0.geometry('1000x850+10+10')

# Zona de Texto
text1 = font.Font(family='Arial', size=20)
text2 = font.Font(family='Helvetica', size=12)
text3 = font.Font(family='Helvetica', size=16)
text4 = font.Font(family='Helvetica', size=20, weight='bold')

label_titulo=Label(v0, text="---CONTROL SCADA GPIO---",font=text1).place(x=310,y=5)

# Declarar imágenes
img_verde = PhotoImage(file="verde.gif")
img_rojo = PhotoImage(file="rojo.gif")
img_amarillo = PhotoImage(file="amarillo.gif")
img_gris = PhotoImage(file="gris.gif")
img_buzzeroff = PhotoImage(file="buzzeroff.gif")
img_buzzeron = PhotoImage(file="buzzeron.gif")

# ENCENDIDO
def evaluarCombo17():
    if combo17.get() == "ENCENDER LUZ ROJA":
        print("ROJO ENCENDIDO")
        os.system("sudo /./home/sa/sh/off17.sh")
        os.system("pkill onoff17.sh")
    elif combo17.get() == "APAGAR LUZ ROJA":
        print("ROJO APAGADO")
        os.system("sudo /./home/sa/sh/on17.sh")
    elif combo17.get() == "PARPADEO DE LUZ ROJA":
        print("ROJO PARPADEANDO")
        os.system("sudo /./home/sa/sh/onoff17.sh")

def evaluarCombo22():
    if combo22.get() == "ENCENDER LUZ AMARILLO":
        print("AMARILLO ENCENDIDO")
        os.system("sudo /./home/sa/sh/off22.sh")
        os.system("pkill onoff22.sh")
    elif combo22.get() == "APAGAR LUZ AMARILLO":
        print("AMARILLO APAGADO")
        os.system("sudo /./home/sa/sh/on22.sh")
    elif combo22.get() == "PARPADEO DE LUZ AMARILLO":
        print("AMARILLO PARPADEANDO")
        os.system("sudo /./home/sa/sh/onoff22.sh")

def evaluarCombo27():
    if combo27.get() == "ENCENDER LUZ VERDE":
        print("VERDE ENCENDIDO")
        os.system("sudo /./home/sa/sh/off27.sh")
        os.system("pkill onoff27.sh")
    elif combo27.get() == "APAGAR LUZ VERDE":
        print("VERDE APAGADO")
        os.system("sudo /./home/sa/sh/on27.sh")
    elif combo27.get() == "PARPADEO DE LUZ VERDE":
        print("VERDE PARPADEANDO")
        os.system("sudo /./home/sa/sh/onoff27.sh")

def evaluarCombo21():
    if combo21.get() == "ENCENDER BUZZER":
        print("BUZZER ENCENDIDO")
        os.system("sudo /./home/sa/sh/off21.sh")
        os.system("pkill onoff21.sh")
    elif combo21.get() == "APAGAR BUZZER":
        print("BUZZER APAGADO")
        os.system("sudo /./home/sa/sh/on21.sh")
    elif combo21.get() == "PARPADEO DE BUZZER":
        print("BUZZER PARPADEANDO")
        os.system("sudo /./home/sa/sh/onoff21.sh")

# Combobox
label_titulo17 = Label(v0, text="Control luz roja", font=text3).place(x=23, y=235)
combo17 = StringVar()
c17 = ttk.Combobox(v0, textvariable=combo17, values=["ENCENDER LUZ ROJA", "APAGAR LUZ ROJA", "PARPADEO DE LUZ ROJA"])
c17.place(x=10, y=260)
btn_combo17 = Button(v0, text=">", command=evaluarCombo17).place(x=197, y=257)

label_titulo22 = Label(v0, text="Control luz amarilla", font=text3).place(x=250, y=235)
combo22 = StringVar()
c22 = ttk.Combobox(v0, textvariable=combo22, values=["ENCENDER LUZ AMARILLO", "APAGAR LUZ AMARILLO", "PARPADEO DE LUZ AMARILLO"])
c22.place(x=247, y=260)
btn_combo22 = Button(v0, text=">", command=evaluarCombo22).place(x=430, y=257)

label_titulo27 = Label(v0, text="Control luz verde", font=text3).place(x=480, y=235)
combo27 = StringVar()
c27 = ttk.Combobox(v0, textvariable=combo27, values=["ENCENDER LUZ VERDE", "APAGAR LUZ VERDE", "PARPADEO DE LUZ VERDE"])
c27.place(x=477, y=260)
btn_combo27 = Button(v0, text=">", command=evaluarCombo27).place(x=660, y=255)

label_titulo21 = Label(v0, text="Control buzzer", font=text3).place(x=710, y=235)
combo21 = StringVar()
c21 = ttk.Combobox(v0, textvariable=combo21, values=["ENCENDER BUZZER", "APAGAR BUZZER", "PARPADEO DE BUZZER"])
c21.place(x=707, y=260)
btn_combo21 = Button(v0, text=">", command=evaluarCombo21).place(x=890, y=255)

# Funciones de sensor
def actualizar_temperatura_humedad():
    sensor = Adafruit_DHT.DHT11
    pin = 4
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    if humedad is not None and temperatura is not None:
        temperatura_label.config(text=f"Temperatura: {temperatura:0.1f}°C")
        humedad_label.config(text=f"Humedad: {humedad:0.1f}%")
    else:
        temperatura_label.config(text="Error al leer temperatura")
        humedad_label.config(text="Error al leer humedad")

def actualizar_distancia():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    inicio = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        inicio = time.time()
        
    while GPIO.input(GPIO_ECHO) == 1:
        fin = time.time()

    duracion = fin - inicio
    distancia = (duracion * 34300) / 2
    distancia_label.config(text=f"Distancia: {distancia:.1f} cm")

def actualizar_pir():
    if GPIO.input(GPIO_PIR) == 1:
        global movimientos
        movimientos+=1
        pir_label.config(text=f"Movimientos: {movimientos}")
        os.system("sudo /./home/sa/sh/off21.sh")
        time.sleep(0.3)
        os.system("sudo /./home/sa/sh/on21.sh")
        
    else:
        pir_label.config(text=f"Movimientos: {movimientos}")
        os.system("sudo /./home/sa/sh/on21.sh")

def actualizar():
    actualizar_temperatura_humedad()
    actualizar_distancia()
    actualizar_pir()
    
    # Actualizar estado de luces y buzzer
    for pin, imagen_on, imagen_off, pos_x, pos_y in [
        ("17", img_rojo, img_gris, 45, 300),
        ("22", img_amarillo, img_gris, 280, 300),
        ("27", img_verde, img_gris, 515, 300),
        ("21", img_buzzeron, img_buzzeroff, 750, 300),
    ]:
        try:
            with open(f"/home/sa/estado{pin}.txt", "r") as pf:
                estado = pf.readline().strip()
                imagen = imagen_on if estado == "0" else imagen_off
                Button(v0, image=imagen).place(x=pos_x, y=pos_y)
        except FileNotFoundError:
            pass

    v0.after(1000, actualizar)

# Crear etiquetas y posiciones
Label(v0, text="Sensor de Proximidad", font=text3).place(x=360, y=100)
distancia_label = Label(v0, text="Distancia: -- cm", font=text4)
distancia_label.place(x=360, y=130)

Label(v0, text="Sensor de Temperatura", font=text3).place(x=680, y=100)
temperatura_label = Label(v0, text="Temperatura: -- °C", font=text4)
temperatura_label.place(x=680, y=130)
humedad_label = Label(v0, text="Humedad: -- %", font=text4)
humedad_label.place(x=680, y=160)

Label(v0, text="Sensor de PIR", font=text3).place(x=20, y=100)
pir_label = Label(v0,text=f"Movimientos: {movimientos}", font=text4)
pir_label.place(x=20, y=130)

# Iniciar la actualización periódica
actualizar()

# Ejecutar la interfaz
