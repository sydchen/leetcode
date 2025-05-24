class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 特殊情況
        if numRows == 1 or numRows >= len(s):
            return s

        # 準備 numRows 行的緩衝
        rows = [''] * numRows
        cur_row = 0
        direction = 1  # +1 表示往下，-1 表示往上

        for c in s:
            rows[cur_row] += c
            cur_row += direction

            # 到頂或到底時反向
            if cur_row == 0 or cur_row == numRows - 1:
                direction *= -1

        # 串接所有行
        return ''.join(rows)


sol = Solution()
print(sol.convert("PAYPALISHIRING", 4))  # ➜ "PINALSIGYAHRPI"
print(sol.convert("PAYPALISHIRING", 3))  # ➜ "PAHNAPLSIIGYIR"
print(sol.convert("A", 1))              # ➜ "A"

