from machine import Pin
import machine

def gpio_get():
    return machine.mem32[0xd0000000+0x010]

def gpio_set(value,mask): 
    machine.mem32[0xd0000000+0x010] = machine.mem32[0xd0000000+0x010] & ~mask | value & mask


pin=Pin(2,Pin.OUT)
pin=Pin(3,Pin.OUT)
pin.drive(0)
value1=1<<2 | 0<<3
value2=0<<2 | 1<<3
mask=1<<2 | 1<<3
while True:
    gpio_set(value1,mask)
    gpio_set(value2,mask)