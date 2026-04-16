import logging, time, digitalio

import pins

def seterrorled():
    led = digitalio.DigitalInOut(pins.PCBErrorLED)
    led.direction = digitalio.Direction.OUTPUT
    logging.debug("PCBErrorLED gesetzt")
    while True:
        led.value = True
        time.sleep(1.5)
        led.value = False


def unseterrorled():
    led = digitalio.DigitalInOut(pins.PCBErrorLED)
    led.direction = digitalio.Direction.OUTPUT
    led.value = False
    logging.debug("PCBErrorLED gelöscht")