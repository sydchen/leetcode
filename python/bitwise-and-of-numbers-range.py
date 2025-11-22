class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        # find common prefix
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift


s = Solution()
print(s.rangeBitwiseAnd(5, 7)) #4
