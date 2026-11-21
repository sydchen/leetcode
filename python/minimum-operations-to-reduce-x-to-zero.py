from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 兩端移除的元素總和為 x，中間保留的元素總和必須是 target。
        target = sum(nums) - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        left = 0
        window_sum = 0
        longest = -1

        for right, num in enumerate(nums):
            window_sum += num

            # 元素都是正數，從左側縮小視窗會降低總和。
            while window_sum > target:
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                longest = max(longest, right - left + 1)

        return len(nums) - longest if longest != -1 else -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.minOperations([1, 1, 4, 2, 3], 5) == 2
    assert solution.minOperations([5, 6, 7, 8, 9], 4) == -1
    assert solution.minOperations([3, 2, 20, 1, 1, 3], 10) == 5
    print("Examples passed")
