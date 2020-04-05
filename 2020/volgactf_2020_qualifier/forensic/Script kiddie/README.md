# Script kiddie

## Summary

* OVA file forensic

## Background knowledges

* OVA file
  * An OVA file is an Open Virtualization Appliance that contains a compressed, "installable" version of a virtual machine.

## Tools

* VMWare Workstation
* AccessData FTK Imager
* Wireshark

## Description

* Open `ubuntu.ova` with VMWare Workstation. It will be automatically imported.
* Open `ubuntu-disk1.vmdk` generated from `ubuntu.ova` with AccessData FTK Imager.
  * `/home/test/message`
    * ![1]
    * It looks like that data of the system was encrypted by ransomware or something.
  * `/home/test/.bash_history`
    * [`clev.py`](./clev.py) must be ransomware script.
  * `/home/prod/net_dumps/dump.pcap`
    * Network traffic had been recorded.
* Analyze [`clev.py`](./clev.py).
  * It is obfuscated.
  * It sends key to `'192.168.1.38',9999`. Look at `def t(Q)` at `class V`.
* Analyze [`dump.pcap`](./dump.pcap) with Wireshark.
  * ![2](./2.png?raw=true)
    * `ip.dst_host == 192.168.1.38 && tcp.port == 9999`
    * The packet has base64-encoded key.
      * `bVRHZWxqaERSS0FTS0toUSxGTHJzU0V2ZVFRaWxvUFJuLFhlZFhIWUJVSHBJWERCSlAsSU9HUEVyam9zeE5pUXJOTSxSenZwYkVVUkxkRmZhR0ZNLHZkQlZEQ3ZpeGpTaENRdnksRVFsY3NuVXR6Q0h5RlBITSxKa0RpamdBRmlWQldKYUx6LGdoY1BJT1NxQ2RDVHFPcEQsRG5lQ3dia0RIa29qcHBIbSxsVlJaUmVBbGFJekhnaXNjLE5kamNnVlZqaWlueGZ0Q0MsUmtnTHBSQ3FybmlicnFzTixremV3dGVBZ1BFWmRrelFKLEhucEdvVWVxY2tFcXhwUW0sTFNOV1JhclRoUmRpUExwTQ==`
      * `mTGeljhDRKASKKhQ,FLrsSEveQQiloPRn,XedXHYBUHpIXDBJP,IOGPErjosxNiQrNM,RzvpbEURLdFfaGFM,vdBVDCvixjShCQvy,EQlcsnUtzCHyFPHM,JkDijgAFiVBWJaLz,ghcPIOSqCdCTqOpD,DneCwbkDHkojppHm,lVRZReAlaIzHgisc,NdjcgVVjiinxftCC,RkgLpRCqrnibrqsN,kzewteAgPEZdkzQJ,HnpGoUeqckEqxpQm,LSNWRarThRdiPLpM`
      * Last token `LSNWRarThRdiPLpM` is the key.
* Decrypt [`secrets.txt.enc`](./secrets.txt.enc) with key `LSNWRarThRdiPLpM` by AES ECB mode.
  * ![3](./3.png?raw=true)
