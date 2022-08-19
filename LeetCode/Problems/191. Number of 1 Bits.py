class Solution:
    def hammingWeight(self, n):
        binN =  bin(n)
        cnt = binN.count("1")
        return cnt
