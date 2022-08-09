from collections import defaultdict

n, m = map(int,input().split())

d1 = defaultdict(list)
d2 = []
for i in range(n):
  inpA = input()
  d1[inpA].append(i+1)

for i in range(m):
  inpB = input()
  d2.append(inpB)

for i in d2:
  if len(d1[i]) != 0:
    for i in d1[i]:
      print(str(i)+' ',end='')
    print('')
      
  else:
    print('-1')
