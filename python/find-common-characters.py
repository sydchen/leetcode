'''
這題要找出每個 word 都有出現的字元，而且要保留重複次數。
例如 "bella", "label", "roller" 都有：
- e 出現至少 1 次
- l 出現至少 2 次
所以答案是 ["e", "l", "l"]。

核心想法：
某個字母能出現在答案中的次數，取決於它在所有 word 裡的最小出現次數。
例如 l 在三個 word 裡分別出現 2、2、2 次，答案就有 2 個 l。
如果某字母在其中一個 word 出現 0 次，最小值就是 0，答案不放它。

解法：Counting Array
1. common_count 記錄目前每個字母在所有已處理 word 中的最小出現次數
   - 題目限制 word 長度最多 100，所以 common_count 初始值設成 101
2. 逐一處理每個 word：
   - 先用暫存 count 統計目前 word 的字母次數
   - 對 26 個字母做 common_count[i] = min(common_count[i], count[i])
3. 最後根據 common_count 組出答案

效能：
題目只包含小寫英文字母，用 26 格 list 比 dict / Counter 少掉 hash 成本。

時間複雜度：O(total_length + 26 * n)，n = len(words)
空間複雜度：O(1)，common_count 和每輪暫存 count 都固定 26 格
'''

class Solution:
    def commonChars(self, words):
        common_count = [101] * 26

        for word in words:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            for i in range(26):
                common_count[i] = min(common_count[i], count[i])

        ans = []

        for i in range(26):
            char = chr(ord('a') + i)
            ans.extend([char] * common_count[i])

        return ans


s = Solution()
print(s.commonChars(["bella", "label", "roller"]))
print(s.commonChars(["cool", "lock", "cook"]))
