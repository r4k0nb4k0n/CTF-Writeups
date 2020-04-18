# autobot

## Summary

* Extract key information from random elf file

## Tools

* IDA 7.0

## Description

* `nc pwn.byteband.it 6000` and analyze it.
  * It gives base64-encoded ELF file.
  * And it receives password string same as the ELF file does.
* Do static analysis on the ELF file.
  * ![2-1](./2-1.png?raw=true)
    * local variables, repeat time of the loop, source key string is different in each binary.
  * ![2-2](./2-2.png?raw=true)
    * Get operand value from `mov` instruction.
  * ![2-3](./2-3.png?raw=true)
    * Get string from fixed address.
* Run [the script](./solve.py) and get flag.
  * ![3](./3.png?raw=true)
