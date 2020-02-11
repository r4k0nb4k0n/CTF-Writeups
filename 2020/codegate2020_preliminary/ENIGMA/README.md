# [ENIGMA](http://ctf.codegate.org/main/context.php?no=5)

```text
Challenge : ENIGMA

Description :
(fixed-point challenge)

DOWNLOAD :
http://ctf.codegate.org/099ef54feeff0c4e7c2e4c7dfd7deb6e/4728ce19e1498b50384b3b392ab22ebe

point : 49
```

## Summary

* Cryptography.

## Background Knowledges

* [치환 암호 - 위키 백과](https://ko.wikipedia.org/wiki/%EC%B9%98%ED%99%98_%EC%95%94%ED%98%B8)
* [암알못의 암호핥기 - 치환암호](https://bpsecblog.wordpress.com/2016/08/03/amalmot_2/)
* [How to Solve Simple Substitution Ciphers](https://www.instructables.com/id/How-to-Solve-Simple-Substitution-Ciphers/)
* [Cryptogram - Wikipedia](https://en.wikipedia.org/wiki/Cryptogram)

## Description

* Unlike the name of this callenge **`ENIGMA`**, [`enigma_touched`](./enigma_touched) looks like **simple substitution cipher**... BUT it was wrong.
  * ![1](./1.png?raw=true)
* With some efforts, substitution table comes up.
  * Some characters don't match theirs subsitution because of enigma cipher.
  * **Notice that spaces, numbers and special characters are not encrypted**.
  * ![2](./2.png?raw=true)
* With the subtitution table, we can get broken flag.
  * ![3](./3.png?raw=true)
* We can get stable flag like solving cryptogram.
  * ![4](./4.png?raw=true)
* `CODEGATE2020{HACKERS ARE NOT BORN ONLY IT IS MADE}`
