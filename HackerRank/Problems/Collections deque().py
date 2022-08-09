from collections import deque

cnt = int(input())
d = deque()

for i in range(cnt):
  temp = input().split()
  if temp[0] == 'append':
    d.append(temp[1])
  elif temp[0] == 'pop':
    d.pop()
  elif temp[0] == 'popleft':
    d.popleft()
  elif temp[0] == 'appendleft':
    d.appendleft(temp[1])

for i in d:
  print(i,end="")
  print(" ",end="")