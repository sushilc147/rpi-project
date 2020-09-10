import RPi.GPIO as GPIO
import time
from sys import argv
whichled=argv[1]
ledaction = argv[2]
LEDa=17
LEDb=18
LEDc=22
LEDd=24
LEDe=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDe, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDa, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDb, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDc, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDd, GPIO.OUT)
if ledaction=="off":
    if whichled=="e":
        GPIO.output(LEDe, False)
    if whichled=="a":
        GPIO.output(LEDa, False)
    if whichled=="b":
        GPIO.output(LEDb, False)
    if whichled=="c":
        GPIO.output(LEDc, False)
    if whichled=="d":
        GPIO.output(LEDd, False)
    if whichled=="all":
        GPIO.output(LEDe, False)
        GPIO.output(LEDa, False)
        GPIO.output(LEDb, False)
        GPIO.output(LEDc, False)
        GPIO.output(LEDd, False)
if ledaction=="on":
    if whichled=="e":
        GPIO.output(LEDe, True)
    if whichled=="a":
        GPIO.output(LEDa, True)
    if whichled=="b":
        GPIO.output(LEDb, True)
    if whichled=="c":
        GPIO.output(LEDc, True)
    if whichled=="d":
        GPIO.output(LEDd, True)
    if whichled=="all":
        GPIO.output(LEDe, True)
        GPIO.output(LEDa, True)
        GPIO.output(LEDb, True)
        GPIO.output(LEDc, True)
        GPIO.output(LEDd, True)
        

