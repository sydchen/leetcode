// https://leetcode.com/discuss/11701/concise-o-log-n-binary-search-solution
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int rot = findMin(nums);
        int n = nums.size();
        int left = 0, right = n - 1, mid, realmid;
        while(left <= right) {
          mid = (left + right) / 2;
          realmid = (mid + rot) % n;
          if(nums[realmid] == target)
            return realmid;
          else if(nums[realmid] < target)
            left = mid + 1;
          else
            right = mid - 1;

        }
        return -1;
    }
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1, mid;
        while(left < right) {
          mid = (left + right) / 2;
          if(nums[mid] < nums[right])
            right = mid;
          else
            left = mid + 1;
        }
        return left;
    }
};

int main(int argc, const char* argv[])
{
    vector<int> nums {4, 5, 6, 7, 0, 1, 2};
    Solution s;
    cout << s.search(nums, 1);
}
