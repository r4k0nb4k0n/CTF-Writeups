# [zurk]

## Summary

* Format String Bug


## Background Knowledges

* x64 format string bug

## Tools

* pwndbg
* ghidra
* [one gadget](https://github.com/david942j/one_gadget)

## Description

* Vulnerability
    * ![1](./1.png?raw=true)
        
* Exploit
    ```
    0x7fffffffe5c0:	0x7025207025207025	0x2520702520702520
    0x7fffffffe5d0:	0x2070252070252070	0x7025207025207025
    0x7fffffffe5e0:	0x0000000000702520	0x00007fffffffe600 <-- stack address
    0x7fffffffe5f0:	0x0000000000400590	0x00000000004006c2
    0x7fffffffe600:	0x00007fffffffe610	0x000000000040069e <-- ret addr of do_move()
    0x7fffffffe610:	0x0000000000400780	0x00007ffff7a2d830 <-- libc address
    0x7fffffffe620:	0x0000000000000000	0x00007fffffffe6f8
    0x7fffffffe630:	0x0000000100000000	0x0000000000400686
    0x7fffffffe640:	0x0000000000000000	0x40ba72707c501039
    0x7fffffffe650:	0x0000000000400590	0x00007fffffffe6f0
    ```
    * main() doesn't returned. (call exit())
        * So, overwrite return address of do_move() with address of welcome().
        * Then, overwrite [`0x7fffffffe610`]() with one shot gadget.
            * call stack before overwriting:
            ```
            do_move() --ret--> main() --call--> welcome() --ret--> main() --call--> ...
            ```
            * call stack after:
            ```
            do_move() --ret--> welcome() --ret--> one shot
            ```
        * [`0x7fffffffe610`]() is originally $rbp of main(), but used for return address of welcome().
    * Wrote 6 bytes divided by 3 bytes 2 times.
        * I don't know why I couldn't write 8 bytes at once :(
    * [`ex.py`](./ex.py)

* `utflag{wtf_i_h4d_n0_buffer_overflows}`