'''
關鍵觀察：maxSize 可忽略，只需檢查長度為 minSize 的子字串。
原因：若長度 L 的子字串出現 k 次，其長度 L-1 的前綴至少也出現 k 次，
且更短的子字串更容易滿足 unique 字元數限制，因此最優解必在 minSize 中。

演算法：固定大小為 minSize 的 Sliding Window
- unique：記錄視窗內各字元的出現次數，len(unique) 即為 unique 字元數
- count：記錄每個合法子字串（unique 字元數 <= maxLetters）的出現次數
- 視窗達到 minSize 時判斷是否合法，無論合法與否都移除左端字元、縮回視窗
'''

from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = defaultdict(int)   # 子字串 → 出現次數
        unique = defaultdict(int)  # 視窗內字元 → 出現次數
        result = 0
        left = 0

        for right in range(len(s)):
            unique[s[right]] += 1  # 右端字元加入視窗

            if right - left + 1 == minSize:  # 視窗達到目標大小
                if len(unique) <= maxLetters:  # unique 字元數合法
                    count[s[left:right + 1]] += 1
                    result = max(result, count[s[left:right + 1]])

                # 移除左端字元，維持視窗大小為 minSize
                unique[s[left]] -= 1
                if unique[s[left]] == 0:  # 計數歸零則刪除，確保 len(unique) 正確
                    del unique[s[left]]
                left += 1

        return result

s = Solution()
print(s.maxFreq("aababcaab", 2, 3, 4))  # 2
print(s.maxFreq("aaaa", 1, 3, 3))       # 2
