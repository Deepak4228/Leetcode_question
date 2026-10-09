class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        total = 0
        for i in range(0,l-1):
            f = s[i]
            sec = s[i+1]
            total += abs(ord(f)-ord(sec))
        return total
        