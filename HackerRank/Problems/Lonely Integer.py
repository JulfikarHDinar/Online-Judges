def lonelyinteger(a):
    dict1 = {}
    for i in a:
        cnt = a.count(i)
        if cnt == 1:
            return i


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)

