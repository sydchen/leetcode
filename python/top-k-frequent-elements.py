from typing import List
import heapq

'''
這題要找出 nums 中出現頻率最高的 k 個元素。

核心想法：
先統計每個數字出現幾次，再按照出現次數由高到低取前 k 個。

Python 的 heapq 是 min heap，預設會把最小值放在 heap top。
如果要模擬 max heap，可以把 frequency 存成負數：
- 出現 3 次 -> -3
- 出現 2 次 -> -2

min heap 會先 pop 較小的值，所以 -3 會比 -2 先被 pop，
等同於 frequency 3 比 frequency 2 優先。

解法：Hash Map + Heap
1. 用 freq 記錄每個數字出現次數
2. 把 (-frequency, number) 放進 heap
3. pop k 次，每次取出的 number 就是目前頻率最高的元素

時間複雜度：O(n + m log m + k log m)，m = 不同數字數量
空間複雜度：O(m)
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        maxh = []
        topk = []
        for x in freq:
            # heapq 是 min heap，所以用負 frequency 模擬 max heap。
            heapq.heappush(maxh, (-freq[x], x))

        for i in range(k):
            _, x = heapq.heappop(maxh)
            topk.append(x)

        return topk

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2)) # [1, 2]
print(s.topKFrequent([1, 2], 2))
