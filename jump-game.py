from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # 記錄目前能到達的最遠位置
        for i, jump in enumerate(nums):
            if i > max_reach:  # 如果當前索引已經超過能到達的範圍，則無法前進
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1:
                return True
        return False

sol = Solution()
print(sol.canJump([2,3,1,1,4]))  # True
print(sol.canJump([3,2,1,0,4]))  # False
