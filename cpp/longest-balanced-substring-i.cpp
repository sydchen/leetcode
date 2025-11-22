#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    bool is_balanced(const vector<int>& freq, int target) {
        for(int v : freq) {
            if (v > 0 && v != target) return false;
        }
        return true;
    }

    int longestBalanced(string s) {
        int n = s.length();
        int max_len = 0;

        for(int i = 0; i < n; i++) {
            vector<int> freq(26, 0);
            for(int j = i; j < n; j++) {
                int diff = s[j] - 'a';
                freq[diff] += 1;

                if(is_balanced(freq, freq[diff])) {
                    max_len = std::max(max_len, j - i + 1);
                }
            }
        }

        return max_len;
    }
};

int main(int argc, const char* argv[])
{
    Solution s;
    cout << s.longestBalanced("abbac"); // 4
    cout << s.longestBalanced("zzabccy"); // 4
    cout << s.longestBalanced("aba"); // 2
}
