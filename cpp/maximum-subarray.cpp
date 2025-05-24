/* https://leetcode.com/discuss/11288/simplest-and-fastest-o-n-c-solution */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans, sum;
        ans = sum = nums[0];
        for(int i = 1; i < nums.size(); i++){
            sum = max(sum + nums[i], nums[i]);
            ans = max(sum, ans);
        }
        return ans;
    }
};

int main(int argc, const char* argv[])
{
    /* vector<int> nums { -2, 1, -3, 4, -1, 2, 1, -5, 4}; */
    vector<int> nums { 1 };
    Solution s;
    cout << s.maxSubArray(nums);
}
