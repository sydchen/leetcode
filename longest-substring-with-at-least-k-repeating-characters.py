#  Divide And Conquer
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solutions/87768/4-lines-python/
# 很聰明漂亮的解法. 找出出現頻率小於k的字元, 如果找不到代表最大解
# 如果找到, 根據該字元c, 切成多個sub strings, 因為substring不會包含該字元
# 找出substrings中是否有符合條件的, ex: s=acccabbfb, k = 3, c=a => substrings=[ccc, bbfb], 找到 ccc符合

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(c))

        return len(s)

s = Solution();
print(s.longestSubstring("aaabb", 3)) # 3
print(s.longestSubstring("ababbc", 2)) # 5

