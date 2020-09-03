class Solution(object):
    def searchRange(self, nums, target):
        ans=[]
        if(target not in nums):
            return([-1,-1])
        for i in range(len(nums)):
            if(nums[i]==target):
                ans.append(i)
        return([min(ans),max(ans)])
                
