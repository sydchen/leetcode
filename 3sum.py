from typing import List
from collections import defaultdict

# Trivil Cases
# Case 1: 3 zeros (0, 0, 0)
# Case 2: 1 zero, 1 positive and 1 negative (0, 3, -3)
# Case 3: 1 positive and 2 negative (6, -2, -4)
# Case 4: 2 positive and 1 negative (2, 4, -6)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negatives = defaultdict(int)
        positives = defaultdict(int)
        zeros = 0
        ans = []

        for n in nums:
            if n > 0:
                positives[n] += 1
            elif n == 0:
                zeros += 1
            else:
                negatives[n] += 1

        # Case 2
        if zeros > 0:
            for p in positives:
                if -p in negatives: ans.append([-p, 0, p])

            if zeros >= 3: ans.append([0, 0, 0])

        # Case 3 and Case 4
        for set_a, set_b in ((negatives, positives), (positives, negatives)):
            lst = list(set_a.keys())
            length = len(lst)
            permutation = []
            for i in range(0, length):
                if set_a[lst[i]] > 1: permutation.append((lst[i], lst[i])) # ex: (-6, 3, 3) or (6, -3, -3)
                for j in range(i + 1, length):
                    permutation.append((lst[i], lst[j]))

            for x, y in permutation:
                target = x + y
                if -target in set_b: ans.append(sorted([-target, x, y]))

        return ans

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
print(s.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
