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
  
#
#
#
#
# This program can handel neg values
def subArraySum(arr, n, Sum):  

    Map = {}  

    curr_sum = 0 
    
    for i in range(0,n):  

        curr_sum = curr_sum + arr[i]  

        if curr_sum == Sum:  
           
            print("Sum found between indexes 0 to", i) 
            return  
        if (curr_sum - Sum) in Map:  
           
            print("Sum found between indexes", \ 
                   Map[curr_sum - Sum] + 1, "to", i)  
              
            return 
    
        Map[curr_sum] = i   
    print("No subarray with given sum exists")
