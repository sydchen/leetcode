'''
這題要刪除最少數量的 intervals，讓剩下的 intervals 彼此不重疊。

換個角度看：
刪除最少 = 保留最多不重疊 intervals。

核心想法：
如果要保留最多不重疊區間，每次應該優先選「結束位置最早」的 interval。
因為結束越早，後面留下的可用空間越多。

這和活動選擇問題一樣。

解法：Greedy
1. 先按照 interval[1]，也就是 end，由小到大排序
2. current_end 記錄目前保留的最後一個 interval 的 end
3. 逐一掃過 intervals：
   - 如果 start >= current_end，代表不重疊，可以保留
   - 否則代表重疊，必須刪掉目前 interval
4. 回傳刪除數量

注意：
題目中 [1, 2] 和 [2, 3] 不算重疊，因為前一段 end == 後一段 start 是允許的。

時間複雜度：O(n log n)
空間複雜度：O(1)，不含排序使用的額外空間
'''

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda interval: interval[1])

        removed = 0
        current_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= current_end:
                current_end = end
            else:
                # 和目前保留的 interval 重疊；因為目前 interval end 較早，所以刪掉新來的這段。
                removed += 1

        return removed


s = Solution()
print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
print(s.eraseOverlapIntervals([[1, 2], [2, 3]]))
