def main():
    needlestr = input("enter the 1st string: ")
    haystr = input("enter the 2nd string: ")
    index = needlestr.find(haystr)
    print("the index is ", index)
    return index


if __name__ == '__main__':
    main()