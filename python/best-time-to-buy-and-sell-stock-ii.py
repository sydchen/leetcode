'''
這題可以交易多次，但同時間最多只能持有一股。
也就是賣出後才能再次買入。

核心想法：
只要相鄰兩天有漲價，就把這段漲幅加進利潤。

例如 prices = [7, 1, 5, 3, 6, 4]
可以看成：
- 1 -> 5 賺 4
- 3 -> 6 賺 3
總共賺 7

這等價於把所有正的相鄰差值加總：
(5 - 1) + (6 - 3)

為什麼可行：
多次交易下，一段連續上漲可以拆成每天買賣，也可以合併成低買高賣，利潤相同。
例如 [1, 2, 3, 4]：
(2 - 1) + (3 - 2) + (4 - 3) = 4 - 1

時間複雜度：O(n)
空間複雜度：O(1)
'''

class Solution:
    def maxProfit(self, prices):
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
