"""
Name:Merrick Moncure
Date: 1/23/25
Assignmnent: Module 3: using events
Apply parallel and distributed computing to computational problems and analyze the scalability and efficiency of the solutions.Assumptions: NA
All work below was performed by Merrick Moncure
"""
import threading #enable multithreading
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
def is_valid_case(N,results,lock):
    number = 2 ** N
    divisors = count_divisors(number)
    result = divisors == N + 1
    with lock: #ensures theres no race conditions
        results.append((N, result))

def main():
    start_time = time.time()
    results = []
    threads = [] #list of threads
    lock = threading.Lock() #a lock that will prevent multiple threads writing at the same time

    for N in range(1, 16): #creating threads
        thread = threading.Thread(target=is_valid_case, args=(N,results,lock))
        threads.append(thread)
        thread.start()

    for thread in threads: #waits for all threads to be done
        thread.join()

    results.sort(key = lambda x: x[0]) #makes sure results are in correct order

    num_true = sum(1 for _, result in results if result)
    num_false = len(results) - num_true

    print("N T/F")
    for N, result in results:
        print(f"{N} {int(result)}")
    print(f"Num True: {num_true}")
    print(f"Num False: {num_false}")
    print(f"Elapsed time: {time.time() - start_time}")

if __name__ == "__main__":
    main()