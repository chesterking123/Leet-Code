class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        di = dict()
        for i in range(len(nums)):
            check = target - nums[i]
            if nums[i] in di:
                return([di[nums[i]],i])
            else:
                di[check]=i
        return []