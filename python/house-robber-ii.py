'''
這題是 House Robber 的環狀版本。
第一間和最後一間相鄰，所以不能同時偷。

核心想法：
既然第一間和最後一間不能同時偷，最終答案一定屬於以下兩種情況之一：
1. 不偷最後一間，只考慮 nums[0 : n - 1]
2. 不偷第一間，只考慮 nums[1 : n]

兩段都變成一般 House Robber 線性問題。
答案取兩者最大值。

解法：
1. 如果只有一間房，直接回傳 nums[0]
2. rob_range(0, n - 1)：偷的範圍不包含最後一間
3. rob_range(1, n)：偷的範圍不包含第一間
4. 回傳兩者最大值

rob_range 使用 O(1) 空間 DP：
- rob：偷目前房子的最大金額
- skip：不偷目前房子的最大金額

時間複雜度：O(n)
空間複雜度：O(1)
'''

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        return max(
            self.rob_range(nums, 0, len(nums) - 1),
            self.rob_range(nums, 1, len(nums))
        )

    def rob_range(self, nums, left, right):
        rob = 0
        skip = 0

        for i in range(left, right):
            prev_skip = skip
            skip = max(skip, rob)
            rob = prev_skip + nums[i]

        return max(rob, skip)


s = Solution()
print(s.rob([2, 3, 2]))
print(s.rob([1, 2, 3, 1]))
print(s.rob([1, 2, 3]))
