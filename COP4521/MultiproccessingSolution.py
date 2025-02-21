"""
Name:Merrick Moncure
Date: 1/23/25
Assignmnent: Module 3: using events
Apply parallel and distributed computing to computational problems and analyze the scalability and efficiency of the solutions.Assumptions: NA
All work below was performed by Merrick Moncure
"""
import math
import queue
import time
import multiprocessing

def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count
def is_valid_case(N,queue):
    number = 2 ** N
    divisors = count_divisors(number)
    result = divisors == N + 1
    queue.put((N,result))

def main():
    start_time = time.time()
    queue = multiprocessing.Queue() #interprocess communication
    processes = [] #list of processes

    for N in range(1, 16): #creating processes
        process = multiprocessing.Process(target=is_valid_case, args=(N,queue))
        processes.append(process)
        process.start() #starts them

    for process in processes: #waits for all processes to be done
        process.join()

    results = []
    while not queue.empty(): #get results from queue
        results.append(queue.get())
    results = sorted(results, key=lambda result: result[0])

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