/* https://leetcode.com/discuss/27387/summary-of-c-solutions */
#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        auto iter = nums.begin();
        for(; k %= n; n -= k, iter += k) {
            for(int i = 0; i < k; i++)
                swap(iter[i], iter[n - k + i]);
        }
    }
};

int main(int argc, const char* argv[])
{
    Solution s;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    s.rotate(nums, 3);
    copy(nums.begin(), nums.end(), ostream_iterator<int>(std::cout, " "));
}
