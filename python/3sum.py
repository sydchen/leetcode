from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 排序後相同值相鄰，方便去重
        n = len(nums)
        ans = []

        for i in range(n):
            # 跳過重複的第一個數，避免產生重複三元組
            if i > 0 and nums[i-1] == nums[i]:
                continue

            # 固定 nums[i]，用雙指針在右側找兩數之和 == -nums[i]
            target = -nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    ans.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    # 跳過重複值，避免產生重複三元組
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif two_sum < target:
                    left += 1   # 總和太小，左指針右移增大
                else:
                    right -= 1  # 總和太大，右指針左移縮小
        return ans

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
print(s.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
