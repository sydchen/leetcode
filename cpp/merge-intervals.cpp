#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

/*
Merge Intervals

先依照 interval 的 start 排序，再從左到右合併。
如果目前 interval 的 start <= merged 最後一段的 end，代表兩段重疊，可以合併。
否則就新增一段 interval。

時間複雜度：O(n log n)
空間複雜度：O(n)
*/

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> merged;
        if (intervals.empty()) {
            return merged;
        }

        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        merged.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); i++) {
            if (merged.back()[1] < intervals[i][0]) {
                merged.push_back(intervals[i]);
            } else {
                // 有重疊時，延長最後一段的右邊界。
                merged.back()[1] = max(merged.back()[1], intervals[i][1]);
            }
        }

        return merged;
    }
};

void printIntervals(const vector<vector<int>>& intervals) {
    for (const auto& interval : intervals) {
        cout << "[" << interval[0] << "," << interval[1] << "]";
    }
    cout << endl;
}

int main() {
    Solution s;

    vector<vector<int>> intervals1{{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    vector<vector<int>> intervals2{{1, 4}, {4, 5}};

    printIntervals(s.merge(intervals1));
    printIntervals(s.merge(intervals2));

    return 0;
}
