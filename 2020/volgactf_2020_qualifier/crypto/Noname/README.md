# [Noname]

## Summary

* AES. Simple Guessing

## Description

* This problem provided 2 files, [encrypted](./encrypted), [encrypted.py](./encryptor.py)
  * The following code is of python.

    ``` python
    from Crypto.Cipher import AES
    from secret import flag
    import time
    from hashlib import md5

    key = md5(str(int(time.time()))).digest()
    padding = 16 - len(flag) % 16
    aes = AES.new(key, AES.MODE_ECB)
    outData = aes.encrypt(flag + padding * hex(padding)[2:].decode('hex'))
    print outData.encode('base64')
    ```

  * The following text is of ciphertext with base64.
  
    ``` text
    uzF9t5fs3BC5MfPGe346gXrDmTIGGAIXJS88mZntUWoMn5fKYCxcVLmNjqwwHc2sCO3eFGGXY3cswMnO7OZXOw==
    ```

* In my case, decoded `encrypted` file and just guessed the `key`.

    ``` bash
    base64 -d encrypted > base64-decoded
    ```

  * `time.time()` in python returns by seconds from system time.
  * I thought that encrypted.py would be executed at least 10 days ago, so just brute-forced.

  ``` python
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
  ```

  * [decrypted.py](./decrypted.py)
* `VolgaCTF{5om3tim3s_8rutf0rc3_i5_th3_345iest_w4y}`