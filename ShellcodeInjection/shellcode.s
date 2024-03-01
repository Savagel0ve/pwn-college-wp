.global _start
_start:
.intel_syntax noprefix
push 0x66
mov rdi, rsp
mov sil, 0x4
mov al, 0x5a
syscall
