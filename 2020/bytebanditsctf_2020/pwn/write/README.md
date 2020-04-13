# [write]

## Summary

* Arbitrary Memory Overwrite

## Tools

* pwndbg
* IDA Pro 7.0

## Description

* Vulnerability
  * ![1](./1.png?raw=true)
    * There's just `Arbitrary Memory Write` vulnerability.
    * Also, provided memory leak for puts() and stack section.
  * Notice that it's not possible to overwrite GOT section.

    ``` bash
    [*] '/MOUNT/contest/bytebandctf-2020/write/write'
        Arch:     amd64-64-little
        RELRO:    Full RELRO
        Stack:    No canary found
        NX:       NX enabled
        PIE:      PIE enabled
    ```

* Exploit
  * [`_rtld_global Overwrite`](https://dreamhack.io/learn/11#16)
    * exit() calls functions as the following order.

        ``` text
        exit()
        -->  __run_exit_handlers()
        ---->  _dl_fini()
        ------>  rtld_lock_default_lock_recursive()
        ```

    * ![2](./2.png?raw=true)
    * ![3](./3.png?raw=true)
    * `_rtld_global + 3840` refers to `rtld_lock_default_lock_recursive()`.
    * `rtld_lock_default_lock_recursive()` has one parameter, `_rtld_global + 2312`, which means `_dl_load_lock`.
    * So, if this section is overwritten, exit() would call the desired function.
    * Notice that there's _rtld_global in loader library a.k.a ld-2.27.so
      * ![4](./4.png?raw=true)
      * But could be calculated with what this binary leaks itself.
      * And get the base address of linux loader by operating with the address of puts().
    * In my case,
      * rtld_lock_default_lock_recursive(_dl_load_lock) == system("sh")

  * [`ex.py`](./ex.py)

* `flag{imma_da_pwn_mAst3r}`
