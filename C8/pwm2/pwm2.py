from machine import Pin, PWM, mem32
def pwm_set_phase(sliceNo,phase):
    PWM_BASE=0x400a8000 # 0x40050000 pico
    CH1_CSR=0x14
    Addr = PWM_BASE +CH1_CSR*sliceNo
    if phase:
        mem32[Addr]=mem32[Addr] | 0x2
    else:
        mem32[Addr]=mem32[Addr] & 0xFFFFFFFD 
pwm16 = PWM(Pin(16))
pwm17 = PWM(Pin(17))
pwm16.freq(250)
pwm_set_phase(0,True)
pwm16.duty_u16(65535//2)
pwm17.duty_u16(65535//4)
while(True):
    pass