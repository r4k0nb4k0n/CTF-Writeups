Seed = [
    0x74, 0x40, 0x34, 0xae, 0x36, 0x7e, 0x10, 0xc2,
    0xa2, 0x21, 0x21, 0x9d, 0xb0, 0xc5, 0xe1, 0x0c,
    0x3b, 0x37, 0xfd, 0xe4, 0x94, 0x2f, 0xb3, 0xb9,
    0x18, 0x8a, 0xfd, 0x14, 0x8e, 0x37, 0xac, 0x58
]

def oneByteEncode(seedByte, userByte):
    ret = 0
    sVar = seedByte
    uVar = userByte
    while uVar > 0:
        if (uVar & 1) == 1:
            ret ^= sVar # XOR
        uVar = uVar >> 1 # divide by 2
        sVar *= 2
        if sVar >= 0x100:
            sVar ^= 0x11d # XOR
    return ret


def tostr(arr):
    s = ""
    for el in arr:
        s += "%02x " % el
    return s


def debug(arr):
    for i in range(0, 64, 16):
        left = list(arr[i:i+8])
        left.reverse()
        right = list(arr[i+8:i+16])
        right.reverse()
        print tostr(left) + "  " + tostr(right)

def encode(userInput):
    maxSize = 64
    data = [0 for i in range(maxSize)]
    for i in range(len(userInput)):
        data[i] = ord(userInput[i])

    idx = 0
    result = []
    while idx < maxSize:
        if data[idx] == 0: break
        tmp = [ data[idx+i] for i in range(16) ]
        tmp += [ 0 for i in range(32) ]
        debug(tmp)
        for i in range(16):
            for j in range(32):
                tmp[i+j+1] ^= oneByteEncode(Seed[j], tmp[i])
            debug(tmp)
        
        result.append(tostr(tmp[16:]))
        idx += 16

    return ' '.join(result)

def findHex(idx, target):
    for i in range(256):
        result = oneByteEncode(Seed[idx],i)
        if result == target:
            return i
    assert (1 == 0)

def decode(data):
    assert len(data) == 32
    data = [ 0 for i in range(16) ] + data
    for i in range(15,-1,-1):
        debug(data)
        data[i+32] = data[i+32] ^ 0x00
        data[i] = findHex(31, target=data[i+32])
        for j in range(30,-1,-1):
            data[i+j+1] ^= oneByteEncode(Seed[j],data[i])
        debug(data)

    return data[:16]

def main(userInput):

    data = [ int(_byte, 16) for _byte in userInput.split(' ') ]
    ret = ''
    for i in range(0,len(data),32):
        result = decode(data[i:i+32])
        for ch in result:
            if ch > 0:
                ret += chr(ch)
    return ret

if __name__ == '__main__':
    s = raw_input("User Input: ")
    #encode("AAAAAAAA")
    #print result
    #test = "1c 60 d8 37 b2 29 f1 22 56 8c f7 92 bb e4 da df e7 a3 b3 ae 14 10 9f b6 90 2a e3 b4 8a 36 2e 3f"
    print main(s)
