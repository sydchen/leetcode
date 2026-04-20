from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = sub_sum = 0
        min_size = float('inf')

        for right in range(n):
            sub_sum += nums[right]
            while sub_sum >= target:
                min_size = min(min_size, right - left + 1)
                sub_sum -= nums[left]
                left += 1

        return 0 if min_size == float('inf') else min_size

s = Solution()
print(s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])) # 2
print(s.minSubArrayLen(target = 4, nums = [1,4,4])) # 1
print(s.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])) # 0
