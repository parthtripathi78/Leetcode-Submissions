class Solution {
public:
    bool isPalindrome(string &s, int i, int j) {
        while(i < j) {
            if(s[i] != s[j])
                return false;

            i++;
            j--;
        }
        return true;
    }

    int rec(int idx, string &s, vector<int> &dp) {
        int n = s.size();

        if(idx == n)
            return 0;

        if(dp[idx] != -1)
            return dp[idx];

        int ans = n;

        for(int i = idx; i < n; i++) {
            if(isPalindrome(s, idx, i)) {
                int pieces = 1 + rec(i + 1, s, dp);
                ans = min(ans, pieces);
            }
        }

        return dp[idx] = ans;
    }

    int minCut(string s) {
        int n = s.size();
        vector<int> dp(n, -1);

        return rec(0, s, dp) - 1;
    }
};