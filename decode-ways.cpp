#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
    public:
        int numDecodings(string s) {
            int n = s.length();
            vector<int> dp(n + 1, -1);
            dp[n] = 1;
            return n == 0 ? 0 : dfs(0, s, dp);
        }

        int dfs(int i, string &s, vector<int> &dp) {
            if (dp[i] > -1) return dp[i];
            if (s[i] == '0') return dp[i] = 0;
            int sum = dfs(i + 1, s, dp);
            if (i < s.length() - 1 && (s[i] == '1' || (s[i] == '2' && s[i+1] <= '6'))) sum += dfs(i + 2, s, dp);
            /* cout << "i = " << i << " => " << sum << endl; */
            return dp[i] = sum;
        }
};

int main()
{
    Solution s;
    cout << s.numDecodings("226") << endl;
    cout << s.numDecodings("17") << endl;
}
