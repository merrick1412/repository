def main():
    nums = [9,6,4,2,3,5,7,0,1]
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    missingnum = expected_sum - actual_sum
    print(missingnum)
    return missingnum


if __name__ == '__main__':
    main()