.intel_syntax noprefix
.global _start

.section .text

_start:
#socket
	mov rdi, 2
	mov rsi, 1
	mov rdx, 0
	mov rax, 41
	syscall
#bind
	mov rdi, rax
	lea rsi, [rip + sockaddr_in]
	mov rdx, 16
	mov rax, 49
	syscall
#listen
	mov rdi, 3
	mov rsi, 0
	mov rax, 50
	syscall	
#accept
	mov rdi, 3
	mov rsi, 0
	mov rdx, 0
	mov rax, 43
	syscall 
#read	
	mov rdi, 4
	mov rsi, rsp
	mov rdx, 256
	mov rax, 0
	syscall	
#find filepath
	mov al, [rsp]
	jmp loop_1_end
loop_1_start:
	inc rsp
	mov al, [rsp]
loop_1_end:
	cmp al, ' '
	jne loop_1_start
	inc rsp # skip ' '
	mov al, [rsp]
	mov r10, rsp
	jmp loop_2_start
loop_2_start:
	inc r10
	mov al, [r10]
loop_2_end:
	cmp al, ' '
	jne loop_2_start	
	mov  byte ptr [r10] ,0
#open	 
	lea  rdi, [rsp]
	mov rsi, 0
	mov rax, 2
	syscall
#read
	mov rdi, 5
	lea rsi, [rsp]
	mov rdx, 1000
	mov rax, 0
	syscall
	mov r10, rax
#close
	mov rdi, 5
	mov rax, 3
	syscall
#write common
	mov rdi, 4
	lea rsi, [rip + response]
	mov rdx, 19
	mov rax, 1
	syscall	
#write response
	mov rdi, 4
	lea rsi, [rsp]
	mov rdx, r10
	mov rax, 1
	syscall
#close
	mov rdi, 4
	mov rax, 3
	syscall	
#accept
	mov rdi, 3
	mov rsi, 0
	mov rdx, 0
	mov rax, 43
	syscall
#exit
	mov rdi, 0
	mov rax, 60
	syscall

.section .data
sockaddr_in:
	.2byte 2
	.2byte 0x5000
	.4byte 0
	.8byte 0
response:
	.ascii "HTTP/1.0 200 OK\r\n\r\n"
