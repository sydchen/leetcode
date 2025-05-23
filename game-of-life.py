'''
必須同時更新所有格子，不能在處理過程中破壞其他格子的狀態。
因此需要用編碼方式暫存狀態變化。
原始狀態 新狀態 暫時值
0        0      0
1        1      1
1        0      2
0        1      3
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None. Modify board in-place.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def count_live_neighbors(x, y):
            directions = [(-1,-1), (-1,0), (-1,1),
                          (0,-1),         (0,1),
                          (1,-1),  (1,0),  (1,1)]
            live = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in [1, 2]: # 1, 2表示目前是活的狀態
                    live += 1
            return live

        # Step 1: 標記所有變化
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # live → die
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 3  # dead → live

        # Step 2: 更新為下一代狀態
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1


board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
sol = Solution()
sol.gameOfLife(board)
print(board)

board = [
    [1, 1],
    [1, 0]
]
sol.gameOfLife(board)
print(board)

