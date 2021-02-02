class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = {}
        limit = numRows 
        
        if(len(s)<3):
            return s
        if(limit<2):
            return s
        
        for i in range(0,limit):
            ans[i]=[]
        j=0
        for letter in s:
            if(j==0):
                flag = '+'
            elif(j==limit-1):
                flag = '-'
                
            ans[j].append(letter)
            
            if(flag == '+'):
                j=j+1
            else:
                j=j-1
                
        ans = ans.values()   
        all_array = []
        
        for array in ans:
            all_array = all_array + array
            
        return(''.join(all_array))
            
        
        
        
