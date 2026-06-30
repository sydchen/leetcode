'''
這題給一組已依 start 排序、且彼此不重疊的 intervals，
要插入 newInterval，並在需要時合併重疊區間。

核心想法：
因為 intervals 已經排序且不重疊，可以分成三段處理：
1. 完全在 newInterval 左邊的 intervals
2. 和 newInterval 有重疊的 intervals
3. 完全在 newInterval 右邊的 intervals

對於中間重疊區間，只要持續更新 newInterval 的左右邊界：
- newInterval[0] = min(newInterval[0], intervals[i][0])
- newInterval[1] = max(newInterval[1], intervals[i][1])

解法：Linear Scan
1. 先把 end < newInterval[0] 的 intervals 加進答案
2. 接著合併所有 start <= newInterval[1] 的 intervals
3. 把合併後的 newInterval 加進答案
4. 最後把剩下 intervals 加進答案

時間複雜度：O(n)
空間複雜度：O(n)
'''

class Solution:
    def insert(self, intervals, newInterval):
        ans = []
        i = 0
        n = len(intervals)

        # 第一段：完全在 newInterval 左邊，不會重疊。
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # 第二段：和 newInterval 重疊，持續擴大 newInterval 範圍。
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        ans.append(newInterval)

        # 第三段：完全在 newInterval 右邊。
        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans


s = Solution()
print(s.insert([[1, 3], [6, 9]], [2, 5]))
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
