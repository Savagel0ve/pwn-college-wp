import subprocess

command= ['/challenge/babyrev_level22.1']

data = bytearray()

with open('res.txt', 'w') as file:
    file.write('')

values = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
exit_fun = [0x31, 0x40, 0x80]
JMP_OR_IMM = [0x20, 0x40]
SYS = [0x1, 0x2, 0x4, 0x10, 0x80]
STM = [0x1, 0x2, 0x4, 0x8, 0x10]
SYS_WRITE = [0x1, 0x2, 0x4, 0x10, 0x80]
REG_B = [0x1, 0x4, 0x10, 0x20, 0x40, 0x80]
for i in JMP_OR_IMM:
    for j in values:
        data.append(0x39)
        data.append(j)
        data.append(i)
        for k in exit_fun:
            data.append(k)
        print(data)
        try:
            res = subprocess.run(command,input=data,stdout=subprocess.PIPE, stderr=subprocess.PIPE,timeout=2)
            with open('res.txt','ab') as file:
                file.write(bytes(hex(j)+hex(i),encoding='ascii'))
                file.write(res.stdout[1074:])
        except subprocess.TimeoutExpired:
                print("timeout",data)
        data.clear()
