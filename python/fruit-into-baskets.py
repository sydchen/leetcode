'''
給一排果樹 fruits[i]，有兩個籃子各只能裝一種水果（無限數量）。
找從連續一段樹採到最多水果的數量。

等價於：找最長的連續子陣列，其中最多只有 2 種不同的值。

解法：Sliding Window
- 用 count map 記錄視窗內各水果的數量
- 右指針不斷擴展；當 distinct 種類 > 2，左指針縮窗直到 <= 2
- 記錄最大視窗長度

時間複雜度：O(n)
空間複雜度：O(1)（map 最多 3 個 key）
'''

from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = ans = 0

        for right, fruit in enumerate(fruits):
            count[fruit] += 1

            # 超過 2 種，縮左端直到恢復 2 種
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans

s = Solution()
print(s.totalFruit([1,2,1]))                      # 3
print(s.totalFruit([0,1,2,2]))                    # 3  ([1,2,2])
print(s.totalFruit([1,2,3,2,2]))                  # 4  ([2,3,2,2])
print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))     # 5  ([1,2,1,1,2])
