'''
這題要找出 s 裡所有長度等於 p、且字母組成和 p 相同的 substring 起始 index。
字母順序不重要，所以只要比較字母出現次數。

核心想法：
anagram 的條件是兩段字串的每個字母出現次數完全相同。
因此可以固定一個長度 len(p) 的 sliding window，在 s 上從左往右移動。

解法：Sliding Window + Counting Array
1. 用 target_count 統計 p 裡 26 個小寫字母的次數
2. 用 window_count 維護目前 s 視窗內的字母次數
3. 每次右邊加入一個字元
4. 如果視窗長度超過 len(p)，左邊移出一個字元
5. 當 window_count == target_count，代表目前視窗是 p 的 anagram，記錄起始 index

效能：
題目只包含小寫英文字母，所以用 26 格 list 比 dict / Counter 少掉 hash 成本。
每次比較兩個 26 格 list 是 O(26)，可視為常數。

時間複雜度：O(26 * len(s))，可視為 O(len(s))
空間複雜度：O(1)，兩個 count array 都固定 26 格
'''

class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []

        target_count = [0] * 26
        window_count = [0] * 26
        ans = []
        window_size = len(p)

        for char in p:
            target_count[ord(char) - ord('a')] += 1

        for right in range(len(s)):
            window_count[ord(s[right]) - ord('a')] += 1

            if right >= window_size:
                left_char = s[right - window_size]
                window_count[ord(left_char) - ord('a')] -= 1

            if window_count == target_count:
                ans.append(right - window_size + 1)

        return ans


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))
