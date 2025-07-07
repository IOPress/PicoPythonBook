from machine import mem32
#addrGPIO = 0x40014000  #pico
addrGPIO = 0x40028000   #pico 2
value=mem32[addrGPIO]
print(bin(value))