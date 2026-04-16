import logging
import time
import digitalio

import globals

def setspoilererrorled():
    #braucht einen thread
    led = digitalio.DigitalInOut(globals.SpoilerLEDred)
    led.direction = digitalio.Direction.OUTPUT
    logging.debug("SpoilerLEDred gesetzt")
    while True:
        led.value = True
        time.sleep(1.5)
        led.value = False

def unsetspoilererrorled():
    led = digitalio.DigitalInOut(globals.SpoilerLEDred)
    led.direction = digitalio.Direction.OUTPUT
    led.value = False
    logging.debug("SpoilerLEDred gelöscht")

def setspoileryellowled():
    #braucht einen thread
    led = digitalio.DigitalInOut(globals.SpoilerLEDyellow)
    led.direction = digitalio.Direction.OUTPUT
    logging.debug("SpoilerLEDyellow gesetzt")
    while True:
        led.value = True
        time.sleep(1.5)
        led.value = False


def unsetspoileryellowled():
    led = digitalio.DigitalInOut(globals.SpoilerLEDyellow)
    led.direction = digitalio.Direction.OUTPUT
    led.value = False
    logging.debug("SpoilerLEDyellow gelöscht")

def setspoilergreenled():
    led = digitalio.DigitalInOut(globals.SpoilerLEDgreen)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True
    logging.debug("SpoilerLEDgreen gesetzt")

def unsetspoilergreenled():
    led = digitalio.DigitalInOut(globals.SpoilerLEDgreen)
    led.direction = digitalio.Direction.OUTPUT
    led.value = False
    logging.debug("SpoilerLEDgreen gelöscht")