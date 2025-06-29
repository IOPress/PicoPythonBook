from machine import Pin, PWM,mem32

def pwm_set_polarity(sliceNo,channel,invert):
    PWM_BASE=0x400a8000 # 0x40050000 pico
    CH1_CSR=0x14
    Addr = PWM_BASE +CH1_CSR*sliceNo
    if invert:
      mem32[Addr]=mem32[Addr] | 0x1 << (2+channel)
    else:
      mem32[Addr]=mem32[Addr] & ~(0x1<<(2+channel))


pwm16 = PWM(Pin(16))
pwm17 = PWM(Pin(17))

pwm16.freq(250)

pwm16.duty_u16(65535//4)
pwm17.duty_u16(65535//4)
pwm_set_polarity(0,1,True)

while(True):
   pass