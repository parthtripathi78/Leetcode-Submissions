class Solution(object):
    def minFallingPathSum(self, grid):
        n = len(grid)

        dp = [[0] * n for _ in range(n)]

        for col in range(n):
            dp[0][col] = grid[0][col]

        for row in range(1, n):
            for col in range(n):
                ans = float('inf')

                for prevcol in range(n):
                    if prevcol != col:
                        ans = min(ans, dp[row - 1][prevcol])

                dp[row][col] = grid[row][col] + ans

        return min(dp[n - 1])