'''
這題給 coins 和 amount，要用最少硬幣數湊出 amount。
每種硬幣可以使用無限次。
如果無法湊出 amount，回傳 -1。

核心想法：
用 DP 記錄每個金額的最少硬幣數。
dp[x] 表示湊出金額 x 需要的最少硬幣數。

狀態轉移：
如果最後一枚硬幣是 coin，那前一個狀態就是 x - coin。
所以：
dp[x] = min(dp[x], dp[x - coin] + 1)

base case：
dp[0] = 0，湊出 0 元需要 0 枚硬幣。

解法：Bottom-up DP
1. 初始化 dp，長度 amount + 1
2. 用 amount + 1 當作不可能的大值
3. 從 1 到 amount 逐一計算最少硬幣數
4. 最後如果 dp[amount] 還是大值，代表無法湊出，回傳 -1

時間複雜度：O(amount * len(coins))
空間複雜度：O(amount)
'''

class Solution:
    def coinChange(self, coins, amount):
        impossible = amount + 1
        dp = [impossible] * (amount + 1)
        dp[0] = 0

        for money in range(1, amount + 1):
            for coin in coins:
                if coin <= money:
                    dp[money] = min(dp[money], dp[money - coin] + 1)

        return -1 if dp[amount] == impossible else dp[amount]


s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([2], 3))
print(s.coinChange([1], 0))
