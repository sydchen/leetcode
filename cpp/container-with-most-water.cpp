/* https://leetcode.com/discuss/1074/anyone-who-has-a-o-n-algorithm */
/* simplify version of Trapping Rain Water */
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height)
    {
        int l = 0, r = height.size() - 1, maxArea = 0;
        while (l < r) {
            maxArea = max(maxArea, (r - l) * min(height[l], height[r]));
            if (height[l] < height[r])
                l++;
            else
                r--;
        }
        return maxArea;
    }
};

int main(int argc, const char* argv[])
{
    Solution s;
    vector<int> height = {1, 2, 1};
    cout << s.maxArea(height);
}
