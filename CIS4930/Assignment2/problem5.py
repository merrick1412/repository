
def insertval(list1,target,val):
    for x in range(len(list1)):
        if isinstance(list1[x], list):
            insertval(list1[x],target,val)
        elif list1[x] == target:
            list1.insert(x+1,val)
            return

def main():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    insertval(list1,6000,7000)
    print(list1)


if __name__ == '__main__':
    main()