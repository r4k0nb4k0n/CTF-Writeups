# Blind Piloting 1

## Summary

* Stack Overflow
* [How fork() works](https://www.csl.mtu.edu/cs4411.ck/www/NOTES/process/fork/create.html)

## Tools

* pwndbg
* IDA 7.0

## Description

* Vulnerability
  * ![1](./1.png?raw=true)
  * ![2](./2.png?raw=true)
    * Child process is created and calls getInput(), which has stack overflow.
    * Notice that `orange box`.
  * Also, there's a helper function.
    * ![3](./3.png?raw=true)

* Exploit
  * This binary gets all linux mitigation enable.

    ``` bash
    root@37f1d5e31052:/MOUNT/contest/b01lersCTF-2020/blind-piloting-1# checksec blindpiloting
    [*] '/MOUNT/contest/b01lersCTF-2020/blind-piloting-1/blindpiloting'
        Arch:     amd64-64-little
        RELRO:    Full RELRO
        Stack:    Canary found
        NX:       NX enabled
        PIE:      PIE enabled
    ```

  * If `canary` corrupted, this binary prints the following message.
    * ![4](./4.png?raw=true)
    * It means that whenever the message isn't printed, an attacker can guess 1 byte of `canary`.
    * Why? I thought that any child process always would copy `canary` from the parent process since fork() will make an exact copy of the parent's address space. And `canary` never change because the parent process doesn't exit.

  * But, there is one more hardship :(
    * An attacker has to guess a desired address with the return address because of `PIE enabled`.
    * An Offset of base address, LSB 12-bit, is same so an attacker could guess the address of `win()` by brute-forcing the rest 4-bit.
    * I didn't use the start address of win() because an error by system() with stack occurred.
    * So returned to `win() + 0x4`

  * [`ex.py`](./ex.py)

* `pctf{34zy_fl4g_h3r3_n0t_muc4_m0r3}`