class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vfreq = 0
        cfreq = 0
        for i in s:
            if i in ("aeiou") and s.count(i)>vfreq:
                vfreq+=1
        for i in s:
            if i not in ("aeiou") and s.count(i)>cfreq:
                cfreq+=1
        total = vfreq+cfreq
        return total 
