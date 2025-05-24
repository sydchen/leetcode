from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # 依照氣球的右端點 (xend) 進行排序
        points.sort(key=lambda x: x[1])

        arrows = 1  # 至少需要 1 支箭
        arrow_pos = points[0][1]  # 第一支箭射在第一個氣球的 xend

        for xstart, xend in points:
            if xstart > arrow_pos:  # 需要新的一支箭
                arrows += 1
                arrow_pos = xend

        return arrows


sol = Solution()
print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))  # 輸出: 2
print(sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))  # 輸出: 4
print(sol.findMinArrowShots([[1,10],[2,8],[3,6],[4,5]]))  # 輸出: 1

