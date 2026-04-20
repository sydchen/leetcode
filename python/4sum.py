'''
找所有不重複的四元組使其和等於 target。

解法：排序 + 雙層迴圈 + 雙指針（3Sum 的延伸）
1. 排序
2. 外層 i 固定第一個數，跳過重複
3. 內層 j 固定第二個數，跳過重複
4. 雙指針 left/right 找剩下兩個數
5. 找到解後跳過重複的 left 和 right

時間複雜度：O(n³)
空間複雜度：O(1)
'''

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return ans

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))    # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(s.fourSum([2,2,2,2,2], 8))        # [[2,2,2,2]]
print(s.fourSum([1000000000,1000000000,1000000000,1000000000], -294967296))  # []
