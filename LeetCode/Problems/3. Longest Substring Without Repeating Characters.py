class Solution:
    def lengthOfLongestSubstring(self, s):
        str1 = ''
        fStr1 = ''
        maxlen = 0

        for i in s:
            if i not in str1:           #unique characters
                str1 = str1 + i

            elif i in str1:             #a duplicate character found
                strLen = len(str1)
                if strLen > maxlen:     
                    maxlen = len(str1)
                    fStr1 = str1
                ind = str1.index(i)     #index of the first position of duplicate character
                str1 = str1[ind+1:]+i   #slicing after the first duplicate character and adding last duplicate character to make it unique

        if len(str1) > len(fStr1):
            fStr1 = str1
    
        return len(fStr1)
