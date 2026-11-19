from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 搜尋範圍包含 left 和 right。
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert solution.search([5], 5) == 0
    assert solution.search([5], 4) == -1
    print("Examples passed")
