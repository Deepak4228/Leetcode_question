class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        s1 = num1[::-1]
        s2 = num2[::-1]

        res = [0] * (len(s1) + len(s2))

        for i in range(len(s1)):
            carry = 0
            start = i

            for j in range(len(s2)):
                n1 = int(s1[i])
                n2 = int(s2[j])

                total = n1 * n2 + res[start] + carry

                res[start] = total % 10
                carry = total // 10

                start += 1

            if carry != 0:
                res[start] = carry

        i = len(res) - 1

        while i >= 0 and res[i] == 0:
            i -= 1

        if i < 0:
            return "0"

        ans = ""

        while i >= 0:
            ans += str(res[i])
            i -= 1

        return ans