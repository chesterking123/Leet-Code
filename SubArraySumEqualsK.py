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
        

#Print Subarray
def subArraySum(arr, n, sum): 
 
    curr_sum = arr[0] 
    start = 0
    i = 1
    while i <= n: 
        while curr_sum > sum and start < i-1: 
            print(curr_sum)
            curr_sum = curr_sum - arr[start] 
            start += 1
              
        if curr_sum == sum: 
            print ("Sum found between indexes") 
            print (arr[start:i]) 
            return 

        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1
  
    print ("No subarray found") 
    return 0
  
# Driver program 
arr = [15, 2, 4, 8, 9, 5, 10, 23] 
n = len(arr) 
sum = 23
  
subArraySum(arr, n, sum)
