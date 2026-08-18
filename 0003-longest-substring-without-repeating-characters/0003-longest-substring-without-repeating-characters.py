class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = set()
        res = 0
        left = 0

        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left = left + 1

            visited.add(s[right])
            res = max(res, right - left + 1)

        return res