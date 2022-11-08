class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        conlist = nums1 + nums2
        conlist = sorted(conlist, reverse=False) 
        print(conlist)
        listlen = len(conlist) 
        if listlen % 2 == 1:    #odd
            #print(conlist[int((listlen+1)/2) - 1]) 
            return float(conlist[int((listlen+1)/2)-1])
        else:					#even
            term1 = int((listlen)/2) - 1
            term2 = int((listlen)/2)
            #print((conlist[term1]+conlist[term2])/2 )
            return float((conlist[term1]+conlist[term2])/2) 
