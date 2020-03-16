encoded = ""
with open("result.txt", "r") as f:
  encoded = f.read()
encoded = encoded.rstrip().lstrip()
encoded = bytes.fromhex(encoded)
decoded = ""
for i in range(len(encoded)):
  if i % 2 != 0:
    decoded += chr(encoded[i] ^ 42)
  else:
    decoded += chr(encoded[i])
print(decoded)