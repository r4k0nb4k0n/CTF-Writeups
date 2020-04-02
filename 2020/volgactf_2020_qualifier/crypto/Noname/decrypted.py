from Crypto.Cipher import AES
import time
from hashlib import md5

now = int(time.time())

f = open('base64-decoded', 'rb')
d = f.read()
target = 'VolgaCTF{'.encode()
for t in range(now-3600*24*10, now):
	key = md5(str(int(t)).encode()).digest()
	aes = AES.new(key, AES.MODE_ECB)
	outData = aes.decrypt(d)
	if outData.startswith(target):
		print(outData)
		break
	print('Failed ... t = {}'.format(t))
