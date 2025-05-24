from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0
        max_reach = 0
        end = 0 # 跳躍的邊界

        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == end:  # 需要進行一次跳躍
                jumps += 1
                end = max_reach  # 更新下一次跳躍的邊界

            if end >= n - 1:
                break

        return jumps

sol = Solution()
print(sol.jump([2,3,1,1,4]))  # 2
print(sol.jump([2,3,0,1,4]))  # 2

