original = None
with open("Legend.gif", "rb") as f:
  original = f.read()

soi = b'\xFF\xD8'
eoi = b'\xFF\xD9'
count = 0

while (original.count(soi) > 0 and original.count(eoi) > 0):
  print(count)
  extracted = original[original.index(soi):original.index(eoi) + 2]
  with open("extracted." + str(count) + ".jpeg", "wb") as f:
    f.write(extracted)
  original = original[original.index(eoi) + 2:]
  count = count + 1
