# Easy as Pie!

## Summary

* Simple Privilege Escalation

## Description

* ![1](./1.png?raw=true)
  * Notice the last sentence of the problem about access control list.
* Server checks the authority of a user with access control list.
* An attacker needed to escalate privilege.
* ![2](./2.png?raw=true)
  * Just added a line to `acl.txt`, which has the authority information of files like /etc/passwd in Linux.
  * Notice that a user couldn't write `.acl.txt` and `flag.txt`.
  * Notice that there's a fake flag, too.
    * A flag string format is same as `auctf{...}`
  * So, `.acl.txt` is so much suspicious.
* ![3](./3.png?raw=true)
