"""
written by Jannik Czinzoll
"""
import board
import busio
import digitalio
import pins

import adafruit_mcp3xxx.mcp3204 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn





def initmcp():
    # spi init und cs pin festlegen
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    cs = digitalio.DigitalInOut(pins.CSPin)

    # MCP3204 initialisieren
    mcp = MCP.MCP3204(spi, cs)
    chan1 = AnalogIn(mcp, MCP.P1)
    return chan1


VOLTAGE_FACTOR: float = 5.659637188
def readvoltage(chan: AnalogIn) -> float:
    voltage = chan.voltage
    volt = voltage * VOLTAGE_FACTOR
    print(f"{volt:.2f}V")
    return volt

