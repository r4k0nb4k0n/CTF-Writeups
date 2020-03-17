# Black Hole

## Summary

* Stack Overflow

## Tools

* pwndbg
* IDA 7.0

## Description

* Vulnerability
  * ![1](./1.png?raw=true)
    * Not checked a boundary of the local variable, `name`.
    * Be able to keep entering characters.
    * The local variable, `v5`, is an index of the `name` array, but a user could be overwrite it.
      * What if changed to the location of the return address? Just exploit.
  * In addition, there's a helper function.
    * ![2](./2.png?raw=true)

* Exploit
  * It needs to exploit with ROP gadgets, since the helper function, `win()`, just returns the content of file.
    * After calling `readFile()` in win(), `$rdi` has the pointer of flag string, so then simply calls puts().
  * [`ex.py`](./ex.py)

* `pctf{th1s_l1ttle_man0uver_just_c0st_us_51_y34r5}`