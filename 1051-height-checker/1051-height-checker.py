class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count=0
        res=sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=res[i]:
                count+=1
        return count