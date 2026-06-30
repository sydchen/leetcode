'''
這題要找出 nums 中出現次數最多的偶數。
如果有多個偶數出現次數相同，回傳數值最小的那個。
如果沒有任何偶數，回傳 -1。

核心想法：
只需要統計偶數頻率。
掃描 nums 時，同步維護目前最佳答案 best：
1. freq[num] 更高，更新 best
2. freq[num] 相同，但 num 更小，也更新 best

解法：Hash Map Counting
時間複雜度：O(n)
空間複雜度：O(m)，m = 不同偶數數量
'''

class Solution:
    def mostFrequentEven(self, nums):
        freq = {}
        best = -1
        best_count = 0

        for num in nums:
            if num % 2 == 1:
                continue

            freq[num] = freq.get(num, 0) + 1

            if freq[num] > best_count or (freq[num] == best_count and num < best):
                best = num
                best_count = freq[num]

        return best


s = Solution()
print(s.mostFrequentEven([0, 1, 2, 2, 4, 4, 1]))
print(s.mostFrequentEven([4, 4, 4, 9, 2, 4]))
print(s.mostFrequentEven([29, 47, 21, 41, 13, 37, 25, 7]))
