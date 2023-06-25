	.file	""
	.text
	.globl	is_prime
	.type	is_prime, @function
is_prime:
.LFB0:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	$2, -4(%rbp)
	jmp	.L2
.L5:
	movl	-4(%rbp), %eax
	movslq	%eax, %rcx
	movq	-24(%rbp), %rax
	cqto
	idivq	%rcx
	movq	%rdx, %rax
	testq	%rax, %rax
	jne	.L3
	movl	$0, %eax
	jmp	.L4
.L3:
	addl	$1, -4(%rbp)
.L2:
	movl	-4(%rbp), %eax
	cltq
	cmpq	%rax, -24(%rbp)
	jg	.L5
	movl	$1, %eax
.L4:
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	is_prime, .-is_prime
	.globl	max
	.type	max, @function
max:
.LFB1:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	-8(%rbp), %rax
	cmpq	-16(%rbp), %rax
	jle	.L7
	movq	-8(%rbp), %rax
	jmp	.L8
.L7:
	movq	-16(%rbp), %rax
.L8:
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	max, .-max
	.section	.rodata
.LC0:
	.string	"%lld"
	.text
	.globl	main
	.type	main, @function
main:
.LFB2:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	$0, -16(%rbp)
	movq	$2, -8(%rbp)
	jmp	.L10
.L12:
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	is_prime
	testl	%eax, %eax
	je	.L11
	movabsq	$600851475143, %rax
	cqto
	idivq	-8(%rbp)
	movq	%rdx, %rax
	testq	%rax, %rax
	jne	.L11
	movq	-8(%rbp), %rdx
	movq	-16(%rbp), %rax
	movq	%rdx, %rsi
	movq	%rax, %rdi
	call	max
	cltq
	movq	%rax, -16(%rbp)
.L11:
	addq	$1, -8(%rbp)
.L10:
	cmpq	$775146, -8(%rbp)
	jle	.L12
	movq	-16(%rbp), %rax
	movq	%rax, %rsi
	leaq	.LC0(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	main, .-main
	.ident	""
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
