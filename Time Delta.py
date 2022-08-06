import datetime

cnt = int(input())
resultList=[]

for test in range(cnt):
    string1 = input()
    string2 = input()

    t1 = datetime.datetime.strptime(string1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.datetime.strptime(string2, "%a %d %b %Y %H:%M:%S %z")

    result = abs((t1-t2).total_seconds())
    resultList.append(result)

for i in resultList:
  print(int(i))