from machine import Pin, PWM
from time import sleep_ms
pwm17 = PWM(Pin(17))
pwm17.freq(2000)

while True:
    for d in range(0,65535,655):
        pwm17.duty_u16(d)
        sleep_ms(50)
