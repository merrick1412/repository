# Original Code: while loop
print("while loop output")
num = 10

while num <= 50:

    is_prime = True

    divisor = 2

    while divisor <= num // 2:

        if num % divisor == 0:
            is_prime = False

            break

        divisor += 1

    if is_prime:
        print(num)

    num += 1

# Your Task: Rewrite this using a for loop
print("for loop output")
num = 10
for i in range(10, 50):
    is_prime = True
    divisor = 2
    for divisor in range(2, num // 2):
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(num)
    num += 1