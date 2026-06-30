'''
這題青蛙要從第一顆石頭跳到最後一顆，再跳回第一顆。
每顆石頭最多只能踩一次，除了起點和終點。
目標是讓整趟路徑中的最大單次跳躍距離最小。

核心想法：
最好的走法是去程踩一組交錯石頭，回程踩另一組交錯石頭。
例如 stones = [0, 2, 5, 6, 7]

可以走：
0 -> 5 -> 7 -> 6 -> 2 -> 0

這種交錯走法會讓最大跳躍只需要考慮「跨過一顆石頭」的距離：
stones[i] - stones[i - 2]

為什麼不是只看相鄰距離：
因為每顆中間石頭只能踩一次，去程和回程不能都使用同一顆石頭。
所以路徑中一定會出現跳過某顆石頭的情況。

解法：Greedy
1. 如果只有兩顆石頭，答案就是 stones[1] - stones[0]
2. 否則掃過 i = 2 到 n - 1
3. 取 max(stones[i] - stones[i - 2])

時間複雜度：O(n)
空間複雜度：O(1)
'''

class Solution:
    def maxJump(self, stones):
        if len(stones) == 2:
            return stones[1] - stones[0]

        ans = 0

        for i in range(2, len(stones)):
            ans = max(ans, stones[i] - stones[i - 2])

        return ans


s = Solution()
print(s.maxJump([0, 2, 5, 6, 7]))
print(s.maxJump([0, 3, 9]))
