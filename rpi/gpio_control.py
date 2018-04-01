from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('GPIOControlIntent', mapping={'status': 'status', 'pin': 'pin'})
def gpio_control(status, pin):
    GPIO.setup(4, GPIO.OUT)
    p = GPIO.PWM(4, 50)
    p.start(7.5)
    p.ChangeDutyCycle(5.5)
    time.sleep(0.2)
    p.ChangeDutyCycle(2.5)

    try:
        pinNum = 15 
    except Exception as e:
        return statement('Pin number not valid.')

    GPIO.setup(pinNum, GPIO.OUT)

    GPIO.output(pinNum, GPIO.HIGH)
    sleep(7)
    GPIO.output(pinNum, GPIO.LOW)
    return statement('Enjoy your drink')
    '''
    if status in ['on', 'high']:    
	GPIO.output(pinNum, GPIO.HIGH) #replaced HIGH with True
    if status in ['off', 'low']:    
	GPIO.output(pinNum, GPIO.LOW) #replaced
    
    return statement('Turning pin {} {}'.format(pin, status))
    '''
