import base64
from Crypto.Util.Padding import pad
from pwn import *

p = process('/challenge/run')
flag = bytearray()
p.recvuntil(b'ciphertext (hex):')


for i in range(1,59):
        pad_text = base64.b64encode(b'a'*(6+i))
        p.sendline(pad_text)
        p.recvuntil(b'ciphertext (hex):')
        recvline = p.recvline()
        print('recvline: ',recvline)
        target = recvline.split(b' ')[-2-int(i/16)]
        print('target: ',target)
        for c in range(0,256):
                force_text = pad(bytearray([c]) + flag,16)
                print(force_text)
                input = base64.b64encode(force_text[:16])
                p.sendline(input)
                p.recvuntil(b'ciphertext (hex):')
                recvline = p.recvline()
                print('recvline: ',recvline)
                cmp = recvline.split(b' ')[1]
                print("cmp: ",cmp)
                if(cmp == target):
                        flag = bytearray([c]) + flag
                        print(flag)
                        break
        
print('flag: ',flag)
