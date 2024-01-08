from pwn import p64

add_value = p64(0x9493413f9a0a9c48)
add_value += p64(0x90c6075add72d4ac)
add_value += p64(0x9c2204a437ddc0a2)
add_value += p64(0xa6d5c2ad)


cmp_value = p64(0x59ed47a9d5824da0)
cmp_value += p64(0x0392e3722b1ea879)
cmp_value += p64(0x73fd023b07caf884)	
cmp_value += p64(0x62363630)

ans = []
for i,b in enumerate(cmp_value):
    ans.append((b - add_value[i])&0xff)

import IPython
IPython.embed()
