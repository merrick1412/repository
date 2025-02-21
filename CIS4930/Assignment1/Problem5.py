def main():
    n = int(input("how many terms do you want"))
    fibonacci = [0,1]
    if n == 0:
        return
    if n == 1:
        output = fibonacci[0]
        print(output)
        return
    if n == 2:
        output = str((fibonacci[0]))
        print(output + str(fibonacci[1]))
        return
    else:
        for i in range(0, n):
            if i > 1:
                fibonacci.append((fibonacci[i-1] + fibonacci[i-2]))
        output = ' '.join(str(num) for num in fibonacci)
        print(output)



if __name__ == '__main__':
    main()