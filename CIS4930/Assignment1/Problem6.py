def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    if x > y:
        for i in range(y, 0, -1):
            if x % i == 0 and y % i == 0:
                print(f"{i} is the HCF of {x} and {y}.")
                return
    if y > x:
        for i in range(x, 0, -1):
            if x % i == 0 and y % i == 0:
                print(f"{i} is the HCF of {x} and {y}.")
                return
    if x == y:
        print(f"{x} is the HCF of {x} and {y}.")
        return
if __name__ == '__main__':
    main()