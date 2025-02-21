#############################################                                         
#                                           #
#     Name: Merrick Moncure                 #
#     Class: CDA 3100                       #
#    Assignment:  #4 Read in three numbers  #
#    and work with sum, difference, product,#
#    division and shifting.                 #
#                                           #
#############################################
	.data
		intro1:	.asciiz	"Name: Merrick Moncure. Title: Making Numbers. Description: Take in 3 numbers, add them, subtract them, multiply them, and divide them. \n"
		intro2: .asciiz "Please enter three numbers: "
		prompt1: .asciiz "Enter a number: "
		fail1: .asciiz "You cannot enter a number less than 1!!!"
		sum: .asciiz "Sum: "
		difference: .asciiz "\nDifference: "
		product: .asciiz "\nProduct: "
		quotient: .asciiz "\nQuotient: "
		remainder: .asciiz "\nRemainder: "
		shiftleft: .asciiz "\nNUM1 Shift Left 1: "
		shiftright: .asciiz "\nNUM2 Shift Right 2: "
		end: .asciiz "\nThat is the end of the program."
		NUM1: .word 1
		NUM2: .word 1
		NUM3: .word 1

	.text
	.globl main
	main:
		
		#loading in some temporary registers to represent input check
		li $t3, 1 #checking against to see if less than
		li $t4, 0 #if becomes 1, program exits

		la $t0,NUM1
		la $t1,NUM2
		la $t2,NUM3
		
		
		
		li $v0, 4 #command for printing string
		la $a0, intro1 #loading in the string
		syscall
		li $v0, 4 #command for printing string
		la $a0, intro2 #loading in another string
		syscall
		li $v0, 4 #command for printing string
		la $a0, prompt1 #loading prompt
		syscall #executing the command

		li $v0, 5 #reading in an integer
		syscall
		move $t0, $v0 #moving the input into t0

		li $v0, 4 #command for printing string
		la $a0, prompt1 #loading in the string
		syscall

		li $v0, 5 #reading in an integer
		syscall
		move $t1, $v0 #moving the input into t0

		li $v0, 4 #command for printing string
		la $a0, prompt1 #loading in the string
		syscall

		li $v0, 5 #reading in an integer
		syscall
		move $t2, $v0 #moving the input into t0

		slt $t4,$t3,$t0 #checking if less than 1 on all inputs
		slt $t4,$t3,$t1
		slt $t4,$t3,$t2

		beq $t4,$zero, ENDIF #if t4 is 0, calls endif

		add $t6,$t0,$t1
		add $t7,$t6,$t2
		li $v0, 4 #command for printing string
		la $a0, sum #loading in the string
		syscall

		li $v0, 1 #print integer
		la $a0, ($t7)
		syscall

		sub $t8,$t0,$t1
		li $v0, 4 #command for printing string
		la $a0, difference #loading in the string
		syscall
		
		li $v0, 1 #print integer
		la $a0, ($t8)
		syscall

		mul $t9,$t0,$t1
		
		mul $t6,$t9,$t2
				
		li $v0, 4 #command for printing string
		la $a0, product #loading in the string
		syscall

		li $v0, 1 #print integer
		la $a0, ($t6)
		syscall

		div $t1, $t2
		mfhi $t5 #remainder
		mflo $t7 #quotient

		li $v0, 4 #command for printing string
		la $a0, remainder #loading in the string
		syscall

		li $v0, 1 #print integer
		la $a0, ($t5)
		syscall	

		li $v0, 4 #command for printing string
		la $a0, quotient #loading in the string
		syscall

		li $v0, 1 #print integer
		la $a0, ($t7)
		syscall	

		li $v0, 4 #command for printing string
		la $a0, shiftleft #loading in the string
		syscall

		sll $t0,$t0,1
		sra $t1,$t1,2

		li $v0, 1 #print integer
		la $a0, ($t0)
		syscall	

		li $v0, 4 #command for printing string
		la $a0, shiftright #loading in the string
		syscall
		
		li $v0, 1 #print integer
		la $a0, ($t1)
		syscall	

		li $v0, 4 #command for printing string
		la $a0, end #loading in the string
		syscall
		
		li $v0, 10	 #kills the program if the input is less than one
		syscall		 #executes the code
		

		ENDIF:
		li $v0, 4	 #command for printing string
		la $a0, fail1	 #loading in the string
		li $v0, 10	 #kills the program if the input is less than one
		syscall		 #executes the code