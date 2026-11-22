class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m = min(nums)
        l = max(nums)

        stack = []
        for i in range(m,l):
            if i not in nums:
                stack.append(i)
        return stack