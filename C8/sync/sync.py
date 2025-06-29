from machine import Pin, PWM
pwm16 = PWM(Pin(16))

pwm16.freq(50)

pwm16.duty_u16(65535//2)
while True:
    pwm16.duty_u16(65535//2)
    pwm16.duty_u16(65535//4)
