class Solution:
    def maxLengthBetweenEqualCharacters(self, s):
        str1 = ''
        maxSize = 0
        
        if len(list(s)) == len(set(s)):
            return -1
        
        for i in range(len(s)):
            for j in range(len(s)-1,-1,-1):
                if s[i] == s[j]:
                    maxSize = max(maxSize, len(s[i+1:j]))

        return maxSize
