#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, bool> dup;
        for(int i = 0; i < nums.size(); i++) {
            if (dup.find(nums[i]) != dup.end()) return true;
            dup[nums[i]] = true;
        }
        return false;
    }
};

int main()
{
    Solution s;
    vector nums = {1,1,1,3,3,4,3,2,4,2};
    cout << s.containsDuplicate(nums);
}
