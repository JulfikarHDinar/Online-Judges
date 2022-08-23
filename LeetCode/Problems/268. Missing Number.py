class Solution:
    def missingNumber(self, nums):
        minVal = 0                              #first term
        maxVal = len(nums)                      #last term
        nTerm = maxVal - minVal + 1             #no of term
        arithSum = nTerm*((minVal+maxVal)/2)    #arithmatic sum
        listSum = sum(nums)
        missVal = int(arithSum - listSum)

        return missVal
