#############################################                                         
#                                           #
#     Name: Merrick Moncure                 #
#     Class: CDA 3100                       #
#    Assignment:  #6 Matrix Multiplication  #
#                                           #
#                                           #
#############################################
.data

	prompt1: .asciiz "Welcome to matrix multiplication in mips\n"
	sizeprompt: .asciiz "Please enter the size of the matrix, has to be between 2-6\n"
	wrongsize: .asciiz "The size has to be between 2 and 6! Please enter a new size\n"
	matrixprompt: .asciiz "Please enter the matrix numbers one after another:\n"
	printmatrixA: .asciiz "Matrix A is: \n"
	endl: .asciiz "\n"
	size: .word 4
	MATRIX1: .space 144 
	MATRIX2: .space 144 
	

.text
.globl main

	main:
	la $s0, MATRIX1
	la $s1, MATRIX2
	
	li $v0, 4
	la $a0, prompt1
	syscall #prints the prompt
	li $v0, 4
	la $a0, sizeprompt
	syscall #prints the prompt
	li $v0, 5
	syscall
	move $t0, $v0 #moves size into $t0
	addiu $sp,$sp,-4 #gets stack space for return address
	sw	$ra,4($sp)
	jal		SIZEVERIFICATION #sends to a input verification function
	lw $ra,4($sp) 
	addiu	$sp,$sp,4#reallocates stack space
	li $t1, 3
	addiu $sp,$sp,-4 #gets stack space for return address
	sw	$ra,4($sp)
	jal		INPUTLOOP1 #sends to the 1st input loop
	lw $ra,4($sp) 
	addiu	$sp,$sp,4 #reallocates stack space
	
	SIZEVERIFICATION:
	li $t1, 2 #makes t1 2, and t2 6 for validation
	li $t2, 6
	blt $t0,$t1,WRONGSIZE
	bgt $t0,$t2,WRONGSIZE
	jr	$ra
	WRONGSIZE:
	li $v0, 4
	la $a0, wrongsize
	syscall #prints the prompt
	j 		main #jumps to top of main to reenter size

	INPUTLOOP1:
	li $t1, 2
	bgt $t0,$t1 INPUTLOOP2 #sends to loop 2 if size is bigger than 2
	li $v0, 4
	la $a0, matrixprompt #prompts user to enter array numbers
	syscall #prints the prompt
	li $t1, 3 #initializing a counter max for the size 4 array elements, 2x2
	li $t2, 0 #the index
	
	matrixloop2x21:
		bgt $t2,$t1,endloop1 #ends if increment is greater than 3
		
		li $v0, 5
		syscall
		move $t3, $v0 #reads in number from user, then puts it in $t3
		
		sw $t3, ($s0) #saves user input into the array
		
		addi $t2, $t2, 1 #increments the index by 1
		addi $s0, $s0, 4 #increments array address by 4 for next element
		
		j matrixloop2x21 #jumps back to top of loop
		
	endloop1:
	li $v0, 4
	la $a0, printmatrixA #prompts user to enter array numbers
	
	addi $s0, $s0, -16
	
	li $t1, 3
	li $t2, 0
	
	
	li $v0, 4
	la $a0, matrixprompt #prompts user to enter array numbers
	syscall #prints the prompt
	li $t1, 3 #initializing a counter max for the size 4 array elements, 2x2
	li $t2, 0 #the index
	matrixloop2x22:
		bgt $t2,$t1,endloop2 #ends if increment is greater than 3
		
		li $v0, 5
		syscall
		move $t3, $v0 #reads in number from user, then puts it in $t3
		
		sw $t3, ($s1) #saves user input into the array
		
		addi $t2, $t2, 1
		addi $s1, $s1, 4
		
		j matrixloop2x22	
	endloop2:
	addi $s1, $s1, -16
	
	li $v0, 4
	la $a0, printmatrixA
	syscall
	li $v0, 1
	move $s0, $v0
	syscall
	addi $s0, $s0, 4
	li $v0, 1
	move $s0, $v0
	syscall
	li $v0, 4
	la $a0, endl
	syscall
	addi $s0, $s0, 4
	li $v0, 1
	move $s0, $v0
	syscall
	addi $s0, $s0, 4
	li $v0, 1
	move $s0, $v0
	syscall
	INPUTLOOP2:
	li $t1, 3
	bgt $t0,$t1 INPUTLOOP3
	INPUTLOOP3:
	li $t1, 4
	bgt $t0,$t1 INPUTLOOP4
	INPUTLOOP4:
	li $t1, 5
	bgt $t0,$t1 INPUTLOOP5
	INPUTLOOP5:
	
	
	
	
	
	
	