/* Suppose there are N elements and they range from A to B. */
/* Then the maximum gap will be no smaller than ceiling[(B - A) / (N - 1)] */
/* Let the length of a bucket to be len = ceiling[(B - A) / (N - 1)], then we will have at most num = (B - A) / len + 1 of bucket */
/* for any number K in the array, we can easily find out which bucket it belongs by calculating loc = (K - A) / len and therefore maintain the maximum and minimum elements in each bucket. */
/* Since the maximum difference between elements in the same buckets will be at most len - 1, so the final answer will not be taken from two elements in the same buckets. */
/* For each non-empty buckets p, find the next non-empty buckets q, then q.min - p.max could be the potential answer to the question. Return the maximum of all those values. */
// https://leetcode.com/discuss/51039/12ms-c-suggested-solution
#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;

        auto lu = minmax_element(nums.begin(), nums.end());
        int l = *lu.first, u = *lu.second;
        int gap = max((u - l) / (n - 1), 1);
        int m = (u - l) / gap + 1;
        vector<int> bucketsMin(m, INT_MAX);
        vector<int> bucketsMax(m, INT_MIN);
        for (int num : nums) {
            int k = (num - l) / gap;
            if (num < bucketsMin[k]) bucketsMin[k] = num;
            if (num > bucketsMax[k]) bucketsMax[k] = num;
        }

        int i = 0, j;
        gap = bucketsMax[0] - bucketsMin[0];
        while (i < m) {
            j = i + 1;
            while (j < m && bucketsMin[j] == INT_MAX && bucketsMax[j] == INT_MIN)
                j++;
            if (j == m) break;
            gap = max(gap, bucketsMin[j] - bucketsMax[i]);
            i = j;
        }
        return gap;
    }
};

int main()
{
    vector<int> num {-1, -4, -2, -21, 3, 21, 68, 8, -2};
    Solution sol;
    cout << sol.maximumGap(num);
}
