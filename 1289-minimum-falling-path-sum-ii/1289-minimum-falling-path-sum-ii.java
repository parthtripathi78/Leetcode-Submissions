class Solution {
    public int minFallingPathSum(int[][] grid) {
        int n = grid.length;
        int[][] dp = new int[n][n];
        for (int col = 0; col < n; col++) {
            dp[0][col] = grid[0][col];
        }
        for (int row = 1; row < n; row++) {
            for (int col = 0; col < n; col++) {
                int ans = Integer.MAX_VALUE;
                for (int prevCol = 0; prevCol < n; prevCol++) {
                    if (prevCol != col) {
                        ans = Math.min(ans, dp[row - 1][prevCol]);
                    }
                }
                dp[row][col] = grid[row][col] + ans;
            }
        }
        int result = Integer.MAX_VALUE;
        for (int col = 0; col < n; col++) {
            result = Math.min(result, dp[n - 1][col]);
        }
        return result;
    }
}