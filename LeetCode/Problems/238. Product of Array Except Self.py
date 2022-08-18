class Solution:
    def productExceptSelf(self, nums):
        #print(nums.count(0))
        list1 = []

        if nums.count(0) > 1:           #contains more than 1 zeros
            for i in range(len(nums)):
                list1.append(0)
                
        elif nums.count(0) == 1:        #contains 1 zero
            zeroInd = nums.index(0)
            #print(zeroInd)
            for i in range(len(nums)):
                if i != zeroInd:
                    list1.append(0)
                else:
                    numsT = nums.copy()
                    del numsT[zeroInd]
                    res = 1
                    for i in numsT:
                        res = res * i
                    list1.append(res)
        else:
            res = 1
            for i in nums:          
                res = res * i       #total product

            for i in nums:
                list1.append(int(res/i))    #productExceptSelf

        return list1