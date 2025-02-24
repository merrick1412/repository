from concurrent.futures import ThreadPoolExecutor



def sums(nums):
    return sum(nums)



def main():
    numbers = [1,2,3,4,5,6,7,8,9,10,]
    num_threads = 5
    chunk_size = len(numbers) // num_threads

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i in range(0, num_threads, chunk_size):
            futures.append(executor.submit(sums, numbers[i:i+2]))
        total_sum = sum(future.result() for future in futures)
    print(f"the sum is: {total_sum}")

if __name__ == "__main__":
    main()
