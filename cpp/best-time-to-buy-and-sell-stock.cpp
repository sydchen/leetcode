#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int minPrice = INT_MAX, bestProfit = 0, profit;
        for(auto &price:prices) {
            if(price < minPrice)
                minPrice = price;
            profit = price - minPrice;
            if(profit > bestProfit)
                bestProfit = profit;
        }
        return bestProfit;
    }
};

int main()
{
    vector<int> prices {1};
    Solution s;
    cout << s.maxProfit(prices);
}
