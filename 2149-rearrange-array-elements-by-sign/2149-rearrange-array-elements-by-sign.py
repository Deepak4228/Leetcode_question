class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = []
        n = []
        for i in nums:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        a = []
        
        for i in range(len(p)):
            a.append(p[i])
            a.append(n[i])
        return a