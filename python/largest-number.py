'''
這題要把 nums 裡的數字重新排列，組成最大的數字字串。

核心想法：
不能單純按照數字大小排序。
例如 3 和 30：
- "3" + "30" = "330"
- "30" + "3" = "303"
所以 3 應該排在 30 前面。

因此比較兩個數字 a、b 時，要看：
- a + b
- b + a

如果 a + b 比 b + a 大，代表 a 應該排在 b 前面。

解法：Custom Sort
1. 先把 nums 轉成字串
2. 用自訂 comparator 排序
3. 排序後串起來
4. 如果結果開頭是 "0"，代表所有數都是 0，回傳 "0"

時間複雜度：O(n log n * k)，k 是數字字串長度
空間複雜度：O(n)
'''

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        nums.sort(key=cmp_to_key(compare))
        ans = ''.join(nums)

        return '0' if ans[0] == '0' else ans


s = Solution()
print(s.largestNumber([10, 2]))
print(s.largestNumber([3, 30, 34, 5, 9]))
