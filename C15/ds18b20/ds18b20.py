from machine import Pin
import onewire,ds18x20
ow = onewire.OneWire(Pin(2))
presence=ow.reset() 
if presence:
    print("Device present")
else:
    print("No device")

DS=ds18x20.DS18X20(ow)
roms=DS.scan()
DS.convert_temp()

print(DS.read_temp(roms[0]))
