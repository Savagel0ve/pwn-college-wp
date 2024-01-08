.intel_syntax noprefix
.global _start

.section .text

_start:

	mov rdi, 2
	mov rsi, 1
	mov rdx, 0
	mov rax, 41
	syscall

	mov rdi, rax
	lea rsi, [rip + sockaddr_in]
	mov rdx, 16
	mov rax, 49
	syscall

	mov rdi, 3
	mov rsi, 0
	mov rax, 50
	syscall	


	mov rdi, 3
	mov rsi, 0
	mov rdx, 0
	mov rax, 43
	syscall 

	mov rdi, 0
	mov rax, 60
	syscall

.section .data
sockaddr_in:
	.2byte 2
	.2byte 0x5000
	.4byte 0
	.8byte 0
