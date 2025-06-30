from utime import sleep_ms
from machine import Pin, SPI
from time import sleep
class spiADC:
    def __init__(self,spi,sckNo,misoNo,mosiNo,CSNo):
        self.spi = SPI(spi, sck=Pin(sckNo),
                           miso=Pin(misoNo), mosi=Pin(mosiNo))
        self.spi.init(baudrate=500_000, bits=8, 
                           polarity=0, phase=0, firstbit=SPI.MSB)
        self.CS = Pin(CSNo, Pin.OUT)
        self.CS.high()
        sleep_ms(1)

    def read(self,chan):
        write=bytearray([0x01, (0x08 | chan) << 4 , 0x00])
        self.CS.low()
        read=bytearray(3)
        self.spi.write_readinto(write,read)
        self.CS.high()
        data =  (read[1] & 0x03) << 8 |  read[2]
        volts =  data * 3.3 / 1023.0
        return volts
adc=spiADC(0,18,16,19,17)
while True:
    volts=adc.read(1)