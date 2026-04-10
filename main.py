import time

from Sensoren import ADC
from Motor import motors

def main():
    print("===Testmode ===")
    adc = ADC.ADC()

    print(adc.get_ampere(0) + "A")
    print(adc.get_12voltage(1) + "V")


    print("===Dreht Motoren in 5Sek!===")
    time.sleep(5)

    motors.vorwaerts(30, 100)


    adc.de_ADC()
    print("===Testmode fertig!===")

if __name__ == '__main__':
    main()