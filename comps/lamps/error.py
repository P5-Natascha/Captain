import logging, time, digitalio

import globals

def seterrorled():
    led = digitalio.DigitalInOut(globals.PCBErrorLED)
    led.direction = digitalio.Direction.OUTPUT
    logging.debug("PCBErrorLED gesetzt")
    while True:
        led.value = True
        time.sleep(1.5)
        led.value = False


def unseterrorled():
    led = digitalio.DigitalInOut(globals.PCBErrorLED)
    led.direction = digitalio.Direction.OUTPUT
    led.value = False
    logging.debug("PCBErrorLED gelöscht")
