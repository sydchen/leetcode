#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef std::pair<int,int> Pair;

class Solution {
public:
    long long maxTaxiEarnings(int n, vector<vector<int>>& rides) {
        vector<vector<Pair>> ridesStartAt(n + 1);

        for (auto &r : rides) {
            int start = r[0], end = r[1], tip = r[2];
            ridesStartAt[start].push_back({end, end - start + tip});
        }

        vector<long long> dp(n + 1);
        for (int i = n - 1; i >= 0; i--) {
            for (auto &[e, d] : ridesStartAt[i]) { //  C++17
                dp[i] = max(dp[i], d + dp[e]);
            }
            dp[i] = max(dp[i], dp[i + 1]);
        }

        return dp[1];
    }
};

int main()
{
    Solution s;

    vector<vector<int>> rides1 { {2, 5, 4}, {1, 5, 1} };
    cout << s.maxTaxiEarnings(5, rides1); // 7
    vector<vector<int>> rides2 { {1, 6, 1}, {3, 10, 2}, {10, 12, 3}, {11, 12, 2}, {12, 15, 2}, {13, 18, 1} };
    cout << s.maxTaxiEarnings(20, rides2); // 20
}
