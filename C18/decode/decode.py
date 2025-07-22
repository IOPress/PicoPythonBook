#not a MicroPython program
#run on dev system to convert certs
import binascii

with open("iopress.key", 'rb') as f:
    lines = f.readlines()
lines = b"".join(lines[1:-1])
key = binascii.a2b_base64(lines)
print("key=", key)

with open("iopress.crt", 'rb') as f:
    lines = f.readlines()
lines = b"".join(lines[1:-1])
cert = binascii.a2b_base64(lines)
print()
print("cert=", cert)