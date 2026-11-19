# 這題的關鍵是把題目的「插入一個字元」反過來看：

# 若 shorter 是 word 的 predecessor，代表從 word 刪掉剛好一個字元，就能得到 shorter。
# 例如：

# "bda" -> "bdca"

# 因為在 "bda" 中插入 "c" 可得到 "bdca"。

# 反過來，處理 "bdca" 時，嘗試刪掉每個位置：

# 刪 b -> "dca"
# 刪 d -> "bca"
# 刪 c -> "bda"
# 刪 a -> "bdc"

# 若 "bda" 已經出現過，就可以把它的 chain 接上 "bdca"。

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # 先處理較短的字，讓所有可能 predecessor 都已在 dp 中。
        words.sort(key=len)

        # dp[word]：以 word 結尾的最長 string chain 長度。
        dp = {}
        longest_chain = 1

        for word in words:
            dp[word] = 1

            # 從 word 刪除一個字元，得到所有可能的 predecessor。
            for index in range(len(word)):
                predecessor = word[:index] + word[index + 1:]

                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)

            longest_chain = max(longest_chain, dp[word])

        return longest_chain


solution = Solution()
print(solution.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))  # 4
print(solution.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))  # 5
print(solution.longestStrChain(["abcd", "dbqca"]))  # 1
