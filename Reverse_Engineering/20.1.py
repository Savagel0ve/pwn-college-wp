from pwn import p64

add_value = p64(0x888a7b1f90ba321a)	
add_value += p64(0x72dd97bd8652)



cmp_value = p64(0xedf2c1b0af9d73ef)
cmp_value += p64(0x16c99cd0ff09)

ans = []
for i,b in enumerate(cmp_value):
    ans.append((b - add_value[i])%256)

with open('20.1','wb+') as file:
    file.write(bytearray(ans))
