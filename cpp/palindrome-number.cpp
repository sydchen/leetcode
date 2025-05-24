/* https://leetcode.com/discuss/33500/an-easy-lines-code-only-reversing-till-half-and-then-compare
x = 12321
x =   12321, 1232, 123, 12   ,1
sum = 0    , 1,    12,  123, 1232  */

#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0|| (x != 0 && x % 10 == 0)) return false;
        int sum = 0;
        while(x > sum)
        {
            sum = sum * 10 + x % 10;
            x = x / 10;
        }
        return (x == sum) || (x == sum / 10);
    }
};

int main(int argc, const char* argv[])
{
    Solution s;
    cout << s.isPalindrome(12321);
}
