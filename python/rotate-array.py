from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # 處理 k 大於 n 的情況

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums, 3)
print(nums)

nums = [-1,-100,3,99]
s.rotate(nums, 2)
print(nums)
