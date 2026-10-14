class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        rich = 0
        for i in accounts:
            if rich < sum(i):
                rich = sum(i)
        return rich