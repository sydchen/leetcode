'''
這題要比較兩個版本號 version1 和 version2。
版本號由多個 revision 組成，中間用 '.' 分隔。

規則：
- 每個 revision 要當成整數比較
- 前導零不影響數值，例如 "001" == "1"
- 如果一邊 revision 比較少，缺少的部分視為 0

核心想法：
可以 split 後逐段轉 int 比較。
這裡用雙指標逐段解析，避免先建立完整 list。

解法：Two Pointers
1. i 指向 version1 目前解析位置，j 指向 version2
2. 每次讀到下一個 '.' 前，把該段轉成整數
3. 比較兩段數字：
   - num1 > num2 回傳 1
   - num1 < num2 回傳 -1
4. 全部段落都相同就回傳 0

時間複雜度：O(m + n)
空間複雜度：O(1)
'''

class Solution:
    def compareVersion(self, version1, version2):
        i = 0
        j = 0
        m = len(version1)
        n = len(version2)

        while i < m or j < n:
            num1 = 0
            num2 = 0

            while i < m and version1[i] != '.':
                num1 = num1 * 10 + int(version1[i])
                i += 1

            while j < n and version2[j] != '.':
                num2 = num2 * 10 + int(version2[j])
                j += 1

            if num1 > num2:
                return 1
            if num1 < num2:
                return -1

            # 跳過 '.'
            i += 1
            j += 1

        return 0


s = Solution()
print(s.compareVersion("1.2", "1.10"))
print(s.compareVersion("1.01", "1.001"))
print(s.compareVersion("1.0", "1.0.0.0"))
