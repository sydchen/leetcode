from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 下、上、右、左

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"  # 標記為已訪問

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        queue.append((nx, ny))
                        grid[nx][ny] = "0"  # 標記為已訪問

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)  # 用 BFS 掃描整個島嶼
        return count

        # def dfs(r, c):
        #     # 超出邊界 or 遇到水，則返回
        #     if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
        #         return

        #     # 標記為已訪問（變成水）
        #     grid[r][c] = "0"

        #     # 探索四個方向
        #     dfs(r + 1, c)  # 下
        #     dfs(r - 1, c)  # 上
        #     dfs(r, c + 1)  # 右
        #     dfs(r, c - 1)  # 左

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":  # 找到新島嶼
        #             count += 1
        #             dfs(r, c)  # 用 DFS 掃描整個島嶼

        # return count

solution = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(solution.numIslands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(solution.numIslands(grid))
