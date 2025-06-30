from utime import sleep_ms
from machine import Pin, SPI
from time import sleep

spi = SPI(0, sck=Pin(18), miso=Pin(16), mosi=Pin(19))
spi.init(baudrate=500_000, bits=8, polarity=0, phase=0, firstbit=SPI.MSB)
CS = Pin(17, Pin.OUT)
CS.high()
sleep_ms(1)
CS.low()
write=bytearray([0x01, 0x80, 0x00])
read=bytearray(3)
spi.write_readinto(write,read)
CS.high()
data =  (read[1] & 0x03) << 8 |  read[2]
volts =  data * 3.3 / 1023.0
print(volts)
spi.deinit()
