class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        reverse = ""
        for i in words:
            reverse+= i[::-1]+" "
        return reverse.strip()