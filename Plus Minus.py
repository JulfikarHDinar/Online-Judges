def plusMinus(arr):
    arrLen = len(arr)
    pos=0
    neg=0
    zer=0
    for i in arr:
        if i > 0:
            pos = pos + 1
        elif i < 0:
            neg = neg + 1
        elif i == 0:
            zer = zer + 1

    rat1 = pos / arrLen
    rat2 = neg / arrLen
    rat3 = zer / arrLen

    print("{:10.6f}".format(rat1)) 
    print("{:10.6f}".format(rat2)) 
    print("{:10.6f}".format(rat3)) 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
