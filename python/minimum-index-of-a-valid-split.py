class Solution:
    def minimumIndex(self, nums):
        from collections import Counter

        # 1. Find the dominant element
        count = Counter(nums)
        dom, cnt_total = max(count.items(), key=lambda x: x[1])

        n = len(nums)
        left_dom = 0

        # 2. Scan from left and check split
        for i, x in enumerate(nums):
            if x == dom:
                left_dom += 1

            left_len = i + 1
            right_len = n - left_len
            right_dom = cnt_total - left_dom

            if left_dom * 2 > left_len and right_dom * 2 > right_len:
                return i

        return -1

