# [The Legend of Hackerman Pt 2]

## Summary

* .docx File Structure

## Background Knowledges

* PNG File Signature: `89 50 4E 47 0D 0A 1A 0A`

## Description

```
Ok, I've received another file from Hackerman, but it's just a Word Document? He said that he attached a picture of the flag, but I can't find it...
```

* Where's [`a picture of the flag`]()?
    * Changed file extension `.docx` to `.zip`.
    
        ```
        $ mv Hacker.docx Hacker.zip
        $ unzip Hacker.zip
        Archive:  Hacker.zip
            inflating: _rels/.rels
            inflating: word/fontTable.xml
            inflating: word/styles.xml
            inflating: word/_rels/document.xml.rels
            inflating: word/settings.xml
            inflating: word/media/image97.png
            inflating: word/media/image102.png
            inflating: word/media/image96.png
            ...
            inflating: word/media/image37.png
            inflating: word/numbering.xml
            inflating: docProps/core.xml
            inflating: docProps/app.xml
            inflating: [Content_Types].xml
            inflating: word/document.xml
        ```

    * There are many image files.
        * Just look at.

* ![flag](./image23.png?raw=true)
