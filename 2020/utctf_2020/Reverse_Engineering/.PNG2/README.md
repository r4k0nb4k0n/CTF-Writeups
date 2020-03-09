# .PNG2

```text
In an effort to get rid of all of the bloat in the .png format, I'm proud to announce .PNG2! The first pixel is #7F7F7F, can you get the rest of the image?
```

* [`pic.png2`](./pic.png2)

## Tools

* `xxd`
* GIMP

## Description

* Use `xxd` to look inside the file.
  * ![1-1](./1-1.png?raw=true)
    * width is `0x5cf`(`1487`)
    * height is `0x288`(`648`)
    * `1487x648`
* Use GIMP to view raw data image.
  * ![2-1](./2-1.png?raw=true)
    * Open the file as Raw image data(`.data`).
  * ![2-2](./2-2.png?raw=true)
    * Set width and height.
    * And the flag shows up.
* `utflag{j139adfo_93u12hfaj}`
