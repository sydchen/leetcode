# TO READ
'''
nice pair 條件：
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

把等式移項：
nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])

所以每個數字只需要算出 diff = num - rev(num)。
如果目前 diff 之前已經出現 k 次，代表目前這個 num 可以和前面 k 個相同 diff 的數字組成 nice pair。

解法：Hash Map 計數
1. 逐一走過 nums
2. 計算 diff = num - rev(num)
3. ans += count[diff]
4. count[diff] += 1

效能調整：
1. Python 裡 str(num)[::-1] 反轉短數字通常比手寫 while 逐位處理更快
2. 使用 dict.get(diff, 0)，不需要 defaultdict import
3. n 最大 10^5，pair 數最多約 5 * 10^9，Python int 可安全承接，所以最後再取 mod，避免每輪都做 %

時間複雜度：O(n * d)，n = len(nums)，d = 數字位數
空間複雜度：O(n)
'''

class Solution:
    def countNicePairs(self, nums):
        mod = 10 ** 9 + 7
        count = {}
        ans = 0

        for num in nums:
            diff = num - int(str(num)[::-1])
            seen = count.get(diff, 0)
            ans += seen
            count[diff] = seen + 1

        return ans % mod


s = Solution()
print(s.countNicePairs([42, 11, 1, 97]))
print(s.countNicePairs([13, 10, 35, 24, 76]))
