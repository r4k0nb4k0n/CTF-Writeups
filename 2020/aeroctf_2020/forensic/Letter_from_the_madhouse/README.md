# [Letter from the madhouse]

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

## Tools

* Volatility
* file
* strings
* grep
* gpg

## Description

* `memory.dump` is MS Windows 64bit memory dump file.
  * ![1](./1.png?raw=true)
* Notice that suspicious processes are in [`pslist`](./pslist.txt).
  * `.\volatility_2.6_win64_standalone.exe -f .\memory.dmp --profile=Win7SP1x64 pslist`
  * ![2](./2.png?raw=true)
* Notice that Firefox process had been terminated.
  * `.\volatility_2.6_win64_standalone.exe -f .\memory.dmp --profile=Win7SP1x64 cmdline`
  * ![3](./3.png?raw=true)
* Dump the memory of suspicious processes.
  * ![4](./4.png?raw=true)
* Extract urls from `1240.dmp`(`firefox.exe`).
  * `strings -a 1240.dmp | grep ://`
  * ![5](./5.png?raw=true)
  * Got the suspicious link. `https://pastebin.com/QRzneSW7`
* Go to the suspicious link and get information from it.
  * It seems to be base64-encoded. [`strange_things.encoded`](./strange_things.encoded)
  * ![6-1](./6-1.png?raw=true)
  * After base64-decoding and saving it in binary, use `file` command to recognize what [`strange_things.decoded`](./strange_things.decoded) is.
  * ![6-2](./6-2.png?raw=true)
  * It is PGP RSA encrypted session key.
* To decrypt [`strange_things.decoded`](./strange_things.decoded), we have to find secret key.
  * Extract strings about PGP key from `2836.dmp`(`notepad++.exe`).
    * `strings -a 2836.dmp | grep PGP`
  * ![7-1](./7-1.png?raw=true)
  * There must be PGP private key, so find out where it is in `2836.dmp`.
    * `strings -a 2836.dmp > strings.2836.dmp`
  * ![7-2](./7-2.png?raw=true)
  * Base64-decode and save it in binary. use `file` command to recognize what [`secretkey.decoded`](./secretkey.decoded) is.
  * ![7-3](./7-3.png?raw=true)
  * It is PGP secret key.
* Decrypt [`strange_things.decoded`](./strange_things.decoded) with [`secretkey.decoded`](./secretkey.decoded).
  * `gpg --import secretkey.decoded`
  * ![8-1](./8-1.png?raw=true)
  * `gpg --decrypt strange_things.decoded`
  * ![8-2](./8-2.png?raw=true)
* `Aero{d46821ea020c13a9a42e16b03d9dcccc97e1d7fa16c8673a4ebde8597715967a}`
