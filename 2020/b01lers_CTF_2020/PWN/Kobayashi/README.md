# Kobayashi

## Summary

* Format String Bug (x86)

## Tools

* pwndbg
* IDA 7.0

## Description

* Vulnerability
  * If enter by the following order, it's possible to exploit FSB!
    * `2 -> Nayota -> 1 -> Scotty -> 1 -> Janice -> 1 -> Leonard`
  * ![1](./1.png?raw=true)
    * Be able to enter 19 bytes and trigger the format string bug, but it's useless to overwrite the return address since it calls exit().

* Exploit
  * In my case, overwrited `exit@got` with `0x804AACD` because I thought it needs to enter several times using FSB.
  * Memory Leak
    * Fortunately, there's a stdin address in stack so it's simple to get libc base address.
    * ![2](./2.png?raw=true)
    * enter `"%2$p"` and calculate offset!
  * Get shell
    * I used one shot at `fileno@got`.
      * I had a hard time finding a function to match the constraints :(
  * [`ex.py`](./ex.py)

* `pctf{r3Pr0gr4mM1ng_tH3_Gam3_1z_th3_0nly_s0lut10n}`