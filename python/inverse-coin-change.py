class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        if n == 0:
            return []

        # Prepend 1 for amount 0 (one way to make 0: use no coins)
        # This is needed because LeetCode's input is 1-indexed
        numWays = [1] + numWays

        n = len(numWays)
        coins = []

        # dp[i] = number of ways to make amount i with coins found so far
        dp = [0] * n
        dp[0] = 1  # Base case: one way to make 0

        # Process each amount sequentially
        for amount in range(1, n):
            # If current ways are less than expected, add this amount as a coin
            if dp[amount] < numWays[amount]:
                coins.append(amount)

                # Update dp array using standard coin change DP
                for i in range(amount, n):
                    dp[i] += dp[i - amount]

        # Verify: recompute from scratch with found coins
        verify = [0] * n
        verify[0] = 1

        for coin in coins:
            for i in range(coin, n):
                verify[i] += verify[i - coin]

        # Return coins only if they produce the exact input
        return sorted(coins) if verify == numWays else []

s = Solution()
print(s.findCoins([0,1,0,2,0,3,0,4,0,5]))

