.global _start
_start:
.intel_syntax noprefix
push 0x66
mov rdi, rsp
push 0x4
pop rsi
push 0x5a
pop rax
syscall
