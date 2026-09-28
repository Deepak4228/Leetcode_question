class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        parenthesis = 0
        for i in s:
            if i =="(":
                parenthesis+=1
                if parenthesis>max:
                    max  = parenthesis
            elif i==")":
                parenthesis-=1
        return max
        