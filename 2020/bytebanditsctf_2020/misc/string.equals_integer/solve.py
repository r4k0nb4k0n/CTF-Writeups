"""
string.equals(integer)
481
Someone gave me two functions to convert strings into integers. I converted some strings to the integers and noted them down. Can you help me converting the concatenation of those strings in the order mentioned in the file hashes.txt into integers?

The answer for this is the multiplication of output of both the functions for the concatenated string. (Wrap the number around flag{})
"""

mod = int(1e9 + 7)
mod2 = int(1e9 + 9)
import random

f = open("hashes.txt", "r")
hashes = f.read().rstrip().split("\n")
hashes = [(int(_hash.lstrip().rstrip().split(' ')[0]), int(_hash.lstrip().rstrip().split(' ')[1])) for _hash in hashes]
touched = {}
for _hash in hashes:
  touched[_hash] = 0
f.close()

def func1(s):
  h = 0
  for i in range(len(s)):
    h += (ord(s[i]) - 96) * pow(31, i, mod)
    h %= mod
  return h


def func2(s):
  h = 0
  for i in range(len(s)):
    h += (ord(s[i]) - 96) * pow(31, i, mod2)
    h %= mod2
  return h


saa = ""

# Generate all permutations of x, a, b -> s[a - 1: b]
payloads = []
for x in range(20):
  print(x)
  f = open("a/" + str(x))
  s = f.read()
  for a in range(1, 1000 + 1):
    for b in range(a, a + 100 + 1):
      payloads += [s[a - 1 : b]]
  f.close()

def main():
  progress = 0
  for payload in payloads:
    ha1 = func1(payload)
    ha2 = func2(payload)
    if touched.get((ha1, ha2)) is not None and touched.get((ha1, ha2)) == 0:
      touched[(ha1, ha2)] = payload
      progress += 1
      print(str(progress) + " / 10000")
  s = "".join([touched[_hash] for _hash in hashes])
  hsh1 = func1(s)
  hsh2 = func2(s)
  print(hsh1, hsh2, hsh1 * hsh2)
  print("flag{" + str(hsh1 * hsh2) + "}")

if __name__ == "__main__":
    main()
