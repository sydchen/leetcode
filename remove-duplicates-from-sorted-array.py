from typing import List

# 1. 使用一個指針 i 來標記存放唯一元素的位置。
# 2. 使用另一個指針 j 遍歷陣列，如果 nums[j] 與 nums[i] 不同，就將其移動到 i+1 的位置。

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

s = Solution()
print(s.removeDuplicates([1,1,2])) # 2
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5

