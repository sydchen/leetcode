/* https://leetcode.com/discuss/56323/very-simple-clean-java-solution */
/* https://leetcode.com/discuss/40559/accepted-4ms-c-solution */

#include <iostream>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int len = s.length();
        if(len < 2) return s;

        for(int i = 0; i < s.length(); i++) {
            findPaLindrome(s, i, i);
            findPaLindrome(s, i, i + 1);
        }

        return s.substr(lo, maxLen);
    }

    void findPaLindrome(string s, int left, int right)
    {
        while (left >= 0 && right < s.length() && s.at(left) == s.at(right)) {
            left--;
            right++;
        }
        if (maxLen < right - left - 1) {
            lo = left + 1;
            maxLen = right - left - 1;
        }
    }

private:
    int maxLen, lo;
};

int main(int argc, const char* argv[])
{
    Solution s;
    cout << s.longestPalindrome("xyzabbadef"); // abba
}
