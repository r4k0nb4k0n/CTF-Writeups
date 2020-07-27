# Hunt

```text
Hunt (Web, Baby, 50 pts)
Author: Vlad Roskov (@mrvos)

I couldn't not make this web10

http://109.233.57.94:54040/

Shamelessly taken from © Matthew Rayfield
```

## Summary

* Javascript

## Tools

* Chrome DevTools

## Description

* When got to `http://109.233.57.94:54040/`, Google "I Am Not A Robot" Captchas fly around(They MOVE. Literally!).
  * ![1](./1.png?raw=true)
* Get the sources of this web page.
  * ![2](./2.png?raw=true)
  * function `addCaptcha()` makes a captchaBox and set its height, width, and rotation random with `Math.sin()` and `Date.now()` every 1 ms using `setTimeout()`.
* Use `clearTimeout()` to stop flying captchas.
  * ![3](./3.png?raw=true)
  * `for(let i=0;i<100000;i++) { clearTimeout(i) }`
  * We don't know the exact timeout IDs, but we can just iterate all possible timeout IDs.
  * ![4](./4.png?raw=true)
  * After stopping them, prove that I'm not a robot.
* After proving I'm not a robot...
  * ![5](./5.png?raw=true)
  * `cybrics{Th0se_c4p7ch4s_c4n_hunter2_my_hunter2ing_hunter2}`
