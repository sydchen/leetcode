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

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 排序後相同值相鄰，方便去重
        n = len(nums)
        ans = []

        for i in range(n):
            # 跳過重複的第一個數，避免產生重複三元組
            if i > 0 and nums[i-1] == nums[i]:
                continue

            # 固定 nums[i]，用雙指針在右側找兩數之和 == -nums[i]
            target = -nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    ans.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    # 跳過重複值，避免產生重複三元組
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif two_sum < target:
                    left += 1   # 總和太小，左指針右移增大
                else:
                    right -= 1  # 總和太大，右指針左移縮小
        return ans

s = Solution2()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
print(s.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
