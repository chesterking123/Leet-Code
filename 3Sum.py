class Solution(object):
    def threeSum(self, nums):
        solution = {}
        nums = sorted(nums)
        for i in range(len(nums)):
            left_point = i+1
            right_point = len(nums)-1
            s=0
            
            while(left_point<right_point):
                s = nums[i]+nums[left_point]+nums[right_point]
                
                if(s>0):
                    right_point=right_point-1
                elif(s<0):
                    left_point = left_point+1
                
                elif(s==0):
                    solution[nums[i],nums[left_point],nums[right_point]] = 1
                    right_point=right_point-1
                    left_point = left_point+1
        return(solution.keys())
