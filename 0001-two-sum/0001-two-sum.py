class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = nums
        t = target
        ind= []
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if (n[i]+n[j]==t):
                    ind.append(i)
                    ind.append(j)
                    break
        return ind