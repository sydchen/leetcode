#include <bit>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> minDifference(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        const int MAXV = 100;
        // pre[i] 表示 nums[0..i-1] 中各值的出現次數
        vector<array<int, 101>> pre(n + 1);
        // 預設 array 會初始化為 0

        for (int i = 0; i < n; ++i) {
            pre[i + 1] = pre[i];           // 複製上一個前綴
            pre[i + 1][nums[i]] += 1;      // 當前值出現一次
        }

        vector<int> ans;
        ans.reserve(queries.size());

        for (auto &q : queries) {
            int l = q[0], r = q[1];
            int prev = -1;
            int minDiff = INT_MAX;

            for (int v = 1; v <= MAXV; ++v) {
                if (pre[r + 1][v] - pre[l][v] > 0) { // 最小差一定發生在「數值相鄰」的兩個數之間
                    if (prev != -1) minDiff = min(minDiff, v - prev);
                    prev = v;
                }
            }

            ans.push_back(minDiff == INT_MAX ? -1 : minDiff);
        }

        return ans;
    }
};

void print(vector<int> result) {
    cout << "Output: [";
    for (int i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i + 1 < result.size()) cout << ", ";
    }
    cout << "]\n";
}

int main(int argc, const char* argv[])
{
    Solution s;
    vector nums{1,3,4,8};
    vector<vector<int>> queries{{0,1},{1,2},{2,3},{0,3}};

    print(s.minDifference(nums, queries)); // [2, 1, 4, 1]
}

