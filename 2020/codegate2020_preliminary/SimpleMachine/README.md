# [SimpleMachine](http://ctf.codegate.org/main/context.php?no=16)

```text
Challenge : SimpleMachine

Description :
(fixed-point challenge)

Classic Check Flag Challenge Machine

DOWNLOAD :
http://ctf.codegate.org/099ef54feeff0c4e7c2e4c7dfd7deb6e/116ea16dbeabe08d1fe8891a27d0f16b

point : 333
```

## Summary

* Reverse Engineering.
* The basic of code virtualization technique.

## Tools

* HxD
* IDA 7.0
* gdb-peda

## Description

* Notice that [`simple_machine`](./simple_machine) is ELF file and [`target`](./target) is data.
  * ![1](./1.png?raw=true)
* Open [`simple_machine`](./simple_machine) with IDA 7.0, analyze, and generate some pseudo-codes.
  * ![2-1](./2-1.png?raw=true)
    * pseudo-code of `main` function.
    * Usage: `./simple_machine target`
    * There is a limitation to the length of target.
    * It uses code virtualization technique.
    * We can assume that [`target`](./target) is a kind of virtualized code script.
  * ![2-2](./2-2.png?raw=true)
    * pseudo-code of `vm_func` function.
    * There is a control function.
  * ![2-3](./2-3.png?raw=true)
    * pseudo-code of `control_func` function.
    * Fetch and decode operations from [`target`](./target).
* Based on `control_func` function, set breakpoint on and debug it.
  * ![3-1](./3-1.png?raw=true)
    * Run `gdb-peda ./simple_machine` and `b *0x80017ca`(Entry point of `control_func`).
    * Debug and understand how the program works.
  * ![3-2](./3-2.png?raw=true)
    * First operation is getting input from `stdin`.
    * 6 `ADD-CHECK` chain operations are checking if first 12 characters of input are `CODEGATE2020`.
    * Next 32 operations are generating 12 hashes, calculating XOR with input, and checking if is zero.
    * if all check is passed, print `GOOD!` to `stdout`.
    * Last operation is just exiting the program.
* Write and execute python script to get flag.
  * ![4](./4.png?raw=true)
  * [`get_flag.py`](./get_flag.py)
* `CODEGATE2020{ezpz_but_1t_1s_pr3t3xt}`
