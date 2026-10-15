class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        list = []
        num1 = str(num)
        for i in num1:
            if num% int(i)==0 and int(i) not in list:
                count+=1
                list.append(i)
        return count