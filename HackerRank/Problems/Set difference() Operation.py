cnt1 = int(input())
listA = set(input().split())

cnt2 = int(input())
listB = set(input().split())

print(len(listA.difference(listB)))