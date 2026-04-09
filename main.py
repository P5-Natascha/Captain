import time

from Sensoren import ADC
from motors import deathrun

def main():
    print("===Testmode ===")
    adc = ADC.ADC()

    adc.get_ampere(0)
    adc.get_12voltage(1)


    print("===Dreht Motoren in 30Sek!===")
    time.sleep(30)
    deathrun.deathrun(5,True,25)

    adc.de_ADC()
    print("===Testmode fertig!===")

if __name__ == '__main__':
    main()