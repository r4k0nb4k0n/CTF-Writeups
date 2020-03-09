# Nittaku_3_Star_Premium

```text
One of my servers was compromised, but I can't figure it out. See if you can solve it for me!

by masond
```

## Summary

* Forensic
* Network
* Guessing

## Background Knowledges

* [Use `dig` to Perform Manual DNS Queries - Linode](https://www.linode.com/docs/networking/dns/use-dig-to-perform-manual-dns-queries/)

## Tools

* Wireshark
* `dig`
* Cryptii

## Description

* Found parts of received data in `capture.pcap`(./capture.pcap).
  * ![1-1](./1-1.png?raw=true)
    * There are base64-encoded binary data in ICMP response data.
    * It is `.gz` file, but all parts are not combined.
* Capture `ping pingable.tk` packets, get data from them and get flag.
  * ![2-1](./2-1.png?raw=true)
  * ![2-2](./2-2.png?raw=true)
  * ![2-3](./2-3.png?raw=true)
* `utflag{p1Ng@b13_f1aG$}`
