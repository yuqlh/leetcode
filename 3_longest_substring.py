class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = re = 0
        d = dict()
        for j in range(len(s)):
            if d.get(s[j]):
                while i<j:
                    d[s[i]] = 0
                    if s[i]==s[j]:
                        i += 1
                        break
                    i += 1
            re = max(re, j-i+1)
            d[s[j]] = 1
        return re
