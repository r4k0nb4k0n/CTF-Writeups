# [bof]

## Summary

* Stack Overflow

## Background Knowledges

* `gets()` doesn't check a boundary of input array.

## Tools

* pwndbg
* ghidra
* [`ROPgadget`](https://github.com/JonathanSalwan/ROPgadget)

## Description

* Soooooooooo simple binary
    * ![1](./1.png?raw=true)
    * ![2](./2.png?raw=true)

* Exploit
    * ROP Chain
        ```
        ---------------- <- return address
         pop rdi ; ret
        ----------------
         0xdeadbeef
        ---------------- 
         & get_flag()
        ---------------- 
        ```
    * [`ex.py`](./ex.py)

* `utflag{thanks_for_the_string_!!!!!!}`