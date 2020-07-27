# XCorp

```text
XCorp (Network, Baby, 50 pts)
Author: Artur Khanov (@awengar)

We got into the XCorp network and captured some traffic from an employee's machine. Looks like they were using some in-house software that keeps their secrets.

xcorp.tar.gz
```

## Summary

* Packet analysis
* .Net Decompile

## Tools

* Wireshark
* dnSpy

## Description

* Most used protocol in this .pcap file is SMB2.
  * ![1](./1.png?raw=true)
  * `u17ra_h4ck3r` authenticate succesfully while other users keep failing.
* `u17ra_h4ck3r` keeps requesting `net10.exe` file.
  * ![2](./2.png?raw=true)
  * The longest requested length is 22528 bytes.
  * And its response data is x86 .Net Assembly file.
* We can decompile .Net Assembly file with dnSpy.
  * ![3](./3.png?raw=true)
  * If we enter correct username, we get decrypted flag.
* `u17ra_h4ck3r` would be plausible username I think.
  * ![4](./4.png?raw=true)
  * `cybrics{53CuR1tY_N07_0b5CuR17Y}`
