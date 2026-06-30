'''
這題只能買一次、賣一次，而且必須先買後賣。
目標是取得最大利潤；如果無法獲利，回傳 0。

核心想法：
每天當作可能的賣出日。
如果今天要賣出，最好的買入價格一定是今天以前看過的最低價格。

所以只需要在掃描 prices 時維護：
- min_price：目前看過的最低買入價
- best_profit：目前能得到的最大利潤

解法：
1. 從左到右掃 prices
2. 更新 min_price = min(min_price, price)
3. 用今天價格賣出，計算 price - min_price
4. 更新 best_profit

時間複雜度：O(n)
空間複雜度：O(1)
'''

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        best_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            best_profit = max(best_profit, price - min_price)

        return best_profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
