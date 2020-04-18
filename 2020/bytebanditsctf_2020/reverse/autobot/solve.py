"""
nc pwn.byteband.it 6000
"""

from pwn import *
import base64

p = remote("pwn.byteband.it", 6000)

while True:
  encoded = p.recvline()
  encoded = encoded.lstrip().rstrip()
  if len(encoded) < 100:
    print(encoded) # print flag
    break
  decoded = base64.b64decode(encoded)

  twisted = ""
  indexes = []

  twisted = decoded[0xAA8:0xAA8+300]
  twisted = "".join(chr(int(x)) for x in twisted)
  print(twisted)
  length = int(decoded[0x95A])
  target = 0x7F4 # the position of `0xC7` mov instruction.
  for i in range(length):
    if int(decoded[target+1]) == 0x85:
      indexes += [int(decoded[target+6])]
      target += 0xA
    elif int(decoded[target+1]) == 0x45:
      indexes += [int(decoded[target+3])]
      target += 0x7

  print(indexes)
  print(length)

  solved = "".join(twisted[index % (length + 1)] for index in indexes)
  solved = solved
  print(solved)

  p.sendline(solved)

