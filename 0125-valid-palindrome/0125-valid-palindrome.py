class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = ""
        for i in s.lower():
            if i.isalnum():
                ans+=i
        if ans==ans[::-1]:
            return True
        else:
            return False