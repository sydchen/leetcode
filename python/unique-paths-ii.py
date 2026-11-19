from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        # dp[r][c]：走到 (r, c) 的不同路徑數。
        dp = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    continue

                if r == 0 and c == 0:
                    dp[r][c] = 1
                    continue

                from_top = dp[r - 1][c] if r > 0 else 0
                from_left = dp[r][c - 1] if c > 0 else 0
                dp[r][c] = from_top + from_left

        return dp[-1][-1]


solution = Solution()
print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
print(solution.uniquePathsWithObstacles([[0, 1], [0, 0]]))  # 1
