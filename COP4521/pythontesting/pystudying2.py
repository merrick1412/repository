import multiprocessing
import math

def primenumfind(x,y):
    for num in range(x,y):
        isprime = True
        if num < 2:
            continue
        
        for number in range(2,num-1):
            if (num % number == 0):
                isprime = False
                break
        if isprime:
            print(f"{num} is prime")
if __name__ == "__main__":
    processes = []
    amnt = int(input("up to what number do you want to see primes? 50 min"))
    numofthreads = amnt // 50 + (1 if amnt % 50 != 0 else 0)
    for i in range(numofthreads):
        start = i * 50
        end = min((i + 1) * 50,amnt)

        p = multiprocessing.Process(target=primenumfind, args=(start,end))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

