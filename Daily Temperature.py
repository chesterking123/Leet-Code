class Solution(object):
    def dailyTemperatures(self,T):
        stack = []
        ans = [0]*len(T)
        for i in range(len(T)):
            while(stack and T[stack[-1]]<T[i]):
                ans[stack.pop()] = i - stack[-1]
            stack.append(i)
        return(ans)
                
            
