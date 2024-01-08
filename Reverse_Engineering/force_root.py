import subprocess

command= ['sudo','strace','-o','syscall.txt','/challenge/babyrev_level22.1']

data = bytearray()

with open('res.txt', 'w') as file:
    file.write('')

values = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
for i in values:
    data.append(0x31)
    for j in values:
        data.append(0x4)
        data.append(0x1)
        print(data)
        try:
            res = subprocess.run(command,input=data,stdout=subprocess.PIPE, stderr=subprocess.PIPE,timeout=2)
            with open('res.txt','ab') as file:
                file.write(bytes(hex(j)+hex(i),encoding='ascii'))
                file.write(res.stdout[1074:])
        except subprocess.TimeoutExpired:
                print("timeout",data)
        data.pop()
        data.pop()
        break
    data.clear()
    break
