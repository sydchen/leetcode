'''
在矩陣中搜尋 target。
每行從左到右遞增，且每行第一個數大於上一行最後一個數。
→ 整個矩陣等同於一個排序好的一維陣列。

解法：Binary Search
將 mid index 映射回二維座標：
- row = mid // cols
- col = mid % cols

時間複雜度：O(log(m * n))
空間複雜度：O(1)
'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // cols][mid % cols]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))   # True
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # False
