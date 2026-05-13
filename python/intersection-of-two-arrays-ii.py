'''
這題要找兩個陣列的交集，而且重複元素要保留。
如果一個數字在 nums1 出現 a 次、在 nums2 出現 b 次，
答案裡要放 min(a, b) 次。

解法：Counting Array
題目限制 nums1[i], nums2[i] 都在 0 到 1000 之間，所以可以用長度 1001 的陣列記錄次數。

1. 先走過 nums1，count[x] += 1
2. 再走過 nums2
3. 如果 count[x] > 0，代表 x 也出現在 nums1，而且還有剩餘可配對次數
4. 把 x 加入答案，並 count[x] -= 1，避免超過 nums1 的出現次數

效能：
固定範圍內用 list 當 counting array，比 dict / Counter 少掉 hash 成本。

時間複雜度：O(m + n)，m = len(nums1)，n = len(nums2)
空間複雜度：O(1)，count 陣列固定 1001 格
'''

class Solution:
    def intersect(self, nums1, nums2):
        count = [0] * 1001
        ans = []

        for num in nums1:
            count[num] += 1

        for num in nums2:
            if count[num] > 0:
                ans.append(num)
                count[num] -= 1

        return ans


s = Solution()
print(s.intersect([1, 2, 2, 1], [2, 2]))
print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
