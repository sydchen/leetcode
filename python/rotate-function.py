from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        # F(0) = 0 * nums[0] + 1 * nums[1] + ...
        score = sum(index * num for index, num in enumerate(nums))
        max_score = score

        # 每次右旋時，nums[i] 會從最後一格移到 index 0。
        # F(k + 1) = F(k) + total - n * moved_number
        for i in range(n - 1, 0, -1):
            score += total - n * nums[i]
            max_score = max(max_score, score)

        return max_score


solution = Solution()
print(solution.maxRotateFunction([4, 3, 2, 6]))  # 26
print(solution.maxRotateFunction([100]))  # 0
