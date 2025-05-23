from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # 從第二天開始，若今天漲價就賣出（等同於昨天買入）
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit += diff
        return profit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))  # ➜ (5-1)+(6-3)=7
print(sol.maxProfit([1,2,3,4,5]))    # ➜ 每天都漲：(2-1)+(3-2)+(4-3)+(5-4)=4
print(sol.maxProfit([7,6,4,3,1]))    # ➜ 一直下跌，無法賺錢=0

