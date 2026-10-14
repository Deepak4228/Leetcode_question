class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        count=0
        list = []
        for i in n:
            d = n.count(i)
            if int(i) not in list:
               list.append(int(i))
               count+= int(i)*d
        return count