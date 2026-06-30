'''
這題要在不能偷相鄰房子的限制下，拿到最多金額。

核心想法：
對每間房子有兩種狀態：
1. rob：偷目前這間
2. skip：不偷目前這間

如果偷目前這間，前一間就不能偷：
rob = previous_skip + nums[i]

如果不偷目前這間，前一間可偷可不偷，取最大：
skip = max(previous_skip, previous_rob)

最後答案是 max(rob, skip)。

解法：DP with O(1) Space
時間複雜度：O(n)
空間複雜度：O(1)
'''

class Solution:
    def rob(self, nums):
        # 有偷目前這間房時，目前能拿到的最大金額
        rob = 0
        # 沒有偷目前這間房時，目前能拿到的最大金額
        skip = 0

        for money in nums:
            prev_skip = skip
            skip = max(skip, rob)
            rob = prev_skip + money

        return max(rob, skip)


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))
