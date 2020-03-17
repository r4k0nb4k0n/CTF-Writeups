# Tweet Raider

## Summary

* Format String Bug (x64)

## Tools

* pwndbg
* IDA 7.0

## Description

* Vulnerability
  * ![1](./1.png?raw=true)
    * Be able to enter 280 bytes and trigger the format string bug.
    * In 64-bit, `printf()` applies the Formatter with the following order, `$rsi, $rdx, $rcx, $r8, $r9, stack, ...`.
    * If you wanna access stack, enter the formatter like `"%6$p" or "%7$p" or ...`.
  * The condition to bypass is that `v3` should be larger than 9000.
    * `v3` locates at `$rsp + 0x8`.

* Exploit
  * `%9001c%7$n`
  * ![2](./2.png?raw=true)
  * ![3](./3.png?raw=true)

* `pctf{Wh4t's_4ft3r_MAARRRZ?}`