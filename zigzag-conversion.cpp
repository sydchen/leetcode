/* https://leetcode.com/discuss/63292/my-easy-read-python-solution */
/* https://leetcode.com/discuss/51476/lines-space-accepted-solution-with-detailed-explantation */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows <= 1) return s;

        string result = "";
        vector<string> rows;
        rows.resize(numRows);
        int cycle = 2 * numRows - 2;

        for(int i = 0; i < s.length(); i++) {
            if(i % cycle < numRows)
                rows[i % cycle] += s[i];
            else
                rows[cycle - i % cycle] += s[i];
        }
        for(string &row : rows)
            result += row;
        return result;
    }
};

int main(int argc, const char* argv[])
{
    Solution s;
    cout << s.convert("PAYPALISHIRING", 3);
}
