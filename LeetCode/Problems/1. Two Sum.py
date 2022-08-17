class Solution:
    def twoSum(self, nums, target):
        list1=[]
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums)-1,-1,-1):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    list1.append(j)
                    list1.append(i)
                    return list1
