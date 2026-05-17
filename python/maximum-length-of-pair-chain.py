'''
這題要從 pairs 中挑出最長 chain。
如果 p1 = [a, b]，p2 = [c, d]，只有在 b < c 時，p2 才能接在 p1 後面。
不需要使用所有 pair，也可以任意調整選取順序。

核心想法：
每次選 pair 時，應該優先選「結尾最小」的 pair。
因為結尾越小，後面越容易接上更多 pair。

這和活動選擇 / 最多不重疊區間問題一樣：
先按照 right 由小到大排序，然後貪心選擇每個能接上的 pair。

解法：Greedy
1. 將 pairs 按照 pair[1]，也就是 right，由小到大排序
2. current_end 記錄目前 chain 最後一個 pair 的 right
3. 逐一檢查排序後的 pair = [left, right]
4. 如果 current_end < left，代表這個 pair 可以接上目前 chain：
   - ans += 1
   - current_end = right
5. 最後回傳 ans

為什麼 greedy 可行：
當有多個 pair 都可以被選時，選 right 最小的 pair 一定不會比較差。
因為它留下最大的後續空間，能接上的未來 pair 只會更多或一樣多。

時間複雜度：O(n log n)，排序 pairs
空間複雜度：O(1)，除了排序使用的額外空間
'''

class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda pair: pair[1])

        ans = 0
        current_end = -1001

        for left, right in pairs:
            if current_end < left:
                ans += 1
                current_end = right

        return ans


s = Solution()
print(s.findLongestChain([[1, 2], [2, 3], [3, 4]]))
print(s.findLongestChain([[1, 2], [7, 8], [4, 5]]))
