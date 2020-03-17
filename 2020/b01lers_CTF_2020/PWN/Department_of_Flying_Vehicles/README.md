# Department of Flying Vehicles

## Summary

* Stack Overflow

## Tools

* pwndbg
* IDA 7.0

## Description

* Vulnerability
  * ![1](./1.png?raw=true)
    * `gets()` doesn't check a boundary of input.
    * In addition, there's a helper function, `orange box`.
    * The condition, which an attacker has to bypass, is that `v6` should be equals to XOR operation of `v7` and `s1`.
      * `s1` is a user input. `v6` and `v7` is given.
      * `v7 ^ s1 = v6 --> v7 ^ v6 = s1`, but `s1` shouldn't be "COOLDAV\x00".
        * by A ^ B = C --> A ^ C = B --> B ^ C = A.
    * But, `v6` and `v7` locate at the higher address than `s1` in stack memory.
      * It means that an attacker can overwrite `v6` and `v7`.
      * Just properly change them to satisfy the condition!
    * Notice that `gets` insert `"\x00"` at the end of an input string.

* Exploit
  * Assumed that the first byte of `v6` is `"\x00"`.
  * Payload is `changed v6` ^ `v7`.
  * [`ex.py`](./ex.py)

* `pctf{sp4c3_l1n3s_R_sh0r7!}`