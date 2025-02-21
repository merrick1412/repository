"""
Name:Merrick Moncure
Date: 1/23/25
Assignmnent: Module 3: using events
Apply parallel and distributed computing to computational problems and analyze the scalability and efficiency of the solutions.Assumptions: NA
All work below was performed by Merrick Moncure
"""
import math
import time

def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count
def is_valid_case(N):
    number = 2 ** N
    divisors = count_divisors(number)
    return divisors == N + 1

def sequential_solution():
    start_time = time.time()
    results = []
    for N in range(1, 16):
        result = is_valid_case(N)
        results.append((N,result))

    num_true = sum(1 for _, result in results if result)
    num_false = len(results) - num_true

    print("N T/F")
    for N,result in results:
        print(f"{N} {int(result)}")

    print(f"Num True: {num_true}")
    print(f"Num False: {num_false}")
    print(f"Elapsed time: {time.time() - start_time}")


if __name__ == "__main__":
    sequential_solution()