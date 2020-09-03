class Solution(object):
    def findRepeatedDnaSequences(self, s):
        dix = {}
        i=0
        answer = []
        if(len(s)<10):
            return([])
        p = True
        i=0
        while(p):
            j=i+10
            if(j==len(s)):
                p = False
            if s[i:j] in dix:
                answer.append(s[i:j])
            dix[s[i:j]] = dix.get(s[i:j],0)+1
            i=i+1
        return(set(answer))        
