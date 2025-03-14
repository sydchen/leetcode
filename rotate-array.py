from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # 避免 k 大於 n
        iter_idx = 0

        while k:
            for i in range(k):
                nums[iter_idx + i], nums[iter_idx + n - k + i] = nums[iter_idx + n - k + i], nums[iter_idx + i]

            n -= k
            iter_idx += k
            k %= n

s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums, 3)
print(nums)

nums = [-1,-100,3,99]
s.rotate(nums, 2)
print(nums)
