# [LOL](http://ctf.codegate.org/main/context.php?no=20)

```text
Challenge : LOL

Description :
(fixed-point challenge)

Find the key in gif file

DOWNLOAD :
http://ctf.codegate.org/099ef54feeff0c4e7c2e4c7dfd7deb6e/a25d7f636b538ec7d456bda96828164f

point : 27
```

## Summary

* Forensic. Steganography.

## Background Knowledges

* [Steganography - Wikipedia](https://en.wikipedia.org/wiki/Steganography)
* [JPEG File Interchange Format - Wikipedia](https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format)
  * [File format structure](https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format#File_format_structure)
    * Start of Image : `FF D8`
    * End of Image : `FF D9`

## Tools

* HxD
* Python script.

## Description

* Notice that the file extension is wrong. It is jpeg file.
  * ![1](./1.png?raw=true)
* Found 9 matches of `FF D8` and `FF D9`. This means that there are 8 jpeg files more in one jpeg file.
  * ![2-1](./2-1.png?raw=true)
  * ![2-2](./2-2.png?raw=true)
* Extract 9 jpeg files from `Legend.gif` using [`extract.py`](./extract.py)
* Here is the picture where the flag is hidden.
  * ![extracted.7](./extracted.7.jpeg?raw=true)
* `CODEGATE2020{J!n*_L00s3_C@^^0^}`
