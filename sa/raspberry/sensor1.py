#!/usr/bin/python3
import subprocess
import time
import pygame
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_PIR = 18
GPIO.setup(GPIO_PIR,GPIO.IN)

num=0
status0 = 0
status1 = 0
try :
    while True:
              status0 = 0
              print ("Listo para comenzar!")
              while True:
                        status0 = GPIO.input(GPIO_PIR)
                        if status0==1 and status1==0:
                                     num=num+1
                                     print ("Atencion se ha detectado movimiento ",num,"")
                                     os.system("sudo /./home/sa/off21.sh")
                                     status1=1
                                     
                                     ##subprocess.call("/./home/pi/timbreON.sh");
                        elif status0==0 and status1==1:
                                     print ("Listo para comenzar!")
                                     os.system("sudo /./home/sa/on21.sh")
                                     status1=0
                                     time.sleep(0.1)
except KeyboardInterrupt:
       GPIO.cleanup()
