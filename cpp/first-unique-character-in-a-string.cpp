#include <iostream>
#include <map>

using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        map<int, int> map;
        int length = s.length();
        for (int i = 0 ; i < length; i++)  map[s[i]]++;

        for (int i = 0 ; i < length; i++) {
            if (map[s[i]] == 1)  return i;
        }

        return -1;
    }
};

int main()
{
    Solution s;
    cout << s.firstUniqChar("loveleetcode");
}

