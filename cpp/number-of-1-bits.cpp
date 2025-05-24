/* https://en.wikipedia.org/wiki/Hamming_weight */
#include <iostream>

using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n)
    {
        int weight = 0;
        for(; n ; n>>=1) {
            if(n & 1)
                weight += 1;
        }
        return weight;
    }
};

int main(int argc, const char* argv[])
{
    Solution s;
    cout << s.hammingWeight(11) << endl;
}
