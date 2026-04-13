import threading

from comps.sensors import ADC, Batterie_Prozent
from communication import comms


def main():
    adc = ADC.ADC()
    t1 = threading.Thread(target=comms.connHandler, args=(adc,))
    t1.start()
    t2 = threading.Thread(target=comms.udpHandler)
    t2.start()

    print(adc.get_ampere(0))
    print(adc.get_12voltage(1))

    t3 = threading.Thread(target=Batterie_Prozent.collect_Bat_Prozent, args=(adc,))
    t3.start()

if __name__ == '__main__':
    main()