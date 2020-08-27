class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):        
        merge = nums1 + nums2
        merge = sorted(merge)
        a = 0
        b = 0
        ans = 0
        if(len(merge)%2 != 0):
            a = (len(merge)-1)/2
            ans = merge[int(a)]
            return(float(ans))
        else:
            j = (len(merge)/2)
            a = j-1
            b = j+1
            p = (sum(merge[int(a):int(b)]))
            return(float(p)/2)
        
        
