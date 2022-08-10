class Solution:
    def isAnagram(self, s: str, t: str):
        list1 = list(s)
        list2 = list(t)
        if len(list1) != len(list2):
            return False

        for i in list1:
            try:
                list2.remove(i)
            except ValueError:
                pass
        
        if len(list2) != 0:
            return False

        list1 = list(s)
        list2 = list(t)
        for i in list2:
            try:
                list1.remove(i)
            except ValueError:
                pass
        if len(list1) != 0:
            return False
        
        return True