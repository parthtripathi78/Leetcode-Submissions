class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {

        int n = matrix.size();

        for (int r = 1; r < n; r++) {

            for (int c = 0; c < n; c++) {

                int mid = matrix[r - 1][c];

                int left = (c > 0) ? matrix[r - 1][c - 1] : INT_MAX;

                int right = (c < n - 1) ? matrix[r - 1][c + 1] : INT_MAX;

                matrix[r][c] = matrix[r][c] + min(mid, min(left, right));
            }
        }

        int ans = INT_MAX;

        for (int c = 0; c < n; c++) {
            ans = min(ans, matrix[n - 1][c]);
        }

        return ans;
    }
};