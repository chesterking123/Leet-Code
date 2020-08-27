
//47 test cases 

areas = []
        edge = len(height)
        if(edge==2):
            return(min(height[0],height[1]))
        if(edge>100):
            for i in range(edge//2):
                for j in range(edge-1,edge//2,-1):
                    areas.append((min(height[i],height[j]))*(j-i))
        else:
            for i in range(edge):
                for j in range(edge-1,-1,-1):
                    areas.append((min(height[i],height[j]))*(j-i))
        
        return(max(areas))
        
// all test cases
def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n=len(height)
        if n == 2:
            return min(height[0],height[1])
        else:
            l=0
            r=n-1
            clh=0
            crh=0
            maxa=0 
            while l<r :                
              
                if height[l]<height[r]:
                    maxa=max(height[l]*(r-l),maxa)
                    clh=height[l]
                    while height[l]<=clh:
                        l+=1
                        if l>= r:
                            return maxa

                else:
                    maxa=max(height[r]*(r-l),maxa)
                    crh=height[r]
                    while height[r]<=crh :
                        r-=1 
                        if l>= r:
                            return maxa
                        

            return maxa
