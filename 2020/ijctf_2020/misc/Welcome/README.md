# Welcome

```text
Author dont wanna give flag easily even its a welcome challenge, You can DM @welcome bot to get the flag but problem is he used different language(lowercase) to get the flag

Author: warlock_rootx

use !help

u know how to get the flag, use google transulater

dont sent emoji,its a diff language but input is english characters(a-z) only

ex. !flag [different language text]
```

## Summary

* OSINT
* base64 decoding

## Tools

* electron.js - Chrome Developer Tool
* Google Image Search
* Cryptii

## Description

* Try to get hint from @welcome bot.
  * ![1](./1.png?raw=true)
  * It says `Maybe check bot icon..`.
* Get the file of icon using Chrome Developer Tool.
  * ![2](./2.png?raw=true)
  * Discord is an Electron app.
  * So Chrome Developer Tool is available.
* Google the file of icon.
  * ![3](./3.png?raw=true)
  * Google says `old writing tamil`.
  * Its language is tamil.
* Say `flag` in tamil to @welcome bot.
  * ![4](./4.png?raw=true)
  * `flag` in tamil is `koti`.
  * @welcome bot gives me `SUpDVEZ7SVQkX0p1c3RfQF9TaW1wbGVfV2VsY29tZV9CMFR9`.
* Decode it.
  * ![5](./5.png?raw=true)
  * `IJCTF{IT$_Just_@_Simple_Welcome_B0T}`
