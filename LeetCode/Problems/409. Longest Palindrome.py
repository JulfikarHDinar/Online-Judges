class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1:
            return 1
        list1 = list(s)
        list1.sort()        #sorting alphabetically
        left = ''           #left string of palindrome 
        right = ''          #right string of palindrome 
        middle = ''         #middle char of palindrome(single char)
        prev = ''           #tracking previous char

        for i in range(len(list1)):
            #print(list1[i])
            if prev == '':
                prev = list1[i]
            elif prev == list1[i]:      
                left = list1[i] + left
                right = right + list1[i]
                prev = ''
            elif prev != list1[i] and middle == '':
                middle = middle + prev
                prev = list1[i]
            else:
                prev = list1[i]
        
        if middle == '' and prev != '':
            middle = middle + prev

        palStr = left+middle+right
        #print(palStr)
        #print(list1)
        return len(palStr)
