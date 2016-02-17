/* https://leetcode.com/discuss/30020/java-o-n-solution-space-o-1 */
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int prevNo = 0, prevYes = 0, tmp;
        for(auto n : nums) {
            int tmp = prevNo;
            prevNo = max(prevNo, prevYes);
            prevYes = n + tmp;
        }
        return max(prevYes, prevNo);
    }
};

int main(int argc, const char* argv[])
{
    Solution s;
}
