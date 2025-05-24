class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        steps = [0] * (n + 1)
        steps[1] = 1
        steps[2] = 2

        for i in range(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]

        return steps[n]


s = Solution()
# print(s.climbStairs(2))
print(f"{s.climbStairs(45)} ways")

