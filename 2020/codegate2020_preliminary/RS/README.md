# [RS](http://ctf.codegate.org/main/context.php?no=3)

```text
Challenge : RS

Description :
ReverSe the RuSt binary.

DOWNLOAD :
http://ctf.codegate.org/099ef54feeff0c4e7c2e4c7dfd7deb6e/81866e4a863e6013f507c54c4999ddec

point : 670
```

## Summary

* Reverse Engineering.
* Find encoding algorithm.
* Decode given result.

## Tools

* pwngdb
* ghidra

## Description

* What is the purpose of this problem?
  * ![1](./1.png?raw=true)
    * Needed [`flag`]() file.
  * ![2](./2.png?raw=true)
    * [`rs`]() binary prints hex values.
  * ![3](./3.png?raw=true)
    * We should find the original string to output as [`result`]() file.
    * output: 128 byte hex values.

* Think about it.
  * I don't know [`flag`](), so I wanna know WHAT'S GOING ON WHEN THIS BINARY READ THE FILE.
    * Needed to debug and find encoding algorithm.
  * Information Required
    1. Memory address that file content was saved.
    2. Instruction address when did something at the above address.
  
* First at all, looking for memory address that file content was saved.
  * ![4](./4.png?raw=true)
    * break point at [`read()`]() and [`write()`]().
    * or [`malloc/free()`]() to observe heap memory.
  * ![5](./5.png?raw=true)
    * Notice [`$rsi`]() register.
  * ![6](./6.png?raw=true)
    * Check for the initial heap.
  * ![7](./7.png?raw=true)
  * Let's execute [`write()`]() right away. (just try)
  * ![8](./8.png?raw=true)
    * Notice [`$rsi`]() register.
  * ![9](./9.png?raw=true)
    * Check for the final heap.
    * It's same as [`$rsi`]() register.
    * The reason why hex values were not together might be because there was a copying process, such as memcpy().
  * Anyway, [`0x55555579d150`]() has original file contnet. After doing any algorithm, [`0x55555579d230`]() and [`0x55555579d260`]() have the result of encoding.
  
