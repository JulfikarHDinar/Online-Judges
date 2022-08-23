class Solution:
    def validPalindrome(self, s):
        if self.isPalindrome(s) == 1:
            return True
        else:
            t, f, l = self.isPalindrome(s)
            
            index = f
            temp = s
            temp = temp[:index] + temp[index + 1:]
            if self.isPalindrome(temp) == 1:
                return True

            index = l
            temp = s
            temp = temp[:index] + temp[index + 1:]
            if self.isPalindrome(temp) == 1:
                return True

            return False


    def isPalindrome(self, s):
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
            return 1
        else:
            return 0, f, l
