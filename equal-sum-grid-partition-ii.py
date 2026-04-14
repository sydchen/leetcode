from typing import List
from collections import defaultdict

from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)
        # 检查原始、水平翻转、垂直翻转（转置）的四种情况
        if self._can_partition(grid, total):
            return True
        if self._can_partition(grid[::-1], total):
            return True
        trans = list(map(list, zip(*grid)))
        if self._can_partition(trans, total):
            return True
        if self._can_partition(trans[::-1], total):
            return True
        return False

    def _can_partition(self, grid: List[List[int]], total: int) -> bool:
        """
        检查以 grid 的“行”划分（即水平切割），
        是否存在一种切法（可选移除一个“切边”上的元素）使得两边和相等。
        """
        m, n = len(grid), len(grid[0])
        first_row = grid[0]
        top_sum = 0
        seen = set()
        for i, row in enumerate(grid):
            top_sum += sum(row)
            bot_sum = total - top_sum
            diff = top_sum - bot_sum
            seen.update(row)

            # 情况1：不移除任何元素
            if diff == 0:
                return True
            # 情况2：移除第一行两端或当前行左端的一个元素
            if diff == first_row[0] or diff == first_row[-1] or diff == row[0]:
                return True
            # 情况3：移除切边内的其它元素（只能在 i>0 且列数>1 时考虑）
            if n > 1 and i > 0 and diff in seen:
                return True

        return False


sol = Solution()
print(sol.canPartitionGrid([[1, 2], [3, 4]]))  # 輸出：True
