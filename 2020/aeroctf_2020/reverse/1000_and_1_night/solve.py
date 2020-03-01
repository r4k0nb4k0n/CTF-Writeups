"""

nc tasks.aeroctf.com 44324
'\x76\x72\x23\x25\x18\x23\x73\x26\x74\x27\x18\x77\x20\x26\x73\x23\x77\x25\x77\x73\x18\x27\x25\x20\x20\x74\x21\x76\x27\x23\x75\x23'



decoded = "".join([chr(((ord(x) + 8) ^ 0x17) - 7) for x in encoded])
"""

from pwn import *

p = remote("tasks.aeroctf.com", 44324)
for i in range(1001):
  if (i == 0):
    tmp = p.recvline()
    target = tmp.split(b' ')[7][1:-2].decode("utf-8")
  else:
    target = tmp.split(b' ')[8][1:-2].decode("utf-8")
  #target = "00ac8ed3b4327bdd4ebbebcb2ba10a00"
  print(target)
  encoded = b""
  operand = [0x0 for x in range(3)]
  with open(target, "rb") as f:
    content = f.read()
    encoded += content[0x12b2:0x12ba]
    encoded += content[0x12bc:0x12c4]
    encoded += content[0x12ce:0x12d6]
    encoded += content[0x12d8:0x12e0]
    operand[0] = content[0x1303]
    operand[1] = content[0x1306]
    operand[2] = (content[0x1309] ^ 0xff) + 1
  encoded = encoded.decode("ascii")
  print("encoded: " + encoded)
  decoded = "".join([chr(((ord(x) + operand[2]) ^ operand[1]) - operand[0]) for x in encoded])
  print("decoded: " + decoded)
  token = decoded
  p.sendline(token)
  tmp = p.recvline()
  print(tmp)