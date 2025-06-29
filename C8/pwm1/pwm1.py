from machine import Pin, PWM
pwm16 = PWM(Pin(16))
pwm17 = PWM(Pin(17))

pwm16.freq(250)

pwm16.duty_u16(65535//2)
pwm17.duty_u16(65535//4)
while(True):
    pass