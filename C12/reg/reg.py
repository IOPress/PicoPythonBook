from machine import Pin,I2C

i2c0=I2C(0,scl=Pin(5),sda=Pin(4),freq=400000)

buf = bytearray([0xE7])
i2c0.writeto( 0x40, buf, True)
read= i2c0.readfrom(0x40, 1, True)
#read=i2c0.readfrom_mem(0x40,0xE7,1)
print("User Register =",read)
