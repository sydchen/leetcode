#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (nums[i] == 0) {
                for(int j = i+1; j< nums.size(); j++)
                    swap(nums[j-1], nums[j]);
            }
        }        
    }
};

int main()
{
    Solution s;
    vector<int> nums {0,1,0,3,12};
    s.moveZeroes(nums);

    for(auto &n:nums)
        cout << n << " ";
    cout << endl;
}
