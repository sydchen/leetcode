class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

'''
tails[i] 表示 長度為 i+1 的遞增子序列中最小的結尾元素。
nums = [10, 9, 2, 5, 3, 7, 101, 18]
tails = [2, 3, 7, 18]
'''

import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        tails = []
        for num in nums:
            i = bisect.bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num
        return len(tails)



s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(s.lengthOfLIS([0,1,0,3,2,3])) # 4
print(s.lengthOfLIS([7,7,7,7,7,7,7])) # 1
