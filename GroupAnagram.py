class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dix = {}
        for s in strs:
            temp = ''.join(sorted(s))
            if(temp in dix):
                dix.get(temp).append(s)
            else:
                dix[temp] = [s]
        return(dix.values())
