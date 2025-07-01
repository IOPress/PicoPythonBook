from utime import sleep_ms
from machine import Pin,I2C
from time import sleep

i2c0=I2C(0,scl=Pin(5),sda=Pin(4),freq=400000)

buf = bytearray([0xE3])
#i2c0.writeto( 0x40, buf, False)
#read= i2c0.readfrom(0x40, 3, True)
read=i2c0.readfrom_mem(0x40, 0xE3, 3)
msb = read[0]
lsb = read[1]
check = read[2]
print("msb lsb checksum =", msb, lsb, check)
