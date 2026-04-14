'''
白色磚塊以區間 tiles[i]=[l,r] 給定，地毯長度 carpetLen，
找地毯最多能蓋住幾塊白磚。

解法：排序 + 前綴和 + Binary Search
最佳放置必定從某個磚塊的左端點開始（往左移只會減少覆蓋）。

對每個磚塊 i，地毯從 tiles[i][0] 開始，右端為 tiles[i][0] + carpetLen - 1：
1. 二分搜找最後一個左端點 <= 地毯右端的磚塊 j
2. 若 tiles[j][1] <= 地毯右端：tiles[i..j] 全部覆蓋 = prefix[j+1] - prefix[i]
3. 若 tiles[j][1] >  地毯右端：tiles[j] 部分覆蓋 = prefix[j] - prefix[i] + (地毯右端 - tiles[j][0] + 1)

時間複雜度：O(n log n)
'''

import bisect
from typing import List

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)

        # prefix[i] = 前 i 個磚塊區間的總長度
        prefix = [0] * (n + 1)
        for i, (l, r) in enumerate(tiles):
            prefix[i + 1] = prefix[i] + (r - l + 1)

        ans = 0
        lefts = [t[0] for t in tiles]  # 各磚塊左端點，用於二分搜

        for i, (l, r) in enumerate(tiles):
            carpet_end = l + carpetLen - 1

            # 找最後一個左端點 <= carpet_end 的磚塊
            j = bisect.bisect_right(lefts, carpet_end) - 1

            if tiles[j][1] <= carpet_end:
                # tiles[i..j] 全部覆蓋
                covered = prefix[j + 1] - prefix[i]
            else:
                # tiles[j] 部分覆蓋
                covered = prefix[j] - prefix[i] + (carpet_end - tiles[j][0] + 1)

            ans = max(ans, covered)

        return ans

s = Solution()
print(s.maximumWhiteTiles([[1,5],[10,11],[12,18],[20,25],[30,32]], 10))  # 9
print(s.maximumWhiteTiles([[10,11],[1,1]], 2))                           # 2
