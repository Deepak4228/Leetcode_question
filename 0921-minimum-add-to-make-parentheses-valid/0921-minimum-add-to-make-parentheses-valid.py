class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        for i in s:
            if l!=[] and l[-1]=="(" and i==")":
                l.pop()
            else:
                l.append(i)
        return len(l)        