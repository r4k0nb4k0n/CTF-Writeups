"""
CODEGATE2020{e__A___A___A___A___A__}
mov
f974 2b9d 4caf bee1 fc0d 6e48 e03c d322 1979 36d6 40e8 cbf7 dead 0000
loop
imul 0x2
dead -> bd5a, 63f7 -> c7ee
xor 0xbd5a, c7ee
dead -> 63f7, 63f7 -> a419
imul 0x2
0000 -> 0000, 0001 -> 0002
add 0x1000
0000 -> 1000, 0002 -> 1002
add 0x0000, 0x0002
400c -> 400c, 400c -> 400e
mov 63f7, a419
xor 63f7, a419
657b('{e') -> 068c, 707a('') -> d463
add 068c, d463
f974 -> 0000, 2b9d -> 0000
add 0001
0000 -> 0001

CODEGATE2020{e__A___A___A___A___A__}
mov
f974 2b9d 4caf bee1 fc0d 6e48 e03c d322 1979 36d6 40e8 cbf7 dead 0000
loop
imul 0x2
dead -> bd5a, 63f7 -> c7ee
xor 0xbd5a, c7ee
dead -> 63f7, 63f7 -> a419
imul 0x2
0000 -> 0000, 0001 -> 0002
add 0x1000
0000 -> 1000, 0002 -> 1002
add 0x0000, 0x0002
400c -> 400c, 400c -> 400e
mov 63f7, a419
xor 63f7, a419
657b('{e') -> 068c, 707a('') -> d463
add 068c, d463
f974 -> 0000, 2b9d -> 0000
add 0001
0000 -> 0001
"""

hashes = [0xf974, 0x2b9d, 0x4caf, 0xbee1, 0xfc0d, 0x6e48, 0xe03c, 0xd322, 0x1979, 0x36d6, 0x40e8, 0xcbf7]

flag = "CODEGATE2020"

a = 0xdead
for x in hashes:
  a_1 = (a * 0x2) & 0x0000ffff
  a_2 = a ^ a_1
  for i in range(0x0, 0xffff+1):
    if (x + i) & 0x0000ffff == 0x0:
      b = a_2 ^ i
      flag += chr(b & 0x00ff)
      flag += chr((b & 0xff00) >> 8)
      break
  a = a_2

print(flag)
