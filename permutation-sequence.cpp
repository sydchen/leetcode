#include <iostream>
// reference: https://oj.leetcode.com/discuss/21027/sharing-my-straightforward-c-solution-with-explanation
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string getPermutation(int n, int k) {
        int pTable[10] = {1};
        for(int i = 1; i <= 9; i++){
            pTable[i] = i * pTable[i - 1];
        }

        vector<char> numSet(9);
        char c = '1';
        generate(numSet.begin(), numSet.end(), [&]{ return c++; });

        string result;
        while(n > 0){
            int temp = (k - 1) / pTable[n - 1];
            result += numSet[temp];
            numSet.erase(numSet.begin() + temp);
            k = k - temp * pTable[n - 1];
            n--;
        }
        return result;
    }
};

int main()
{
    Solution s;
    cout << s.getPermutation(8, 8590);
}
