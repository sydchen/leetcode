'''
這題要合併所有重疊的 intervals。

核心想法：
如果先按照 start 由小到大排序，那只需要從左到右看目前 interval 是否能接到上一個合併結果。

對目前 interval = [start, end]：
- 如果 start <= merged 最後一段的 end，代表有重疊，可以合併
- 否則代表沒有重疊，直接新增一段 interval

注意：
[1, 4] 和 [4, 5] 也算重疊，因為 start == last_end。
合併後是 [1, 5]。

解法：Sort + Linear Scan
1. intervals 依照 start 排序
2. 逐一掃過 intervals
3. 如果 merged 是空的，或目前 start > merged[-1][1]，新增 interval
4. 否則更新 merged[-1][1] = max(merged[-1][1], end)

時間複雜度：O(n log n)，排序
空間複雜度：O(n)，儲存答案
'''

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval[0])
        merged = []

        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                # 有重疊時，只需要延長最後一段的右邊界。
                merged[-1][1] = max(merged[-1][1], end)

        return merged


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1, 4], [4, 5]]))
