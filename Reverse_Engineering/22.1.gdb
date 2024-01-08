et $enable_regs = 1
set $interpret_instruction = $base + 0x1f1a
set $IMM = $base + 0x18e1
set $STM = $base + 0x1a36
set $SYS = $base + 0x1c53
set $flag_seed = $base + 0x12c9


b *$flag_seed
commands
    si 6
    set $rip = 0x555555555461
    c
end



b *$IMM
commands
    printf "IMM REACH op"
end

b *$STM
commands
        printf "STM REACH op"
end

b *$SYS
commands
        printf "SYS REACH op"
end
 



    

