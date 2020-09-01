class Solution(object):
    def subarraySum(self, nums,k):
        sumdict = {0:1}
        n = len(nums)
        count = 0
        s = 0

        for num in nums:
            s += num
            if s-k in sumdict:
                count += sumdict[s-k]
            sumdict[s] = sumdict.get(s,0)+1
            print(sumdict)
        return count
        
        
