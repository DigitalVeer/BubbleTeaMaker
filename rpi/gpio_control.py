##--[[ IMPORTS ]]--##
from flask import Flask
from flask_ask import Ask, statement, convert_errors
from time import sleep
import RPi.GPIO as GPIO
import logging
import time
##--[[ IMPORTS END]]--##


##--[[ SET UP BEGIN ]]--##
# The current model being used is a Raspberry Pi 3
# GPIO has two modes: BCM and BOARD mode
# For the sake of consistency, only BCM mode will be used throughout
GPIO.setmode(GPIO.BCM)


# Initialize Flask, the service to help route our intents to Alexa
app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

# Show our INTENTions (ba dum tss) and the parameters we expect to be passed in
# Although we are not doing anything with these parameters, they're useful for debugging
@ask.intent('GPIOControlIntent', mapping={'status': 'status', 'pin': 'pin'})

##--[[ SET UP END ]]--##


##--[[ FUNCTION BEGIN ]]--##

def gpio_control(status, pin):
    #Set up appropiate pins
    GPIO.setup(4, GPIO.OUT)
    p = GPIO.PWM(4, 50)
    p.start(7.5)
    #Ensure everything is clocked at an appropiate speed
    p.ChangeDutyCycle(5.5)
    #Keep a small pause between each sequence
    time.sleep(0.2)
    p.ChangeDutyCycle(2.5)

    try:
        pinNum = 15 
    except Exception as e:
        return statement('Pin number not valid.')

    GPIO.setup(pinNum, GPIO.OUT)

    GPIO.output(pinNum, GPIO.HIGH)

    #Due to the nature of the way Alexa is programmed, a response cannot be given after more than 8 seconds.
    #Hence, 7 seconds is the maximum time the program can process tasks without returning to Alexa
    sleep(7)
    GPIO.output(pinNum, GPIO.LOW)

    #Task is set up to expect a string - statement allows for that.
    return statement('Enjoy your drink')

##--[[ FUNCTION END ]]--##

    '''
    if status in ['on', 'high']:    
	GPIO.output(pinNum, GPIO.HIGH) #replaced HIGH with True
    if status in ['off', 'low']:    
	GPIO.output(pinNum, GPIO.LOW) #replaced
    
    return statement('Turning pin {} {}'.format(pin, status))
    '''
