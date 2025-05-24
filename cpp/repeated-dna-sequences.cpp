// https://leetcode.com/discuss/74330/20-ms-solution-c-with-explanation
// https://leetcode.com/discuss/44689/10-lines-c-code-8-ms-passed
#include <vector>
#include <iostream>
#include <iterator>

using namespace std;
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> ans;
        if(s.length() < 10)
            return ans;

        char hashMap[1048576] = {0};
        for(int i=0;i<=s.length()-10;i++) {
            int hashNum = 0;
            for(int j=i;j<i+10;j++)
                hashNum = hashNum << 2 | (s[j] - 'A' + 1) % 5;
            if(hashMap[hashNum] == 1)
                ans.push_back(s.substr(i, 10));
            hashMap[hashNum]++;
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<string> result = sol.findRepeatedDnaSequences("AAAAAAAAAAAA");
    for(int i=0;i<result.size();i++) {
        cout << result[i] << endl;
    }
}
