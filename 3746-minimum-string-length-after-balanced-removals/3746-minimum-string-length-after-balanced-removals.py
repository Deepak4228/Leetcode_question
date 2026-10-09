class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s.count("a")
        b = s.count("b")
        return abs(a-b)