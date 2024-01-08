from pwn import *


context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']




gdbscript=r"""
set $enable_regs = 1
set $interpret_instruction = $base + 0x1f1a
set $IMM = $base + 0x18e1
set $STM = $base + 0x1a36
set $SYS = $base + 0x1c53
set $flag_seed = $base + 0x12c9
set $SYS_OPEN = $base + 0x1cba
set $SYS_WRITE = $base + 0x1e96
set $SYS_READ = $base + 0x1df7
set $SYS_EXIT = $base + 0x1f12

define p_regs
    if $enable_regs
            printf "a: 0x%x\n", *((char *)$reg_base)
                    printf "b: 0x%x\n", *((char *)$reg_base+1)
                            printf "c: 0x%x\n", *((char *)$reg_base+2)
                                    printf "d: 0x%x\n", *((char *)$reg_base+3)
                                            printf "s: 0x%x\n", *((char *)$reg_base+4)
                                                    printf "i: 0x%x\n", *((char *)$reg_base+5)
                                                            printf "f: 0x%x\n", *((char *)$reg_base+6)
                                                                end
                                                                end

b *$flag_seed
commands
    si 6
    set $rip = 0x555555555461
    c
end

b *$interpret_instruction
commands
    set $m_base = $rdi
    set $op = $rsi
    set $reg_base = $m_base + 0x400
    c
end



b *$IMM
commands
    printf "IMM REACH op\n"
    p_regs
end



b *$STM
commands
    printf "STM REACH op\n"
end

b *$SYS_OPEN
commands
    printf "OPNE REACH op\n"
end

b *$SYS_READ
commands
    printf "READ REACH op\n"
end

b *$SYS_WRITE
commands
    printf "WRITE REACH op\n"
end

b *$SYS_EXIT
commands
    printf "EXIT REACH op\n"
end
"""

io = gdb.debug('/challenge/babyrev_level22.0',gdbscript=gdbscript,setuid=False,aslr=False)

io.writeafter('yancode: ',b'\x40\x80\x40')
print(io.readallS())
