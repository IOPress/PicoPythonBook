from utime import sleep_ms
from machine import Pin, SPI
from time import sleep

spi = SPI(0, sck=Pin(18), miso=Pin(16), mosi=Pin(19))
spi.init(baudrate=500_000, bits=8, polarity=0, phase=0,
                                           firstbit=SPI.MSB)

CS = Pin(17, Pin.OUT)
CS.high()
sleep_ms(1)

write = bytearray([0xD0])
CS.low()
spi.write(write)
read = spi.read(1)
CS.high()
print("Chip ID is",hex(read[0]))

CS.low()
write=bytearray([0xF2,0x01])
spi.write(write)
write=bytearray([0xF4,0x27])
spi.write(write)
CS.high()

CS.low()
write=bytearray([0xF7])
spi.write(write)
sleep_ms(10)
rBuff = spi.read(8)
CS.high()

pressure = (rBuff[0] << 12) |(rBuff[1] << 4) | (rBuff[2] >> 4)
temperature = (rBuff[3] << 12) | ( rBuff[4] << 4) | (rBuff[5] >> 4)
humidity = rBuff[6] << 8 | rBuff[7]

print("Humidity = ", humidity)
print("Pressure = ", pressure)
print("Temp. = ", temperature)
