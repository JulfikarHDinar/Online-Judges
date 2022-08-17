def miniMaxSum(arr):
    minVal = min(arr)
    maxVal = max(arr)
    
    minRes = 0
    chck1 = 0
    chck2 = 0
    maxRes = 0

    for i in arr:
        if i == minVal and chck1 == 0:
            chck1 = 1
            continue
        else:
            maxRes += i

    for i in arr:
        if i == maxVal and chck2 == 0:
            chck2 = 1
            continue
        else:
            minRes += i

    print(minRes, maxRes)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)