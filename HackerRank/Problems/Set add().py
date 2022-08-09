if __name__ == '__main__':
    cnt = int(input())
    setA = {""}
    setA.discard("")  
    for i in range(cnt):
        setA.add(input())
    print(len(setA))
