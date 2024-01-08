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
main_loop:	
#accept
	mov rdi, 3
	mov rsi, 0
	mov rdx, 0
	mov rax, 43
	syscall
#fork
	mov rax, 57
	syscall
	cmp rax, 0
	jne parent
child:
#close 
	mov rdi, 3
	mov rax, 3
	syscall 
#read	
	mov rdi, 4
	mov rsi, rsp
	mov rdx, 512
	mov rax, 0
	syscall	
	mov r8, rax
#find filepath
	mov al, [rsp]
	mov cl, [rsp]
	jmp loop_1_end
loop_1_start:
	inc rsp
	dec r8
	mov al, [rsp]
loop_1_end:
	cmp al, ' '
	jne loop_1_start
	inc rsp # skip ' '
	dec r8
	mov al, [rsp]
	mov r10, rsp
	jmp loop_2_start
loop_2_start:
	inc rsp
	dec r8
	mov al, [rsp]
loop_2_end:
	cmp al, ' '
	jne loop_2_start	
	mov  byte ptr [rsp] ,0
	cmp cl, 'P'
	je POST
GET:
#GET_open_for_read	 
	lea  rdi, [r10]
	mov rsi, 0
	mov rax, 2
	syscall
#GET_read
	mov rdi, 3
	lea rsi, [rsp]
	mov rdx, 1000
	mov rax, 0
	syscall
	mov r10, rax
#Con_close
	mov rdi, 3
	mov rax, 3
	syscall
#COn_write_common
	mov rdi, 4
	lea rsi, [rip + response]
	mov rdx, 19
	mov rax, 1
	syscall	    
#GET_write response
	mov rdi, 4
	lea rsi, [rsp]
	mov rdx, r10
	mov rax, 1
	syscall
	jmp exit
POST:
#POST_open_for_write
	lea rdi, [r10]
	mov rsi, 0100|01
	mov rdx, 0777
	mov rax, 2
	syscall
#POST_cal_len:
	mov al, [rsp]
	jmp loop_3_end
loop_3_start:
	inc rsp
	dec r8
	mov al, [rsp]
loop_3_end:
	cmp al, 'L'
	jne loop_3_start
	jmp loop_4_end
loop_4_start:
	inc rsp
	dec r8
	mov al, [rsp]
loop_4_end:
	cmp al, '\n'
	jne loop_4_start
	inc rsp
	dec r8
	mov al, [rsp]
	jmp loop_5_end
loop_5_start:
	inc rsp
	dec r8
	mov al, [rsp]
loop_5_end:
	cmp al, '\n'
	jne loop_5_start
	inc rsp
	dec r8
#POST_wirte
	mov rdi, 3
	lea rsi, [rsp]
	mov rdx, r8
	mov rax, 1
	syscall
#Con_close
	mov rdi, 3
	mov rax, 3
	syscall
#COn_write_common
	mov rdi, 4
	lea rsi, [rip + response]
	mov rdx, 19
	mov rax, 1
	syscall	
exit:
#exit
	mov rdi, 0
	mov rax, 60
	syscall

parent:
#close
	mov rdi, 4
	mov rax, 3
	syscall	
#accept
#	mov rdi, 3
#	mov rsi, 0
#	mov rdx, 0
#	mov rax, 43
#	syscall
	jmp main_loop
#exit
#	mov rdi, 0
#	mov rax, 60
#	syscall

.section .data
sockaddr_in:
	.2byte 2
	.2byte 0x5000
	.4byte 0
	.8byte 0
response:
	.ascii "HTTP/1.0 200 OK\r\n\r\n"

