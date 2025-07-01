from utime import sleep_ms
from machine import Pin,I2C
from time import sleep

def crcCheck(msb, lsb,check):
    data32 = (msb << 16)|(lsb <<8)| check
    divisor = 0x988000
    for i in range(16):
        if data32 & 1<<(23 - i):
             data32 ^= divisor
        divisor>>= 1
    return data32

i2c0=I2C(0,scl=Pin(5),sda=Pin(4),freq=400000)
buf = bytearray([0xE3])
i2c0.writeto( 0x40, buf, False)
read= i2c0.readfrom(0x40, 3, True)
msb = read[0]
lsb = read[1]
check = read[2]
print("msb lsb checksum =", msb, lsb, check)
data16= (msb << 8) |  (lsb & 0xFC)
temp = (-46.85 +(175.72 * data16 /(1<<16)))
print("Temperature C ", temp)
print("Checksum=",crcCheck(msb,lsb,check))

buf = bytearray([0xF5])
i2c0.writeto( 0x40, buf, True)
read=bytearray(3)
while True:
    sleep_ms(1)
    try:
        i2c0.readfrom_into(0x40,read, True)
        break
    except:
        continue
msb = read[0]
lsb = read[1]
check = read[2]
print("msb lsb checksum =", msb, lsb, check)
data16 = (msb << 8) | (lsb & 0xFC)
hum = -6 + (125.0 * data16) / 65536
print("Humidity ", hum)
print("Checksum=",crcCheck(msb,lsb,check))