* Second, looking for instruction address when did something at the above address.
  * Do simple method like dividing, because the code is complex and there are many called functions.
  * ![10](./10.png?raw=true)
  * ![11](./11.png?raw=true)
    * Commands traced should go back after calling [`read()`](). So there will be [`the first moment`]() changing heap memory if the command is executed after holding breakpoint at the following command for each command(#1 ~ #9). [`The first moment`]() means that algorithm was found.
    * It's just my idea. Let me know a better method if it exists :)
    * I could find [`the first moment`]() at [`0x5555555661ec`]()(#14) in here.
    * It's just the start. Like this, do so at some commands called after the first moment. It will become closer to the address of the desired function.
  * ![12](./12.png?raw=true)
  * ![13](./13.png?raw=true)
    * after [`#2`]() instruction, change of heap was found.
  * ![14](./14.png?raw=true)
    * Notice hex values at [`0x55555579d230`]().
    * In HERE, the first moment means 0x55555555dc90.

    ```text
    call 0x55555555dc90

    ---> call 0x555555566ce0

    ------> call 0x55555555b840

    ...

    ---------------------> call 0x55555555de70

    ------------------------> call 0x55555555d7f0

    ------------------------->>> call 0x555555559570 : memcpy(0x55555579d230, fileContent, 16)

    ------------------------->>> call 0x55555555eab0 : Change file contents by one byte
    ```
  
  * ![15](./15.png?raw=true)
  * ![16](./16.png?raw=true)
    * Eventually, [`0x55555555d7f0`]() was called. This function calls 0x555555559570, [`0x55555555eab0`](). Anyway, the parameter(at [`$rsi`]()) is what I think it is seed values. The reason why memory address saved at [`$rdi`]() was not [`0x55555579d150`]() is just because of memcpy().
  
  * ![17](./17.png?raw=true)
    * [`0x55555555eab0`]() has two parameters. [`$rdi`]() and [`$rsi`]() have familiar values.
    * This function change file contents by one byte.
    * As you could see, seed values start at [`0x55555579d1c1`]() not 0x55555579d1c0.

    ```c++
    // 0x55555555eab0
    short oneByteEncode(char seedByte, char userByte) {
        short ret, sVar, uVar;
        ret = 0;
        sVar = seedByte;
        uVar = userByte;

        while (uVar) {
            if ((uVar & 1) == 1) ret ^= sVar; // XOR
            uVar = (short) uVar >> 1; // 2로 나눔
            sVar *= 2; // 2배 곱함
            if (sVar >= 0x100) sVar ^= 0x11d; // XOR
        }
        return ret;
    }
    ```
  * It's the result to decompile at [`0x55555555eab0`]().
  * IDA or ghidra provide useful abilities with searching function.
    * Name of function has offset of code like sub_aab0().
    * 0xaab0 = 0x55555555eab0 - code base address

  * Algorithm Summary
  1. Copy file content by 16 bytes. (say fileContent)
  2. One byte (= index [`i`]()) of copied data and each byte (= index [`j`]()) of seed at 0x55555579d1c1 are encoded together.
  3. Next byte (= [`i + j + 1`]()) of copied data and the value oneByteEncode() returned are encoded by XOR. oneByteEncode() is called 32 times (= length of seed values). so, the value returned is encoded 0x00 after 16 byte (= length of copied data).
  4. i++; and doing untill [`i`]() wil be 16.
  5. Finally, 48 bytes encoded data is created at address of copied data.
  6. Throw away the first 16 bytes of the data.
  7. Go back No.1 if next 16 bytes of file content exists. The current result is added at previous result.

    ```c++
    // 0x55555555d7f0
    char* sub_97f0(char *userInput, char *seedStr) {
    char *ret = 0;

    for (int k=0; userInput[k] != 0; k+=16) {
        char tmp[48];
        char result[32];
        memset(tmp,0,sizeof(tmp));
        memcpy(tmp,&userInput[k],16); // Copy file content by 16 bytes.

        for (int i=0; i<16; i++) {
            for (int j=0; j<32; j++) {
                tmp[i+j+1] ^= oneByteEncode(seedStr[j], tmp[i]);
            }
        }

        memcpy(result, &tmp[16], 32); // Throw away the first 16 bytes 
        concat(ret,result);
    }
    return ret;
    }
    ```

    * It's just my pseudo-code after debugging.

* Lastly, create algorithm for decoding!
  * Basic: [`result`]() file shows 128 bytes hex values. Now we know there's the data of 32 bytes per 16 bytes of file content after encoding. If calculating, [`128 / 32 = 4`](), so it means from 16 bytes of file content was [`copied 4 times`](). In other words, length of file content will be 64 (= 16*4).
  
  * Method: Think the other way round.

    ```python
    Seed = [
        0x74, 0x40, 0x34, 0xae, 0x36, 0x7e, 0x10, 0xc2,
        0xa2, 0x21, 0x21, 0x9d, 0xb0, 0xc5, 0xe1, 0x0c,
        0x3b, 0x37, 0xfd, 0xe4, 0x94, 0x2f, 0xb3, 0xb9,
        0x18, 0x8a, 0xfd, 0x14, 0x8e, 0x37, 0xac, 0x58
    ]
        
    def findHex(idx, target): # brute forcing
        for i in range(256): # ascii range (0~255)
            result = oneByteEncode(Seed[idx],i)
            if result == target:
                return i
        assert (1 == 0)

    def decode(data):
        assert len(data) == 32
        data = [ 0 for i in range(16) ] + data
        for i in range(15,-1,-1):
            data[i+32] = data[i+32] ^ 0x00
            data[i] = findHex(31, target=data[i+32])
            for j in range(30,-1,-1):
                data[i+j+1] ^= oneByteEncode(Seed[j],data[i])

        return data[:16]
    ```

  * Prove of Concept:

    ```text
    예제) ABCDEFGH
    출력) 91 21 70 be 6c 27 f6 aa ff 00 a2 47 a4 f6 db 24 10 43 6b a2 46 a5 ef 09 08 c8 ff b2 8d b8 58 a3

    23 d7 6d ea 5a d8 7a 41   1a 6a 4c 0f 00 07 c4 23
    d1 4b bf ea d4 c2 ef ed   9c e9 cb ff d9 df 7d 2d
    98 9a 54 12 e2 5c df 34   00 06 24 80 67 c8 ad 65

    // memory after algorithm
    23 d7 6d ea 5a d8 7a 41   1a 6a 4c 0f 00 07 c4 23
    aa f6 27 6c be 70 21 91   24 db f6 a4 47 a2 00 ff
    09 ef a5 46 a2 6b 43 10   a3 58 b8 8d b2 ff c8 08
    ```
    
  1. The last byte of 32 bytes is always encoded with 0x00 by XOR. --> Original: 0x00 ^ oneByteEncode(Seed[31], data[15]) = 0xa3 --> 0xa3 ^ 0x00 = oneByteEncode(Seed[31], data[15]) = 0xa3
  2. Get data[15] by brute forcing (=[`findHex(idx, target)`]()) with oneByteEncode(Seed[31], data[15]). The result of inverse computation is 0x1a.
  3. data[15] (= the result of No. 2) is used to calculate data[16] ~ data[46]. This data[15] is the final value.
  4. data[16] ~ data[46] (= the result of No. 3) is used to obtain the results of a previous computation process. In here, data[46] can be calculated with 0x00 by XOR, such as No. 1. Then, we'll get the final value of data[14]

  * [`script.py`](./script.py)

* `CODEGATE2020{RS_m4y_st4nd_f0r_R3v3rS1ng_RuSt_0r_R33d_S010m0n}`
