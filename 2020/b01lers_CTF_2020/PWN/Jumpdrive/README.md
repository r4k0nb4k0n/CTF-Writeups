# Jumpdrive

## Summary

* Format String Bug (x64)

## Tools

* pwndbg
* IDA 7.0

## Description

* Vulnerability
  * ![1](./1.png?raw=true)
    * ![2](./2.png?raw=true)
  * In 64-bit, `printf()` applies the Formatter with the following order, `$rsi, $rdx, $rcx, $r8, $r9, stack, ...`.
    * If you wanna access stack, enter the formatter like `"%6$p" or "%7$p" or ...`.
  
* Exploit
  * ![3](./3.png?raw=true)
    * The content of flag is saved in stack. So, simply could print by FSB.
  * Just print 4 times after offset 10.
    * `"%10$p %11$p %12$p %13$p"`
  * [`ex.py`](./ex.py)

* `pctf{pr1nTf_1z_4_St4R_m4p}`