from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        while left < right and top < bottom:
            # 從左至右
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # 從上至下
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # 確保還有行列未遍歷
            if not (left < right and top < bottom):
                break

            # 從右至左
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # 從下至上
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
