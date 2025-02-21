def count(s):
    alphacount = sum(c.isalpha() for c in s)
    numcount = sum(c.isdigit() for c in s)
    return alphacount, numcount


def main():
    inputstr = input("Enter a string: ")
    alphacount, numcount = count(inputstr)

    print (f"alpha count: {alphacount}\n")
    print(f"num count: {numcount}")
    return alphacount, numcount

if __name__ == "__main__":
    main()