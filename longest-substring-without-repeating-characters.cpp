#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> map(255, -1);
        int pos = -1, ans = 0;

        for(int i = 0; i < s.size(); i++ ) {
            int ch = s.at(i);
            pos = max(pos, map[ch]);
            ans = max(ans, i - pos);
            map[ch] = i;
        }

        return ans;
    }
};

int main()
{
    Solution s;
    /* cout << s.lengthOfLongestSubstring("abcabcbb"); */
    /* cout << s.lengthOfLongestSubstring("bbbbb"); */
    cout << s.lengthOfLongestSubstring(" ");
}
