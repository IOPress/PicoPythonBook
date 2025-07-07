from rp2 import Flash
import os

print(os.listdir("/"))
f=open("Hello.txt","wt")
f.write("Hello World")
f.close
f.flush()
print(os.listdir("/"))
f=open("Hello.txt","rt")
s=f.read()
f.close
print(s)