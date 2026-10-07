class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
       
        unique_types = len(set(candyType))   # count unique candies
        return min(unique_types, len(candyType) // 2)