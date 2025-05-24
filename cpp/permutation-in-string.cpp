// https://leetcode.com/problems/permutation-in-string/discuss/102588/Java-Solution-Sliding-Window
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int count[26] = {0};
        int len_s1 = s1.size(), len_s2 = s2.size();

        if (len_s1 > len_s2) return false;

        for(int i = 0 ; i < len_s1; i++) {
            count[s1[i] - 'a']++;
            count[s2[i] - 'a']--;
        }

        if (check(count)) return true;

        for(int i = len_s1; i < len_s2; i++) {
            count[s2[i] - 'a']--;
            count[s2[i - len_s1] - 'a']++;

            if (check(count)) return true;
        }

        return false;
    }

    bool check(int count[])
    {
        for(int i = 0 ; i < 26; i++) {
            if(count[i] != 0) return false;
        }
        return true;
    }
};

int main()
{
    Solution s;
    cout << s.checkInclusion("ab", "eidbaooo");
    cout << s.checkInclusion("ab", "eidboaoo");
}
