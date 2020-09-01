from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        counted = Counter(s)
        counted = sorted(counted.items(), key = lambda x: x[1],reverse = True)
        answer = []
        for i in range(len(counted)):
            answer.append(counted[i][0]*counted[i][1])
        return(''.join(answer))
        
        
        
