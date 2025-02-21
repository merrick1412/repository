def main():
    inputstr = input("Enter a string: ")
    digits = [int(c) for c in inputstr if c.isdigit()]

    if not digits:
        return 0,0
    totalsum = sum(digits)
    avg = totalsum / len(digits)

    print("the sum is", totalsum)
    print ("\nThe average is: ", avg)
    return totalsum,avg

if __name__ == '__main__':
    main()