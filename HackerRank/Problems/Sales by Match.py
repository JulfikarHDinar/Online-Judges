def sockMerchant(n, arr)
    list1 = []
    cnt = 0
    for i in arr
        if i not in list1
            list1.append(i)
        else
            cnt += 1
            list1.remove(i)

    return cnt
if __name__ == '__main__'
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, arr)
    print(result)