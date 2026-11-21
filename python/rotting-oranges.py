from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # 所有原本腐爛的橘子同時作為 BFS 起點。
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue and fresh > 0:
            # 處理同一分鐘開始時已腐爛的橘子。
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert solution.orangesRotting([[0, 2]]) == 0
    print("Examples passed")
