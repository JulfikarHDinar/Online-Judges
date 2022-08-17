class Solution:
    def plusOne(self, digits):
        str1 = ''
        for i in digits:
            str1 += str(i)
        num = int(str1)
        num += 1
        return list(str(num))
