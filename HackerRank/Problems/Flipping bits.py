def flippingBits(n):
    binStr = format(n ,"b")         #dec to bin string
    #print(binStr+'\n')
    binLst = []
    for i in range(len(binStr)):    #replacing 1s with zero and vice versa from right
        #print(binStr[i])
        if binStr[i] == '1':
            binLst.append(0)
        elif binStr[i] == '0':
            binLst.append(1)
    #print(binLst)

    for i in range(32-len(binLst)):     #remaining leading 1s
        binLst = [1] + binLst
    
    binLst = ''.join(map(str, binLst))  #concating
    #print(int(binLst, 2))           #bin to dec string
    return int(binLst, 2)

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        print(result)