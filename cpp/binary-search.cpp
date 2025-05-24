#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size();

        int i = 0, j = nums.size() - 1;
        while(i <= j) {
            int mid_idx = (i + j) / 2;
            int mid = nums[mid_idx];

            if (mid == target) return mid_idx;

            if (target < mid) {
                j = mid_idx - 1;
            }
            else if (target > mid) {
                i = mid_idx + 1;
            }
        }
        return -1;
    }
};

int main(int argc, const char* argv[])
{
    Solution s;
    /* vector<int> nums = { -1,0,3,5,9,12  }; */
    /* cout << s.search(nums, 9); // 4 */

    vector<int> nums = { 5 };
    cout << s.search(nums, 5); // 0
}
