from machine import Pin, PWM, mem32

def pwm_get_wrap(sliceNo):
    PWM_BASE=0x400a8000 # 0x40050000 pico
    CH1_CSR=0x14
    Addr = PWM_BASE +0x10+CH1_CSR*sliceNo    
    return (mem32[Addr])

pwm16 = PWM(Pin(16))
pwm16.freq(125000000//4)
print(pwm_get_wrap(0))
pwm16.duty_u16(65535//2)
while(True):
    pass
