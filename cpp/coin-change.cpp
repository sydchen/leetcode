#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int max = amount + 1;
        vector<int> dp(max, max);
        dp[0] = 0;
        for (int i = 1 ; i <= amount; i++) {
            for (int j = 0; j < coins.size(); j++) {
                int coin = coins[j];
                if(coin <= i) dp[i] = min(dp[i], dp[i-coin] + 1);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
};

int main()
{
    Solution s;
    vector<int> coins {1, 2, 5};
    cout << s.coinChange(coins, 11);
}
