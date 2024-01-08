.intel_syntax noprefix
.global _start

.section .text

_start:

	mov rdi, 2
	mov rsi, 1
	mov rdx, 0
	mov rax, 41
	syscall
	
	mov rdi, 0
	mov rax, 60
	syscall

.section .data
