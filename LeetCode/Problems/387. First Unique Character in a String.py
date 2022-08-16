class Solution:
    def firstUniqChar(self, s):
        ind = -1
        if len(s) == 1:
            ind = 0
            return ind
            
        for i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    continue
                elif s[i] == s[j]:
                    ind = -1
                    break
                elif s[i] != s[j]:
                    ind = i
                if j == len(s)-1:
                    return ind
        return ind