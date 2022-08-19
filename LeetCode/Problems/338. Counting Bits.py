class Solution:
    def countOne(self, nStr):
        cnt = 0
        for i in range(len(nStr)):
            if nStr[i] == '1':
                cnt += 1
        return cnt

    def countBits(self, n):
        list1 = []
        for i in range(n+1):
            binStr = format(i, 'b')
            tmp = self.countOne(binStr)
            list1.append(tmp)
            
        return list1
        