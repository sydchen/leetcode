from typing import List
from collections import Counter
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
2. 建立所有 (-frequency, number) 的列表，用 heapify 在 O(m) 時間內建堆
3. pop k 次，每次取出的 number 就是目前頻率最高的元素

時間複雜度：O(n + k log m)，n 為陣列長度，m 為不同數字的數量
空間複雜度：O(m)
'''

class Solution:
    # 4ms
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        # heapq 是 min heap，所以用負 frequency 模擬 max heap。
        maxh = [(-count, x) for x, count in freq.items()]
        heapq.heapify(maxh)

        topk = []
        for _ in range(k):
            _, x = heapq.heappop(maxh)
            topk.append(x)

        return topk

    # 12ms
    def topKFrequentBucket(self, nums: List[int], k: int) -> List[int]:
        """分桶法，時間與額外空間都是 O(n)。"""
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        # buckets[freq] 存放恰好出現 freq 次的數字。
        for num, freq in counts.items():
            buckets[freq].append(num)

        answer = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                answer.append(num)
                if len(answer) == k:
                    return answer

        return answer

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2)) # [1, 2]
print(s.topKFrequent([1, 2], 2))
