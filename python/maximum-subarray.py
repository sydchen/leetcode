# Kadane’s Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        currentMax = nums[0]
        globalMax = nums[0]

        for i in range(1, n):
            currentMax = max(nums[i], currentMax + nums[i])
            globalMax = max(globalMax, currentMax)

        return globalMax

