# Chugga Chugga

* [`chugga_chugga.tgz`]
  * [`chugga`](./chugga)

## Tools

* IDA 7.0

## Description

* Analyze [`chugga`](./chugga) using IDA 7.0.
  * ![1-1](./1-1.png?raw=true)
    * It is ELF binary.
    * It is written and compiled by golang.
    * `main_main` is the main function in golang binary.
  * ![1-2](./1-2.png?raw=true)
    * Generate C-style pseudo-code.
    * A bunch of `if` statements let us know the flag.
* `pctf{s4d_chugg4_n01zez}`
