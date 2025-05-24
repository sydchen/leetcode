// https://leetcode.com/problems/house-robber-ii/discuss/59921/9-lines-0ms-O(1)-Space-C%2B%2B-solution
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        else if (n == 1) return nums[0];
        else return max(rob(nums, 0, n - 2), rob(nums, 1, n - 1));
    }

    int rob(vector<int>& nums, int l, int r) {
        int prev = 0, prev_prev = 0;
        for (int i = l; i <= r; i++) {
            int tmp = max(nums[i] + prev_prev, prev);
            prev_prev = prev;
            prev = tmp;
        }
        return prev;
    }
};

int main()
{
    Solution s;
    /* vector<int> nums { 1,2,3,1 }; */
    /* cout << s.rob(nums); // 4 */

    vector<int> nums { 2, 3, 2 };
    cout << s.rob(nums); // 3
}
