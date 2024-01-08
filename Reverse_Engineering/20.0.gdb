start
set $m_base = 0
set $reg_base = 0
set $input_base = 0
set $mem_base = 0
set $enable_regs = 0
set $enable_buf = 1

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
        x/6gx $input_base
    end
end

define show_cmp_value
    printf "cmp_value: \n"
    x/6gx $cmp_value  
end

b *interpret_instruction
commands
    set $m_base = $rdi
    set $reg_base = $m_base + 0x400
    set $mem_base = $m_base + 0x300
    set $input_base = $mem_base + 0x30
    set $cmp_value = $mem_base + 0xb7 - 0x1c + 1
    printf "m_base: 0x%lx\n", $m_base
    printf "reg_base: 0x%lx\n", $reg_base
    del break 2
    c
end

b *interpret_instruction
commands
    p_regs
    show_buf
    show_cmp_value
    c
end


    
