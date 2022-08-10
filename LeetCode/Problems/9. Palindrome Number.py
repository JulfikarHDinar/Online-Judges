class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
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
