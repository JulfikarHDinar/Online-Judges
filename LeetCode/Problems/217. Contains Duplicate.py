class Solution:
    def containsDuplicate(self, nums):
        numsUnique = set(nums)
        
        if len(numsUnique) != len(nums):
            return True
        
        return False