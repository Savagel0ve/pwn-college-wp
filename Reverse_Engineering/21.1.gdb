starti
#set $base = 0x555555554000
set $m_base = 0
set $reg_base = 0
set $input_base = 0
set $mem_base = 0
set $enable_regs = 1
set $enable_buf = 1
set $interpret_instruction = $base + 0x1a52 

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

define show_buf
    if $enable_buf
        printf "buffer: \n"
        x/2gx $input_base
    end
end

define show_cmp_value
    printf "cmp_value: \n"
    x/2gx $cmp_value  
end


b *$interpret_instruction
commands
    set $m_base = $rdi
    set $op = $rsi
    set $reg_base = $m_base + 0x400
    set $mem_base = $m_base + 0x300
#    set $input_base = $mem_base + 0x30
#    set $cmp_value = $mem_base + 0x74 - 0xe + 1
#    printf "m_base: 0x%lx\n", $m_base
#    printf "reg_base: 0x%lx\n", $reg_base
    printf "op: 0x%lx\n", $op
    del break 1
end

b *$interpret_instruction
commands
    p_regs
    set $op = $rsi
    printf "op: 0x%lx\n", $op
#    if $op & 0x8 
#         printf "[CMP] "
#         set $pr = $rsi >> 0x10 & 0xff
#	 set $pl = $rsi >> 0x8 & 0xff
#	 printf "CMP 0x%lx 0x%lx\n",$pr,$pl
#    end
#    if $op & 0x1
#	printf "[LDM] "
#	set $mem = $rsi >> 8 & 0xff
#	printf "LDM from [0x%lx]\n", $mem
#    end
#    show_buf
#    show_cmp_value
    c
end


    
