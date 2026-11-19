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
                        grid[nx][ny] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)  # 用 BFS 掃描整個島嶼

        return count

    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        """DFS 版本；使用 stack 避免遞迴深度限制。"""
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue

                count += 1
                stack = [(r, c)]
                grid[r][c] = "0"

                while stack:
                    x, y = stack.pop()

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"
                            stack.append((nx, ny))

        return count

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
