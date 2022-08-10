import re
class Solution:
    def getClean(self, s:str):
        s = re.sub('[^a-zA-Z0-9]', ' ', s)
        s = s.lower()
        s = re.sub(' +', '', s)
        return s

    def isPalindrome(self, s: str):
        s = self.getClean(s)
        if len(s) == 0 or  len(s) == 1:
            return True
        f=0
        l=len(s)-1
        check = 0
        for i in range( int(len(s)/2) ):
            if s[f] == s[l]:
                check = 1
                f+=1
                l-=1
                continue
            else:
                check = 0
                break
        if check == 1:
            return True
        else:
            return False