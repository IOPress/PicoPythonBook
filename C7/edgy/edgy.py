from utime import sleep
from machine import Pin
import machine

def gpio_get_events(pinNo):
    IO_BANK0_BASE=0x40028000  #Pico 2
    INTR0=0x230 #Pico 2
  # IO_BANK0_BASE=0x40014000 #Pico
  # INTR0=0xF0 #Pico
    mask = 0xF << 4 * (pinNo % 8)
    intrAddr = IO_BANK0_BASE + INTR0 + (pinNo // 8)*4
    return (machine.mem32[intrAddr] & mask) >> (4 * (pinNo % 8))

def gpio_clear_events(pinNo, events):
    IO_BANK0_BASE=0x40028000  #Pico 2
    INTR0=0x230 #Pico 2
  # IO_BANK0_BASE=0x40014000 #Pico
  # INTR0=0xF0 #Pico
    intrAddr = IO_BANK0_BASE + INTR0 + (pinNo // 8)*4
    machine.mem32[intrAddr] = events << (4 * (pinNo % 8))

pin=Pin(22,Pin.IN,Pin.PULL_UP)

print("Press Button")
gpio_clear_events(22, Pin.IRQ_FALLING)
sleep(10)
event = gpio_get_events(22)
gpio_clear_events(22, Pin.IRQ_FALLING)
if event & Pin.IRQ_FALLING:
    print("Button Pressed")
else:
    print("Button Not Pressed")
