'''
這題要找一個 subsequence，符合：
1. subsequence 的總和要大於剩下元素的總和
2. 長度要盡可能短
3. 如果有多個答案，選總和最大的
4. 回傳結果要是 non-increasing order，也就是由大到小

核心想法：
要讓 subsequence 長度最短，就應該優先拿最大的數字。
因為同樣拿一個元素，越大的數字越快讓 subsequence sum 超過剩下的 sum。

題目限制 nums[i] 在 1 到 100 之間，所以不一定要排序。
可以先用 counting array 統計每個數字出現次數，再從 100 往 1 掃。
效果等同於由大到小取數字，但時間從 O(n log n) 降到 O(n + 100)。
當 selected_sum > remaining_sum 時，就已經符合題目條件，立刻回傳目前選到的數字。

解法：Greedy + Counting Array
1. count[num] 記錄 num 出現幾次
2. total 記錄所有數字總和
3. selected_sum 記錄目前選到的 subsequence 總和
4. 從 100 往 1 掃，等同於從大到小逐一選數字：
   - selected_sum += num
   - total -= num，這時 total 代表剩下元素總和
   - 如果 selected_sum > total，回傳答案

為什麼 greedy 可行：
題目要最短長度，所以每一步都應該選目前可選的最大值。
如果不用最大值，改拿較小的值，不可能用更少元素讓總和超過剩下元素。
前 k 大數字也會是所有長度 k 的選法中總和最大的，所以同時滿足 size 相同時總和最大。

時間複雜度：O(n + 100)，n = len(nums)
空間複雜度：O(100)，不含答案
'''

class Solution:
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        total = sum(nums)
        selected_sum = 0
        ans = []

        for num in nums:
            # 從大到小選，讓 subsequence 用最少元素就超過剩下總和。
            selected_sum += num
            total -= num
            ans.append(num)

            if selected_sum > total:
                return ans

class Solution:
    def minSubsequence(self, nums):
        count = [0] * 101
        total = sum(nums)
        selected_sum = 0
        ans = []

        for num in nums:
            count[num] += 1

        # 從最大值往小值取，等同排序後由大到小選，但不用 O(n log n) 排序。
        for num in range(100, 0, -1):
            while count[num] > 0:
                selected_sum += num
                total -= num
                ans.append(num)
                count[num] -= 1

                if selected_sum > total:
                    return ans


s = Solution()
print(s.minSubsequence([4, 3, 10, 9, 8]))
print(s.minSubsequence([4, 4, 7, 6, 7]))
print(s.minSubsequence([6]))
