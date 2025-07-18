from machine import Pin
import machine

def gpio_get():
    return machine.mem32[0xd0000000+0x010]

def gpio_set(value,mask): 
    machine.mem32[0xd0000000+0x010] =
         machine.mem32[0xd0000000+0x010] & ~mask | value & mask

pin=Pin(22,Pin.OUT)
pin=Pin(21,Pin.OUT)
value1=1<<22 | 0<<21
value2=0<<22 | 1<<21
mask=1<<22 | 1<<21
while True:
    gpio_set(value1,mask)
    gpio_set(value2,mask)
