from utime import sleep_ms
from machine import Pin, PWM

pwm25 = PWM(Pin(17))
pwm25.freq(2000)

while True:
    for b in range(0,100):
        pwm25.duty_u16(int(65535*b*b*b/1000000))
        sleep_ms(50)
