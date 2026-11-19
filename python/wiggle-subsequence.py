from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # up / down：最後一段差值分別為正 / 負的最長 wiggle 長度。
        up = 1
        down = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # 目前向上，接在最後一次向下的序列後面。
                up = down + 1
            elif nums[i] < nums[i - 1]:
                # 目前向下，接在最後一次向上的序列後面。
                down = up + 1
            # 相等時差值為 0，不能延長 wiggle sequence。

        return max(up, down)


solution = Solution()
print(solution.wiggleMaxLength([1, 7, 4, 9, 2, 5]))  # 6
print(solution.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))  # 7
print(solution.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 2
