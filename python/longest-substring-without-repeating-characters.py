'''
找最長不含重複字元的子字串長度。

解法：Sliding Window
用 count map 記錄視窗內各字元數量，duplicate 追蹤重複字元的種類數。
當 duplicate > 0，縮左端直到無重複。

時間複雜度：O(n)
空間複雜度：O(1)（最多 128 個 ASCII 字元）
'''

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        duplicate = 0  # 視窗內有幾種字元出現超過一次
        left = ans = 0

        for right, c in enumerate(s):
            count[c] += 1
            if count[c] == 2:   # 剛變成重複
                duplicate += 1

            while duplicate > 0:
                count[s[left]] -= 1
                if count[s[left]] == 1:  # 移除後不再重複
                    duplicate -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
print(s.lengthOfLongestSubstring("bbbbb"))     # 1
print(s.lengthOfLongestSubstring("pwwkew"))    # 3
print(s.lengthOfLongestSubstring(""))          # 0
