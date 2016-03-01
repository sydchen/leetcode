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
        	else
        		left = mid + 1;
        }
        return nums[left];
    }
};

int main(int argc, const char* argv[])
{
    vector<int> nums {4, 5, 6, 7, 0, 1, 2};
    Solution s;
    cout << s.findMin(nums);
}
