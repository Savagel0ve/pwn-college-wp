from pwn import *
import re

def is_subset_equal(a: int, b: int) -> bool:
    return (b | a) == b

LEVELS ={"TS": 4,
        "S": 3,
        "C": 2,
        "UC": 1}

CATEGORIES = {
        "NUC": 1,
        "NATO": 1 << 1,
        "ACE": 1 << 2,
        "UFO": 1 << 3}

p = process('/challenge/run')


for i in range(64):
    p.recvuntil('Q')
    recvline = p.recvline()
    print(recvline)
    recvline = str(recvline,encoding='utf-8')
    levels = re.findall(r'level\s([A-Z]+)',recvline)
    subject_level = LEVELS[levels[0]]
    object_level = LEVELS[levels[1]]
    categories = re.findall(r'\{([A-Z, ]*)\}',recvline)
    subject_set = 0
    object_set = 0
    for s in categories[0].split(", "):
        subject_set |= CATEGORIES[s] if s != '' else 0
    
    for s in categories[1].split(", "):
        object_set |= CATEGORIES[s] if s != ''  else 0
    
    is_read = re.findall(r'\} ([a-z]+)',recvline)[0] == 'read'
    
    is_allowed_by_level = subject_level >= object_level if is_read else object_level >= subject_level
    is_allowed = False
    if is_allowed_by_level:
        if is_read:
            is_allowed = is_subset_equal(object_set, subject_set)
        else:
            is_allowed = is_subset_equal(subject_set, object_set)
    
    ans = 'yes' if is_allowed else 'no'
    p.sendline(ans)

p.recvuntil("Here's your flag:")
p.recvline()
print(p.recvline())

