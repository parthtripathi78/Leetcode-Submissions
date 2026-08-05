class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = {}

        def lps(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == s[j]:
                dp[(i, j)] = 2 + lps(i + 1, j - 1)
            else:
                dp[(i, j)] = max(lps(i + 1, j), lps(i, j - 1))

            return dp[(i, j)]

        return len(s) - lps(0, len(s) - 1)
        