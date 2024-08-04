#  Divide And Conquer
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solutions/87768/4-lines-python/
# 很聰明漂亮的解法. 找出出現頻率小於k的字元, 如果都大於k, 找到最大解
# 接著根據該字元c, 切成多個sub strings, 因為sub strings不會包含該字元
# 找出sub strings中是否有符合條件的, ex: s=acccabbfb, k = 3, c = a => substrings=[ccc, bbfb] => 3
# s = ababbc, k = 3, c = a => substrings=[b, bbc] => 0

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(c))

        return len(s)

s = Solution();
print(s.longestSubstring("aaabb", 3)) # 3
print(s.longestSubstring("ababbc", 2)) # 5

