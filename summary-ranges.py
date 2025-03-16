from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:  # 遇到不連續的數字
                if start == nums[i - 1]:  # 單個數字範圍
                    result.append(str(start))
                else:  # 範圍是 start -> nums[i-1]
                    result.append(f"{start}->{nums[i - 1]}")
                start = nums[i]  # 更新起點

        # 加入最後一個區間
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result

sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))  # 輸出: ["0->2","4->5","7"]
print(sol.summaryRanges([0,2,3,4,6,8,9]))  # 輸出: ["0","2->4","6","8->9"]
print(sol.summaryRanges([]))  # 輸出: []
print(sol.summaryRanges([-2,-1,1,2,3,5,6,7]))  # 輸出: ["-2->-1","1->3","5->7"]

