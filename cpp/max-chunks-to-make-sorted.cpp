// https://leetcode.com/problems/max-chunks-to-make-sorted/discuss/113497/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int max_trunks = 0, max_ele = -1;
        for (int i = 0; i < arr.size(); i++) {
            max_ele = max(max_ele, arr[i]);
            if (max_ele == i) max_trunks += 1;
        }

        return max_trunks;
    }
};


int main()
{
    Solution s;

    vector<int> arr1 { 4, 3, 2, 1, 0 };
    cout << s.maxChunksToSorted(arr1) << endl; // 1
    vector<int> arr2 { 1, 0, 2, 3, 4 };
    cout << s.maxChunksToSorted(arr2) << endl; // 4

}
