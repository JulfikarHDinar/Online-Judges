import collections
class Solution:
    def canConstruct(self, ransomNote, magazine):
        list1 = list(ransomNote)
        list2 = list(magazine)

        letterCollection1 = collections.Counter(list1)
        letterCollection2 = collections.Counter(list2)

        #print(letterCollection1)
        #print(letterCollection2)
        for i in letterCollection1.items():
            #print(i[0],end=' ') #key
            #print(i[1]) #value
            if letterCollection2[i[0]] >= i[1]:
                continue
            else:
                return False

        return True
