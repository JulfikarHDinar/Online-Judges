def countingSort(arr):
    res = []
    for i in range(100):
        res.append(0)
    
    for i in arr:
        temp = res[i]
        temp += 1
        res[i] = temp
    
    return res

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    for i in result:
        print(i, end=' ')
