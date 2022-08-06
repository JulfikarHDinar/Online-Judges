cnt1 = int(input())
listT = list(map(int,input().split()))
listA = []
for i in range(cnt1):
  listA.append(listT[i])
setA = set(listA) 
#print(listA)

cnt2 = int(input())
listB = []
for i in range(cnt2):
  listB.append(input())
#print(listB)

for i in listB:
  temp = i.split()
  #print(temp[0]+"--"+temp[1])
  if temp[0] == 'remove':
    try:
      setA.remove(int(temp[1]))
    except:
      pass

  elif temp[0] == 'discard':
    setA.discard(int(temp[1]))

  elif temp[0] == 'pop':
    setA.pop()

print(sum(setA))
