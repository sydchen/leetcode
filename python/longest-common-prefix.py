'''
找字串陣列中所有字串的最長公共前綴。

解法：垂直掃描
以第一個字串為基準，逐字元與其他字串比對。
遇到不一致或超出某字串長度，立即回傳當前前綴。

時間複雜度：O(m * n)，m = 最短字串長度，n = 字串數量
空間複雜度：O(1)
'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return strs[0][:i]
        return strs[0]

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))  # "fl"
print(s.longestCommonPrefix(["dog","racecar","car"]))     # ""
print(s.longestCommonPrefix(["a"]))                       # "a"
