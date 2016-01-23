#include <iostream>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int ret = 0;
        while(x) {
            if(ret > INT_MAX/10 || ret <INT_MIN/10)
                return 0;
            ret = ret * 10 + x % 10;
            x /= 10;
        }
        return ret;
    }
};

int main(int argc, const char* argv[])
{
    Solution s;
    cout << s.reverse(1534236469);
}
