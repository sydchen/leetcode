'''
在矩陣中搜尋 target，每行從左到右遞增，每列從上到下遞增。

解法：從右上角出發
右上角的特性：
- 往左：數字變小
- 往下：數字變大

因此每次比較可以排除一整行或一整列：
- 當前值 > target → 往左移（排除此列）
- 當前值 < target → 往下移（排除此行）
- 相等 → 找到

時間複雜度：O(m + n)
空間複雜度：O(1)
'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1  # 從右上角出發

        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1  # 當前值太大，往左
            else:
                r += 1  # 當前值太小，往下

        return False

s = Solution()
matrix = [
    [1,  4,  7, 11, 15],
    [2,  5,  8, 12, 19],
    [3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
print(s.searchMatrix(matrix, 5))   # True
print(s.searchMatrix(matrix, 20))  # False
