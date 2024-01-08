import subprocess

command= ['/challenge/babyrev_level22.0']

data = bytearray()

with open('res.txt', 'w') as file:
    file.write('')

values = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
for i in values:
    for j in values:
        data.append(j)
        data.append(0x31)
        data.append(i)
        print(data)
        try:
            res = subprocess.run(command,input=data,stdout=subprocess.PIPE, stderr=subprocess.PIPE,timeout=2)
            with open('res.txt','ab') as file:
                file.write(bytes(hex(j)+hex(i),encoding='ascii'))
                file.write(res.stdout[1074:])
        except subprocess.TimeoutExpired:
                print("timeout",data)
        data.clear()
    data.clear()
