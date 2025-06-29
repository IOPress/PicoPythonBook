from machine import Pin, PWM, mem32
import array
import math

def pwm_get_wrap(sliceNo):
    PWM_BASE=0x400a8000 # 0x40050000 pico
    CH1_CSR=0x14
    Addr = PWM_BASE +0x10+CH1_CSR*sliceNo    
    return (mem32[Addr])

wave = array.array('H', [0]*256)
for i in range(256):
    wave[i] = int(65535//2 + 
           (math.sin(i * 2.0 * 3.14159 / 255.0) * 65535//2))

pwm16 = PWM(Pin(16))
pwm16.freq(125000000//256)

print(pwm_get_wrap(0))
while(True):
    for i in range(256):
        pwm16.duty_u16(wave[i])
