# [Drawings on the walls]

## Summary

* Forensic. Memory.

## Background Knowledges

* [Command Reference · volatilityfoundation/volatility Wiki](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference)
  * Image Identification
    * imageinfo
  * Processes and DLLs
    * pslist
    * cmdscan
  * Process Memory
    * memdump
* [w00tsec: Extracting RAW pictures from memory dumps](https://w00tsec.blogspot.com/2015/02/extracting-raw-pictures-from-memory.html)

## Tools

* Volatility
* GIMP
* strings
* grep

## Description

* `memory.dump` is MS Windows 64bit memory dump file.
  * ![1](./1.png?raw=true)
* Notice that suspicious processes are in [`pslist`](./pslist.txt).
  * `.\volatility_2.6_win64_standalone.exe -f .\memory.dmp --profile=Win7SP1x64 pslist`
  * ![2](./2.png?raw=true)
* Notice that `C:\Users\anonym\Desktop\rickroll.jfif` had been opened with `mspaint.exe`.
  * `.\volatility_2.6_win64_standalone.exe -f .\memory.dmp --profile=Win7SP1x64 cmdline`
  * ![3](./3.png?raw=true)
* Dump the memory of suspicious processes.
  * ![4](./4.png?raw=true)
* Extract RAW picture from `2080.dmp`(`mspaint.exe`).
  * Fix the extension of file to `.data` for recognizing this file as RAW data in GIMP.
  * ![5](./5.png?raw=true)
  * `11y_g07`
* Extract strings about `11y_g07` from `2836.dmp`(`notepad++.exe`).
  * `strings -a 2836.dmp | grep 11y_g07`
  * ![6](./6.png?raw=true)
* `Aero{g00dj0b_y0u_f1n411y_g07_7h3_wh0l3_fl4g}`
