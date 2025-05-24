from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        have = {}
        l, r = 0, 0
        formed = 0
        required = len(need)
        min_len = float("inf")
        min_window = ""

        while r < len(s):
            char = s[r]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            # 當窗口已經符合條件時，嘗試縮小左邊界
            while formed == required:
                # 更新最小窗口
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r+1]

                # 移除最左邊字元
                left_char = s[l]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1  # 若移除後不再滿足 `need`

                l += 1  # 縮小窗口

            r += 1  # 擴展窗口

        return min_window

solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # 輸出："BANC"
print(solution.minWindow("a", "aa"))  # 輸出：""
print(solution.minWindow("a", "a"))  # 輸出："a"
print(solution.minWindow("abc", "cba"))  # 輸出："abc"

