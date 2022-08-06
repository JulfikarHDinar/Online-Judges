import operator
import collections
string = input()
uniqueChar = set(string)

myDict = dict()

for i in uniqueChar:
  cnt =  string.count(i)
  myDict[i] = cnt

lettersorted = collections.OrderedDict(sorted(myDict.items()))
valuesorted = dict( sorted(lettersorted.items(), key=operator.itemgetter(1),reverse=True))

i=0
for keys, values in valuesorted.items():
    if i == 3:
      break
    print(keys+" "+str(values))
    i=i+1