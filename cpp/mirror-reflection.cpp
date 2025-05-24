#include <iostream>

using namespace std;

class Solution {
public:
    int mirrorReflection(int p, int q) {
        while (p % 2 == 0 && q % 2 == 0)  p >>= 1, q >>= 1;
        if (p % 2 == 0)
            return 2;
        else if (q % 2 == 0)
            return 0;
        else
            return 1;
    }
};

int main(int argc, const char* argv[])
{
    Solution s;
    cout << s.mirrorReflection(2, 1);
    cout << s.mirrorReflection(5, 2);
}

