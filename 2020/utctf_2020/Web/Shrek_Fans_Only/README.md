# Shrek Fans Only

```text
Shrek seems to be pretty angry about something, so he deleted some important information off his site. He murmured something about Donkey being too *committed* to infiltrate his swamp. Can you *checkout* the site and see what the *status* is?
```

## Background Knowledges

* [File inclusion vulnerability - Wikipedia](https://en.wikipedia.org/wiki/File_inclusion_vulnerability)
* [Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
  * Git is a content-addressable filesystem.

## Tools

* `wget`
* `base64`
* `zlib-flate`

## Description

* Analyze [link](http://3.91.17.218/)
  * ![1-1](./1-1.png?raw=true)
    * `getimg.php?img=aW1nMS5qcGc=`
    * `echo aW1nMS5qcGc= | base64 --decode` -> `img1.jpg`
    * File-inclusion vulnerable.
* Get git commit history.
  * ![2-1](./2-1.png?raw=true)
    * To get flag, we have to find difference between `759be9 Initial commit` and `976b62 remove flag`.
  * ![2-2](./2-2.png?raw=true)
    * Follow the tree object of each commit object.
    * SHA-1 sum of `index.php` is different. This means that there are changes.
    * Flag must be deleted from `index.php`.
  * ![2-3](./2-3.png?raw=true)
    * Follow the blob object of `index.php` in `759be9 Initial commit`.
    * The flag shows up.
* `utflag{honey_i_shrunk_the_kids_HxSv03jgkj}`
