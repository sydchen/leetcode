'''
這題給一個 n x n 的 grid，grid[r][c] 代表騎士在第幾步走到這個格子。
要判斷這是不是一個合法的 knight tour：
- 第 0 步必須從左上角 (0, 0) 開始
- 每一步都要符合騎士走法
- 每個數字 0 到 n^2 - 1 都剛好出現一次

核心想法：
不用真的模擬騎士「找下一步」。
因為 grid 已經直接告訴你每一步落在哪個格子，所以只要把：
step -> (row, col)
這個對應存下來，再檢查相鄰兩步是否是合法騎士移動即可。

解法：Position Table
1. 先檢查 grid[0][0] 是否是 0，不是就直接回傳 False
2. 建立 pos，讓 pos[step] = (row, col)
3. 對 step = 1 到 n^2 - 1：
   - 取前一步和目前步的位置差
   - 合法騎士走法只有：
     abs(dr), abs(dc) = (1, 2) 或 (2, 1)
4. 只要有一步不合法就回傳 False，全部合法才回傳 True

為什麼可行：
題目給的 grid 已經是一條完整訪問順序。
驗證 knight tour 的本質就是檢查每一對相鄰步數是否真能用騎士走法連起來。

時間複雜度：O(n^2)
空間複雜度：O(n^2)
'''

class Solution:
    def checkValidGrid(self, grid):
        n = len(grid)

        if grid[0][0] != 0:
            return False

        pos = [None] * (n * n)

        for row in range(n):
            for col in range(n):
                pos[grid[row][col]] = (row, col)

        for step in range(1, n * n):
            prev_row, prev_col = pos[step - 1]
            row, col = pos[step]

            dr = abs(row - prev_row)
            dc = abs(col - prev_col)

            # 合法騎士移動只能是 2x1 或 1x2。
            if not ((dr == 1 and dc == 2) or (dr == 2 and dc == 1)):
                return False

        return True


s = Solution()
print(s.checkValidGrid([[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]]))
print(s.checkValidGrid([[0, 3, 6], [5, 8, 1], [2, 7, 4]]))
