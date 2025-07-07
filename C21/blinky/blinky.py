from machine import mem32,Pin
from time import sleep_ms 
led=Pin(2,mode=Pin.OUT)  
addrSIO = 0xd0000000
while True:
    mem32[addrSIO + 0x018] = 1 << 2   #0x014 for Pico
    sleep_ms(500)
    mem32[addrSIO + 0x020] = 1 << 2   #0x18 for Pico
    sleep_ms(500)