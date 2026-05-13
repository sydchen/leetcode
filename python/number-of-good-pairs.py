from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums):
        count = defaultdict(int)

        ans = 0

        for x in nums:
            ans += count[x]
            count[x] += 1

        return ans


s = Solution()
print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(s.numIdenticalPairs([1, 1, 1, 1]))
print(s.numIdenticalPairs([1, 2, 3]))
