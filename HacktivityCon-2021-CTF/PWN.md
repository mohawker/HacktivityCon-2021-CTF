# PWN
## Retcheck
### Problem Type: Buffer Overflow

We obtain the binary `./retcheck`. Running `checksec`, we note that there is no PIE, ASLR, or stack canaries. 
We decompile it in ghidra and take a look at the `main` function. 

`main()` calls another function `vuln()` and returns 0. We then look at `vuln()`

![](https://i.imgur.com/lDqDojc.png)

`vuln()` initialises two notable variables: 
- A 400 byte buffer: `local_198`
- A long variable (a mock 'stack canary') to store the return address

The program does two notable things:
- `gets` an input
-  Compares the 'stack canary' to the original return address, if they are not equal, the program will `abort()`

The program uses `gets` which is vulnerable to buffer overflow. In typical buffer overflow problems, we will be able to overwrite the RIP register, and have the program return to a different function pointer. In this challenge, ghidra  found a function `win()`, which prints out the contents of `flag.txt`. A suitable payload will be:
> "A" * 400 + `padding` + `return_address to win()`


However, the presence of the 'mock' stack canary does not allow us to do just that. 

We note that the stack canary is initialised right above the buffer, which we can also overflow. We use GDB to find the original return address, and ensure that the stack canary value is equal to the original return address - to ensure the program does not abort. Our payload is now:

> "A" * 400 + `padding` + `original_return_address` + ???

However, this would return the program to the original return address, and we will not be able to get the flag. We recall that in the `main()` function, it calls return 0.

Through experimentation on GDB, we are able to overflow the return address in the `main()` function with the following payload: 
> "A" * 400 + `8 byte padding` + `original_return_address` + `8 byte padding` + `win()_return_address`

Our final python command looks something like this: 
> `python -c 'print("A" * 408 + "\x65\x14\x40\x00\x00\x00\x00\x00" + "AAAAAAAA" + "\xe9\x12\x40\x00\x00\x00\x00\x00")'`

And we piece it together in a python script with pwntools, submit it to the challenge server. 

![](https://i.imgur.com/f714jii.png)

###### tags: `H@cktivityCon 2021 CTF`, `pwn`




 

