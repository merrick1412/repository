
def bitcount(n):
    ans = [0] * (n+1)
    for i in range(1, n+1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans

def main():
    n = 5
    result = bitcount(n)
    print(result)


if __name__ == '__main__':
    main()