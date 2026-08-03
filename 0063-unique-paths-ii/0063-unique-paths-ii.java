class Solution {
    public int func(int[][] a, int dp[][], int r, int c, int m, int n) {
        if(r >= m || c >= n) {
            return 0;
        }
        if(a[r][c] == 1) {
            return 0;
        }
        if(r == m-1 && c == n-1) {
            return 1;
        }
        if(dp[r][c] != -1) {
            return dp[r][c];
        }
        dp[r][c] =  func(a, dp, r, c+1, m, n) + func(a, dp, r+1, c, m, n);
        return dp[r][c];
    }
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int dp[][] = new int[m][n];
        for(int[] i : dp) {
            Arrays.fill(i, -1);
        }
        return func(obstacleGrid, dp, 0, 0, m, n);
    }
}