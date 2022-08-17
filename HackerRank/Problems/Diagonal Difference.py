def diagonalDifference(arr):
    j = 0
    k = len(arr) - 1
    dim1 = 0 
    dim2 = 0 
    for i in range(len(arr)):
        dim1 += arr[i][i]
        dim2 += arr[j][k]
        j+=1
        k-=1

    return abs(dim1-dim2)
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        
    #arr =[[1, 2, 3], [4, 5, 6], [9, 8, 9]]
    result = diagonalDifference(arr)
    print(result)