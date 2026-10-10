class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        s = s.split()
        l = len(s)
        ans = ""
        for i in range(l):
            if i!=k:
                ans+= s[i]+" "
            else:
                break
        return ans.strip()
        