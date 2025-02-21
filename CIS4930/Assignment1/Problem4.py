def main():
    x = input("Enter a number: ")
    y = input("Enter another number: ")
    
    for z in range(int(x), int(y)):
        sum = 0
        for digit in str(z):
            i = int(digit)
            sum += i*i*i
        if sum == z:
            print(z)


if __name__ == '__main__':
    main()