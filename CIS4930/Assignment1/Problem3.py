def main():
    n = int(input("Enter a number: "))
    if n == 1:
        print("not prime")
        return
    for x in range(2, n - 1):
        if (n % x) == 0:
            print("not prime")
            return
    else:
        print("prime")

if __name__ == '__main__':
    main()