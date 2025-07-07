from rp2 import Flash
import os
flash=Flash()
os.umount("/")
print(flash.ioctl(4,0))
print(flash.ioctl(5,0))
flash.ioctl(6,0)
flash.writeblocks(0,b"Hello World")
buf=bytearray(25)
flash.readblocks(0,buf)
print(buf)