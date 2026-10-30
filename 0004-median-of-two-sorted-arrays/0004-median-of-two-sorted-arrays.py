class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
    
        s = sorted(nums1 + nums2)
        n = len(s)

        if n % 2 == 0:
            return (s[n // 2 - 1] + s[n // 2]) / 2.0

        return (s[n // 2])
        