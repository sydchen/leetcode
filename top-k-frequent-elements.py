from typing import List
import heapq

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
            heapq.heappush(maxh, (-freq[x], x, freq[x]))

        for i in range(k):
            t = heapq.heappop(maxh)
            topk.append(t[1])

        return topk

s = Solution()
# print(s.topKFrequent([1,1,1,2,2,3], 2)) # [1, 2]
print(s.topKFrequent([1, 2], 2))

