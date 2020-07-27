# Baby Rev

```text
Baby Rev (Reverse, Baby, 50 pts)
Author: Egor Zaytsev (@groke)

I started teaching my daugther some reversing. She is capable to solve this crackme. Are you?

Download: babyrev.tar.gz

This link can be helpful: snap.berkeley.edu/offline
```

## Summary

* Code Analysis
* XOR

## Tools

* [Snap!](https://snap.berkeley.edu/snap/snap.html)

## Description

* After `tar -xvf babyrev.tar.gz`, we get [`babyrev.xml`](./babyrev.xml).
* Thanks to the link in description, we can open the file with Snap!.
  * ![1](./1.png?raw=true)
  * We can get the fact that the result of XOR calculation of each character of secret and key is 33.
* The result of XOR calculations of each character of secret and 33 would be each character of key.
  * ![2](./2.png?raw=true)
  * `cybrics{w3l1C0m3_@nd_G00d_lUck!}`
