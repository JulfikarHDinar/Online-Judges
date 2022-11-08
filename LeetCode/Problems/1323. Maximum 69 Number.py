class Solution:
    def maximum69Number (self, num):
        str1 = str(num)
        str2 = ""
        check = 1
        for i in str1:
            if check == 1 and i == '6':
                str2 = str2 + '9'
                check = 0
            else:
                str2 = str2 + i
        return int(str2)
