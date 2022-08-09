cnt = input()
listA = input().split()
cmdCnt = int(input())

A = set(listA)
for i in range(cmdCnt):
  string = input().split()
  if string[0] == 'intersection_update':
    listB = input().split()
    B = set(listB)
    A.intersection_update(B)

  elif string[0] == 'update':
    listB = input().split()
    B = set(listB)
    A.update(B)

  elif string[0] == 'symmetric_difference_update':
    listB = input().split()
    B = set(listB)
    A.symmetric_difference_update(B)

  elif string[0] == 'difference_update':
    listB = input().split()
    B = set(listB)
    A.difference_update(B)
  
sum = 0
for i in A:
  sum = sum + int(i)
print(sum)