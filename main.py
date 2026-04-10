import time
import threading

from Sensoren import ADC
from Sensoren import Batterie_Prozent
from Motor import motors
from Comm import Comm

def main():
    print("===Testmode ===")
    t1 = threading.Thread(target=Comm.tcp_server_step)
    t1.start()
    adc = ADC.ADC()


    t2 = threading.Thread(target=Comm.connHandler, args=(adc, 0))
    t2.start()

    print(adc.get_ampere(0))
    print(adc.get_12voltage(1))

    t3 = threading.Thread(target=Batterie_Prozent.collect_Bat_Prozent, args=(adc,))
    t3.start()

    while True:
        print(Batterie_Prozent.get_Bat_Prozent())
        time.sleep(5)


    print("===Dreht Motoren in 5Sek!===")
    time.sleep(5)

    motors.vorwaerts(30, 100)


    #adc.de_ADC()
    print("===Testmode fertig!===")

if __name__ == '__main__':
    main()