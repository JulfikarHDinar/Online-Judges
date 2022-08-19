import sys
class Solution:
    def maxProfit(self, prices):
        min = sys.maxsize
        maxProf = -min
        
        for i in prices:
            if i < min:
                 min = i
            #print(min)
            prof = i - min
            #print(prof)
            if prof > maxProf:
                maxProf = prof
                
        return maxProf