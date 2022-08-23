class Solution:
    def isAnagram(self, s: str, t: str):
        list1 = list(s)
        list2 = list(t)
        list1.sort()
        list2.sort()
        if len(list1) != len(list2):
            return False

        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False        
        
        return True