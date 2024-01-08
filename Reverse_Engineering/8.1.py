from pwn import * 

arr = [ 0x3a, 0xd2, 0x43, 0x68, 0xad, 0x65, 0xbb, 0xbf, 0x72, 0x64, 0xb4, 0x75, 0x79, 0x36, 0x08, 0x4f, 0xa4, 0x75, 0x6f, 0xf0, 0x94, 0x22, 0x9c, 0x73, 0x7f, 0xed, 0x55, 0xb6, 0xf8, 0x41, 0x70, 0xf6, 0x43, 0x72, 0x68, 0x24, 0x46, 0xfd ]

arr.reverse()

for i in range(0,len(arr)):
    num = i % 7
    if num == 0:
        arr[i] = ord(xor(arr[i],0x3d))
    elif num == 1:
        arr[i] = ord(xor(arr[i],10))
    elif num == 2:
         arr[i] = ord(xor(arr[i],0x6d))
    elif num == 3:
        arr[i] = ord(xor(arr[i],0xfa))
    elif num == 4:
        arr[i] = ord(xor(arr[i],0x39))
    elif num == 5:
        arr[i] = ord(xor(arr[i],0x29))
    elif num == 6:
        arr[i] = ord(xor(arr[i],0x34))
    num = i % 6
    if num == 0:
        arr[i] = ord(xor(arr[i],0xa1))
    elif num == 1:
        arr[i] = ord(xor(arr[i],0x2e))
    elif num == 2:
        arr[i] = ord(xor(arr[i],0x28))
    elif num == 3:
        arr[i] = ord(xor(arr[i],0xf0))
    elif num == 4:
        arr[i] = ord(xor(arr[i],0x29))
    elif num == 5:
        arr[i] = ord(xor(arr[i],0x9))


print(arr)
