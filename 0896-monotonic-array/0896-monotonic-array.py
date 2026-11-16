class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = sorted(nums)
        if n==nums or n[::-1]==nums:
            return True
        else:
            return False
                