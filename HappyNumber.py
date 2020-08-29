class Solution(object):
    def isHappy(self, n):
        prew = n
        lis = []
        while(n!=1):
            n = int(sum([int(i)**2 for i in str(n)]))
            print(n)
            if(n in lis):
                return(False)
                
            if(str(n) == str(prew)):
                return(False)
            lis.append(n)

        return(True)
                
        
        
        #sum([int(i) ** 2 for i in str(n)])
