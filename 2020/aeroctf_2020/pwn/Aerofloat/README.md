# [Aerofloat]

## Summary

* Stack Overflow

## Background Knowledges

* Vulnerability of `scanf()`
	* if enter a character when formatter is the number, such as '%d', '%lf', '%f',
		* input value is not saved.
		* And input is skipped after that.
	* But, in this case, `%lf` is used as formatter.
		* So, if enter a character, [`'.'`](), not skipped.

## Tools

* pwndbg
* ghidra
* [one gadget](https://github.com/david942j/one_gadget)

## Description

* There's 3 options.
	* ![2](./2.png?raw=true)
		* First option calls the following functions.
			* [`read(0, &ticket_id[i], 8)`]()
			* [`scanf('%lf', &rating[i])`]()
		* Second option, it's just listing.
		* Third option just prints user name.
	* **But, notice that this binary shows `memory leak` when ticket id is 8 bytes.**

* Not checked bound of arrays saving ticket id and rating.
	* ![3](./3.png?raw=true) // source code
		* It's possible to keep entering.
		* arrays is local variable.
	* [`Stack Overflow`]

* Debugging
	* ![4](./4.png?raw=true)
		* `red box` is libc address.
			* offset = 0x60 = 0x10 * 6
			* Enter dummy 6 times.
			* In case of 7th, if enter a character, [`'.'`](), as rating, be able to leak libc address.
		* `yellow box` is return address.
			* offset = 0x120 = 0x10 * 12
			* Enter dummy 5 times after `red box`.
			* In case of 13th, if enter double value equals to desired address, it's gonna move to there.
		* `green box` is index of array. Don't overwrite.
		* `purple box` is check variable. Don't overwrite.
			* if this is less than 1, call exit().

* Exploit
	* used one shot gadget.
		* ![5](./5.png?raw=true)
	* needed some utility function
	```python
	def double_to_hex(f):
    		return hex(struct.unpack('<Q', struct.pack('<d', f))[0])

	def hex_to_double(h):
    		return struct.unpack('d', h)[0]
	```
	* [`script`](./ex.py)
	* ![6](./6.png?raw=true)
