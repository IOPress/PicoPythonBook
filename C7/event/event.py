from utime import sleep
from machine import Pin
import machine

def gpio_get_events(pinNo):
    mask = 0xF << 4 * (pinNo % 8)
    intrAddr = 0x40014000 + 0x0f0 + (pinNo // 8)*4
    return (machine.mem32[intrAddr] & mask) >> (4 * (pinNo % 8))

def gpio_clear_events(pinNo, events):
    intrAddr = 0x40014000 + 0x0f0 + (pinNo // 8)*4
    machine.mem32[intrAddr] = events << (4 * (pinNo % 8))

pin=Pin(22,Pin.IN,Pin.PULL_UP)
while True:    
    event=gpio_get_events(22)
    if(event & Pin.IRQ_FALLING):
        print("falling")
    if(event & Pin.IRQ_RISING):
        print("rising")
    gpio_clear_events(22, Pin.IRQ_FALLING | Pin.IRQ_RISING)
    sleep(0.5)
