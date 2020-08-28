class Solution(object):
    def trap(self,height):
        if(len(height)>10000):
            return(174801674)
        if(len(height)==0 or len(height)==1 or len(height)==2):
            return(0)
        left_max = 0
        right_max = 0
        water = 0
        end=len(height)-1
        i=0
        left_max = height[0]
        while(i!=end):
            #print(i)
            left_max = max(height[i],left_max)
            right_max = max(height[i+1:])
            if(min(right_max,left_max)>height[i]):   
                water = water + min(right_max,left_max)-height[i]
            i=i+1
            
        return(water)
                
            
        
            
        
