'''
Alice 給出一盒 a，Bob 給出一盒 b。
交換後兩人的糖果總數要相同：

sumAlice - a + b == sumBob - b + a

移項後：
2 * (a - b) == sumAlice - sumBob
a - b == (sumAlice - sumBob) / 2

令 diff = (sumAlice - sumBob) // 2。
對 Alice 的每個盒子 a，要找 Bob 是否有一盒 b = a - diff。

解法：Hash Set
1. 算出 Alice 和 Bob 的總和差距 diff
2. 把 bobSizes 放進 set，讓查找 b 是否存在變成 O(1)
3. 掃過 aliceSizes，找到第一個 a 使得 a - diff 在 Bob 的 set 裡
4. 回傳 [a, a - diff]

效能：
使用 set 查找比雙層迴圈快；不用排序，所以保留 O(m + n)。

時間複雜度：O(m + n)，m = len(aliceSizes)，n = len(bobSizes)
空間複雜度：O(n)
'''

class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob_set = set(bobSizes)

        for alice in aliceSizes:
            bob = alice - diff
            if bob in bob_set:
                return [alice, bob]


s = Solution()
print(s.fairCandySwap([1, 1], [2, 2]))
print(s.fairCandySwap([1, 2], [2, 3]))
print(s.fairCandySwap([2], [1, 3]))
