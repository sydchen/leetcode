'''
n 枚硬幣排成階梯，第 k 行需要 k 枚，找能排出幾個完整行。

前 k 行總共需要 k*(k+1)/2 枚硬幣。
找最大的 k 使得 k*(k+1)/2 <= n。

解法一：Binary Search
在 [1, n] 內找最大的 k 滿足 k*(k+1)/2 <= n。

解法二：數學公式
k*(k+1)/2 <= n → k² + k - 2n <= 0
解一元二次方程：k = (-1 + sqrt(1 + 8n)) / 2

時間複雜度：O(log n) / O(1)
'''

import math
from typing import List

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2  # 取上界，避免無限迴圈
            if mid * (mid + 1) // 2 <= n:
                left = mid
            else:
                right = mid - 1
        return left

class Solution2:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + math.sqrt(1 + 8 * n)) / 2)

s = Solution()
print(s.arrangeCoins(5))   # 2（1+2=3 枚，第 3 行不夠）
print(s.arrangeCoins(8))   # 3（1+2+3=6 枚，第 4 行不夠）

s2 = Solution2()
print(s2.arrangeCoins(5))  # 2
print(s2.arrangeCoins(8))  # 3
