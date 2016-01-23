/* https://leetcode.com/discuss/65637/simple-c-solution-using-2-k-ary */
/* http://stackoverflow.com/questions/5231096/time-complexity-of-power */
/* https://en.wikipedia.org/wiki/Exponentiation_by_squaring */

#include <iostream>

using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        double result = 1;
        if(n < 0) {
            n *= -1;
            x = 1/x;
        }
        while(n > 0) {
            if(n & 1) {
                result *= x;
                n--;
            }
            x *= x;
            n /= 2;
        }
        return result;
    }
};

int main(int argc, const char* argv[])
{
    Solution sol;
    cout << sol.myPow(34.21, -3);
}
