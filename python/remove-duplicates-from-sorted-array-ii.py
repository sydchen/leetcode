'''
i < 2
前兩個位置無條件接受，因為任何元素最多保留 2 次，前兩個不可能超標。

nums[j] != nums[i - 2]
nums[i-2] 是目前已寫入序列中，往前數第 2 個的值。

由於陣列已排序，若 nums[j] == nums[i-2]，代表 nums[i-2]、nums[i-1]、nums[j] 這三個值相同，這個元素已出現 ≥ 2 次，跳過。

反之若不相等，表示這個值出現次數還沒到 2，寫入。
'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1

        return i

s = Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))   # 5
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))  # 7

