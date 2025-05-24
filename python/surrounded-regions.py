from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])

        # DFS 標記所有與邊界相連的 'O' 為 'T'
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r + 1, c)  # 下
            dfs(r - 1, c)  # 上
            dfs(r, c + 1)  # 右
            dfs(r, c - 1)  # 左

        # 遍歷邊界，將與邊界相連的 'O' 標記為 'T'
        for r in range(rows):
            dfs(r, 0)  # 左邊界
            dfs(r, cols - 1)  # 右邊界
        for c in range(cols):
            dfs(0, c)  # 上邊界
            dfs(rows - 1, c)  # 下邊界

        # 遍歷整個 board，處理標記：
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"  # 內部被包圍的 O 變成 X
                elif board[r][c] == "T":
                    board[r][c] = "O"  # 邊界連通的 O 還原


# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         if not board:
#             return

#         rows, cols = len(board), len(board[0])
#         queue = deque()

#         # 把所有邊界上的 'O' 加入 queue，並標記為 'T'
#         for r in range(rows):
#             if board[r][0] == "O":
#                 queue.append((r, 0))
#             if board[r][cols - 1] == "O":
#                 queue.append((r, cols - 1))
#         for c in range(cols):
#             if board[0][c] == "O":
#                 queue.append((0, c))
#             if board[rows - 1][c] == "O":
#                 queue.append((rows - 1, c))

#         while queue:
#             r, c = queue.popleft()
#             if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
#                 board[r][c] = "T"
#                 queue.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])

#         # 遍歷整個 board，處理標記：
#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c] == "O":
#                     board[r][c] = "X"
#                 elif board[r][c] == "T":
#                     board[r][c] = "O"

solution = Solution()
board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]

solution.solve(board)
for row in board:
    print(row)


board = [["X"]]

solution.solve(board)
for row in board:
    print(row)
