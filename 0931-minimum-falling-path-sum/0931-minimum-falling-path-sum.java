class Solution {
    int[][] memo;
    int n;
    public int minFallingPathSum(int[][] matrix) {
        n = matrix.length;
        memo = new int[n][n];
        for (int[] row : memo) {
            java.util.Arrays.fill(row, Integer.MAX_VALUE);
        }
        int ans = Integer.MAX_VALUE;
        for (int c = 0; c < n; c++) {
            ans = Math.min(ans, dfs(matrix, 0, c));
        }
        return ans;
    }
    int dfs(int[][] matrix, int r, int c) {
        if (c < 0 || c == n) {
            return Integer.MAX_VALUE;
        }
        if (r == n) {
            return 0;
        }
        if (memo[r][c] != Integer.MAX_VALUE) {
            return memo[r][c];
        }
        int left = dfs(matrix, r + 1, c - 1);
        int down = dfs(matrix, r + 1, c);
        int right = dfs(matrix, r + 1, c + 1);
        int ans = matrix[r][c] + Math.min(left, Math.min(down, right));
        memo[r][c] = ans;
        return ans;
    }
}