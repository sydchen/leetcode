# 這題的關鍵在於觀察「最大絕對值總和 = max(最大子陣列和, |最小子陣列和|)」。
# 因為如果有一段子陣列的和是很大的負數，取絕對值後也可能是最大的值。

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = 0
        cur_max = cur_min = 0

        for x in nums:
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)

            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)

        return max(max_sum, -min_sum)

s = Solution()
print(s.maxAbsoluteSum([1,-3,2,3,-4])) # 5
print(s.maxAbsoluteSum([2,-5,1,-4,3,-2])) # 8

