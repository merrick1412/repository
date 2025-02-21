#############################################                                         
#                                           #
#     Name: Merrick Moncure                 #
#     Class: CDA 3100                       #
#    Assignment:  #5MIPS ASSEMBLY SUM, MIN, #
# MAX, MEAN AND VARIANCE                    #
#                                           #
#############################################

.data
	array:  .float 1.0 2.0 3.0 4.0 5.0
	prompt1: .asciiz "\nEnter 5 integer numbers: "
	readnum: .asciiz "\nEnter a number: "
	iterator: .word 0
	size: .word 4
	divisor: .word 5
	printinputs: .asciiz "\nFloating Point List: "
	endl: .asciiz "\n"
	sum: .asciiz "\nThe sum of the numbers is: "
	smallest: .asciiz "\nThe Smallest number is: "
	largest: .asciiz "\nThe Largest number is: "
	mean: .asciiz "\nThe Mean of the numbers is: "
	variance: .asciiz "\nThe variance of the numbers is: "
.text
.globl main
main:
	la $a1, array #array address goes into $a1
	lw $t1, iterator #iterator initialized to 0
	lw $t2, size #sets the cap for iteration at 4, for 5 elements
	
	li $v0, 4
	la $a0, prompt1
	syscall #prints the prompt
	
	
	
	loop: #input loop
	bgt $t1, $t2, end_loop #ends if greater than 4
	
	la $a0, readnum
	li $v0, 4 
	syscall #prompting numbers
	
	li $v0, 5
	syscall
	move $t3, $v0 #user inputing integers
	
	mtc1 $t3, $f10
	cvt.s.w $f10, $f10 #converting int to float
	
	s.s $f10, ($a1) #reading the floats back into the array
	
	addi $t1, $t1, 1 #incrementing index
	addi $a1, $a1, 4 #incrementing array address
	
	
	j loop
		
	end_loop:
	
	
		
		addi $a1,$a1 -20 #resets the array address to be at 1st element
		
		li $v0, 4
		la $a0, printinputs
		syscall #printed float form of inputs
		
		lw $t1, iterator
		lw $t2, size #resets t1 and t2 to be at 0 and 4 respectively
	loop2:
		bgt $t1, $t2, end_loop2 #same iterator loop as before
		
		li $v0, 4
		la $a0, endl #prints a whitespace
		syscall
		
		li $v0, 2
		l.s $f12 ($a1) #reads the element being pointed at into $f12, which prints it out
		syscall
		
		addi $t1, $t1, 1 #incrementing index
		addi $a1, $a1, 4 #incrementing array address
		
		j loop2
		
	end_loop2:
		addi $a1,$a1 -20 #resetting the array
		
		li $v0, 4
		la $a0, sum 
		syscall #printing the sum prompt
		
		l.s $f2 0($a1)
		l.s $f4 4($a1)
		l.s $f6 8($a1)
		l.s $f8 12($a1)
		l.s $f10 16($a1) #loading each of the elements of array into float registers for math
		add.s $f20, $f2, $f4
		add.s $f20, $f20, $f6
		add.s $f20, $f20, $f8
		add.s $f20, $f20, $f10 #sums them all together
		
		li $v0, 2
		mov.s $f12, $f20
		syscall #prints sum
		
		li $v0, 4
		la $a0, endl 
		syscall #whitespace
		
		lw $t1, iterator #used iterator to set $t1 back to 0
		la $a3, iterator #loaded 0 into $a3 for cleaning out registers
		l.s $f2, ($a3)
		l.s $f4, ($a3)
		l.s $f6, ($a3)
		l.s $f8, ($a3)
		l.s $f10, ($a3)
		l.s $f20, ($a3) #cleans out the registers for use later
		
		
		lw $t2, size #loaded 4 into t2
		
		
		l.s $f2 ($a1) #using this as the first minimum to check against
		minloop:
		bgt $t1, $t2, exit #same iteration as past loops
		
		l.s $f4 ($a1) #loads in an element
		
		c.lt.s $f4, $f2 #checks the element against the f2 to see if its less than
		bc1t newmin #if the element in f4 is smaller, jumps to newmin
		
		addi $t1, $t1, 1 #incrementing
		addi $a1, $a1, 4
		j minloop #back to top
		newmin:
		mov.s $f2, $f4 #changes f2 to the new minimum
		j minloop #back to top
		
		exit: #break when done
		
		li $v0, 4
		la $a0, smallest 
		syscall
		
		li $v0, 2
		mov.s $f12, $f2
		syscall #prints out the minimum
		
		lw $t1, iterator
		la $a3, iterator
		l.s $f2, ($a3)
		l.s $f4, ($a3)
		l.s $f6, ($a3)
		l.s $f8, ($a3)
		l.s $f10, ($a3)
		l.s $f20, ($a3) #cleaned out registers again
		
		addi $a1,$a1 -20 #resets array to 1st element again
		
		lw $t2, size #loads t2 to be 4 again
		
		l.s $f4 ($a1) #similar logic as minimum loop, just uses f4
		maxloop:
		bgt $t1, $t2, exit1 #same for loop equivalent
		
		l.s $f2 ($a1) #takes element into f2 to check against f4
		
		c.lt.s $f4, $f2 #if f4 is greater, jumps to newmax
		bc1t newmax #jump if true
		
		addi $t1, $t1, 1
		addi $a1, $a1, 4 #incrementing
		j maxloop #back to top
		newmax:
		mov.s $f4, $f2 #sets the new max to check against
		j maxloop #back to top
		
		exit1: #breaks out
		
		li $v0, 4
		la $a0, largest 
		syscall
		
		li $v0, 2
		mov.s $f12, $f4
		syscall #prints max
		
		addi $a1,$a1 -20 #resets array
		
		la $a3, divisor
		l.s $f24 ($a3)
		cvt.s.w $f24 $f24 #loads in and converts 5 to a float for use in division
		l.s $f2 0($a1)
		l.s $f4 4($a1)
		l.s $f6 8($a1)
		l.s $f8 12($a1)
		l.s $f10 16($a1) #loading in all array elements
		add.s $f20, $f2, $f4
		add.s $f20, $f20, $f6
		add.s $f20, $f20, $f8
		add.s $f20, $f20, $f10 #sum
		div.s $f22, $f20, $f24 #divide by 5
		
		li $v0, 4
		la $a0, mean 
		syscall
		
		li $v0, 2
		mov.s $f12, $f22
		syscall #prints mean
		
		
		lw $t1, iterator
		lw $t2, size #resets iterator and size
		variance1:
		bgt $t1, $t2, FINALLY_OVER #same for loop logic
		l.s $f5, ($a1) #takes in 1st array element
		sub.s $f3, $f5, $f22 #subtracts the mean from it, same mean calculated before in f22
		mul.s $f3, $f3, $f3 #squares the result
		add.s $f9, $f9, $f3 #adds the result to a sum being kept in f9
		addi $t1, $t1, 1 #incrementing index
		addi $a1, $a1, 4 #incrementing array address
		j variance1 #back to top
		FINALLY_OVER: #i was frustrated
		

		
		li $v0, 4
		la $a0, variance #prints variance prompt
		syscall
		
		la $a2, size
		l.s $f15 ($a2)
		cvt.s.w $f15 $f15
		div.s $f9, $f9, $f15 #converts 4 to float, then divides sum by it
		
		li $v0, 2
		mov.s $f12, $f9
		syscall #prints variance
		
		li $v0, 10
		syscall #exit
		