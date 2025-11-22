class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0

        while n > 0:
            n //= 5
            count += n

        return count

s = Solution()
print(s.trailingZeroes(3)) # 0
print(s.trailingZeroes(5)) # 1
print(s.trailingZeroes(0)) # 0
