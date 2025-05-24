// https://www.geeksforgeeks.org/coin-change-dp-7/
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        if(amount == 0)
            return 1;
        if(coins.size() == 0)
            return 0;

        vector<vector<int> > table(amount + 1, vector<int>(coins.size()));
        for (int i = 0; i < coins.size(); i++)
            table[0][i] = 1;

        int m = coins.size();
        int n = amount, i, j, x, y;
        for (i = 1; i < n + 1; i++)
        {
            for (j = 0; j < m; j++)
            {
                x = (i-coins[j] >= 0) ? table[i - coins[j]][j] : 0;
                y = (j >= 1) ? table[i][j - 1] : 0;
                table[i][j] = x + y;
            }
        }
        return table[n][m - 1];
    }
};

int main()
{
    Solution s;
    /* vector<int> coins {1, 2, 5}; */
    /* cout << s.change(5, coins); */
    vector<int> coins {};
    cout << s.change(0, coins);
}
