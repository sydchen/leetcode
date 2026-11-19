from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dp1 = dp2 = dp3 = 0

        for x in nums:
            if x == 1:
                dp1 += 1
            elif x == 2:
                dp2 = max(dp1, dp2) + 1
            else:
                dp3 = max(dp1, dp2, dp3) + 1

        return len(nums) - max(dp1, dp2, dp3)


solution = Solution()
print(solution.minimumOperations([2, 1, 3, 2, 1]))  # 3
print(solution.minimumOperations([1, 3, 2, 1, 3, 3]))  # 2
print(solution.minimumOperations([2, 2, 2, 2, 3, 3]))  # 0
