class Solution(object):
    def numJewelsInStones(self, J, S):
        count = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if(J[i]==S[j]):
                    count = count+1
                else:
                    pass
        return(count)
