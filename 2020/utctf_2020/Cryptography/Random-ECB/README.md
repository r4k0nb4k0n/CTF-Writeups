# [Random-ECB]

## Summary

* AES-ECB
* Brute force

## Background Knowledges

* [Block cipher mode of operation](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation)
	* ![1](./1.png?raw=true)
    * [`Electronic Codebook (ECB)`](): The simplest of the encryption modes
	    * A plaintext is divided into blocks. (128-bit, 256-bit, ...)
        * Each block is encrypted/decrypted separately. (i.e. independentely)
        * An only single key is used for all blocks.


## Description

* How a plaintext is encrpyted in given source code.
    ```python
    def encryption_oracle(plaintext):
        b = getrandbits(1) # 0 or 1
        plaintext = pad((b'A' * b) + plaintext + flag, 16)
        return aes_ecb_encrypt(plaintext, KEY).hex()
    ```
    * block size: 16 bytes
    * KEY is random, but not changed when the program was being executed.
    * either `plaintext + flag` or `'A' + plaintext + flag` are generated.

* How to guess the flag.
    * What if plaintext is `'A'*15`?
    * The first encrypted block is of either [`encrypt('A'*15 + flag[0])`]() or [`encrypt('A'*16)`]().
    * Be able to know the ciphertext of `'A'*15 + flag[0])` by comparing with that of `'A'*16`.
        * Then, brute-forcing one byte of flag with ascii code.
    * Keep getting the next byte of flag by shortening the length of the plaintext 'AA...A'.
        * Notice that a plaintext can becomes `'A' + plaintext`.
        * So, check if the current ciphertext is different from the previous ciphertext.
    * Also, do so in the next block.
    * [`get_flag.py`](./get_flag.py)
    
* `utflag{3cb_w17h_r4nd0m_pr3f1x}`