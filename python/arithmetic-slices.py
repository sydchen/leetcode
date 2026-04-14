'''
找陣列中等差數列子陣列的數量（長度至少 3）。

解法：DP
dp = 以 i 結尾的等差子陣列數。
若 arr[i] - arr[i-1] == arr[i-1] - arr[i-2]，dp += 1（延伸前一個等差數列）
否則 dp = 0（斷掉，重新計算）

每個 i 貢獻 dp 個新的合法子陣列加入總數。

時間複雜度：O(n)
空間複雜度：O(1)
'''

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = total = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp += 1
            else:
                dp = 0
            total += dp

        return total

s = Solution()
print(s.numberOfArithmeticSlices([1,2,3,4]))      # 3
print(s.numberOfArithmeticSlices([1,2,3,4,5]))    # 6  (3+2+1)
print(s.numberOfArithmeticSlices([1,2,3,8,9,10])) # 2
print(s.numberOfArithmeticSlices([1,2]))           # 0
