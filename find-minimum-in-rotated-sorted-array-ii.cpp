// https://leetcode.com/discuss/19746/my-pretty-simple-code-to-solve-it
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1, mid;
        while(left < right) {
        	mid = (left + right) / 2;
        	if(nums[mid] < nums[right])
        		right = mid;
            else if(nums[mid] > nums[right])
                left = mid + 1;
        	else
                right--;

        }
        return nums[left];
    }
};

int main(int argc, const char* argv[])
{
    vector<int> nums {1, 3, 3};
    Solution s;
    cout << s.findMin(nums);
}
