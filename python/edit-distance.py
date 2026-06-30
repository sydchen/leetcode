'''
這題要計算 word1 轉成 word2 的最少操作數。
每次可以做三種操作：
1. Insert 插入一個字元
2. Delete 刪除一個字元
3. Replace 替換一個字元

核心想法：
用 DP 處理兩個字串的 prefix。
dp[i][j] 表示 word1 前 i 個字元，轉成 word2 前 j 個字元所需的最少操作數。

狀態轉移：
1. 如果 word1[i - 1] == word2[j - 1]
   最後一個字元已經相同，不需要新操作：
   dp[i][j] = dp[i - 1][j - 1]

2. 如果 word1[i - 1] != word2[j - 1]
   可以從三種操作中取最小：
   - Delete：dp[i - 1][j] + 1
     刪掉 word1 的最後一個字元
   - Insert：dp[i][j - 1] + 1
     在 word1 後面插入 word2[j - 1]
   - Replace：dp[i - 1][j - 1] + 1
     把 word1[i - 1] 換成 word2[j - 1]

base case：
- dp[i][0] = i，word1 前 i 個字元轉成空字串，需要刪 i 次
- dp[0][j] = j，空字串轉成 word2 前 j 個字元，需要插入 j 次

時間複雜度：O(m * n)
空間複雜度：O(m * n)
'''

class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    ) + 1

        return dp[m][n]


s = Solution()
print(s.minDistance("horse", "ros"))
print(s.minDistance("intention", "execution"))
