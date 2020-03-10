from pwn import *

r = remote('ecb.utctf.live', 9003)
#r = process(['python', 'server.py'])


def get_hash_block(plaintext, block_idx):
	r.sendlineafter("Input a string to encrypt (input 'q' to quit):",plaintext)
	r.recvuntil(':)\n')
	ret = r.recvline()[:-1].decode()
	return ret[block_idx*32:block_idx*32+32]


def brute_force(chunk, target_block, dummy_block, block_idx):
	charset = 'utflag{}bcdehijkmnopqrsvwxyz0987654321-_:;.,`~!@#$%^&*()+=?><|ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for ch in charset:
		plaintext = chunk + ch
		while True:
			block = get_hash_block(plaintext, block_idx)
			if block != dummy_block and block != target_block:
				break
			elif block == target_block:
				log.info("Found Character: {}".format(ch))
				return ch


def find_block(plaintext, dummy_block, block_idx):
	while True:
		block = get_hash_block(plaintext, block_idx)
		if block != dummy_block:
			return block


def guess():
	plaintext = 'A'*16
	block_idx = 0
	FLAG = ''
	dummy_block = get_hash_block(plaintext, block_idx)
	while True:
		part = ''
		for i in range(1,16):
			target_block = find_block(plaintext[i:16+block_idx], dummy_block, block_idx)
			ch = brute_force(plaintext[i:] + part, target_block, dummy_block, block_idx)
			if ch is '}':
				FLAG += part + "}"
				log.info(FLAG)
				exit()
			if ch is None:
				log.info("Failed.")
				exit()
			part += ch
			dummy_block = target_block
		plaintext = 'A' + plaintext + part
		block_idx += 1
		FLAG += part


if __name__ == '__main__':
	guess()
