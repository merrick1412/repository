def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    i = len(nums) -1
    while i > 0:
        if nums[i] == nums[i-1]:
            nums.pop(i)
        i -=1
    print(nums)
    return nums

if __name__ == '__main__':
    main()