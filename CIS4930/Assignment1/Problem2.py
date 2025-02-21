def main():
    n = 1
    while n >=0:
        n = int(input("enter an integer:"))
        if n % 2 == 0:
            print("even")
        else:
            print("odd")


if __name__ == '__main__':
    main()