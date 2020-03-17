# Meshuggah 2.0

## Summary

* Type Confusion

## Tools

* pwndbg
* IDA 7.0

## Description

* Vulnerability
  * ![1](./1.png?raw=true)
  * ![2](./2.png?raw=true)
    * In C language, rand() always returns the same value in each sequence if a seed value is equal.
    * A seed value is determined by srand().
    * Notice that the local variable, `v3`, to save what time(0) returns is `Integer type`.
      * It's able to guess the seed value.
    * Guessing what rand() returns.
      * then the `count` variable can be maximum 104. (4 + 100)

* Exploit
  * Assumed that a computer time of client is similar to that of server.
  * `pwntools` supports C-lang functions in python if there's a library file.

        ```python
        c = elf.ctypes.CDLL('./libc.so.6')
        t = int(time.time()) + 2
        c.srand(t)
        print c.rand()
        ```

  * [ex.py](./ex.py)

* `pctf{Un4uT40r1z3d_uS3r_Up_1N_my_Gr1ll!_y0u_tRy1ng_to_h4cK_My_c4tCh_a_R1111de??_Unc00l_br0_Unc0o0ol!}`