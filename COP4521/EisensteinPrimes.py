"""
Name:Merrick Moncure
Date: 1/12/25
Assignmnent: Module 1: EisensteinPrimes
Displays all eisenstein numbers below entered number
Assumptions: NA
All work below was performed by Merrick Moncure
"""
import math


def validate_input():
    """
    check that input >0
    """
    while True:
        try:
            value = float(input("Enter a number greater than 0"))
            if value > 0:
                return int(value)
            else:
                print ("number must be > 0")
        except ValueError:
            print("invalid input. enter a number")

def is_eisenstein_prime(n):
    """

    checks if eisenstein prime
    """
    if n < 2:
        return False
    if n % 3 == 0 and n != 3:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n % 3 == 2
def find_eisenstein_primes(limit):
    """
    finds all eisenstein primes less than the limit
    """
    eisenstein_primes = []
    for num in range(2, limit):
        if is_eisenstein_prime(num):
            eisenstein_primes.append(num)
    return eisenstein_primes

def main():
    """
    exectues program
    """
    limit = validate_input()
    primes = find_eisenstein_primes(limit)
    print("eisienstein primes less than {}:".format(limit))
    for prime in primes:
        print(prime)
    prime_sum = sum(primes)
    print("the sum of the eisenstein primes is:",prime_sum)

if __name__ == "__main__":
    main()