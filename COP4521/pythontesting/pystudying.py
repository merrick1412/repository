import multiprocessing
import math
import sys
def calc_factorial(num):
    result = math.factorial(num)
    print(f"factorial of {num} is {result}")

if __name__ == "__main__":
    nums = [1,2,3,5,7,3024]
    sys.set_int_max_str_digits(1000000)
    processes = []
    for num in nums:
        process = multiprocessing.Process(target=calc_factorial, args=(num,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    print("calcs completed")
