from typing import List
import heapq

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solutions/1322101/c-java-python-maxheap-minheap-binary-search-picture-explain-clean-concise/
# Greedy solution
# 把每列第一個元素加進去min heap, 其中top就是1st smallest element, 接著加入該element右邊的element B,
# 之後情況
# 1. element B又在heap top(2nd smallest), 那繼續向右又加入element
# 2. heap中有更小的element C(2nd smallest), pop from heap, 得到r和c後, 往右加入element D

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        n = len(matrix)

        for i in range(n):
            heapq.heappush(minHeap, (matrix[i][0], i, 0))

        ans = None
        for i in range(k):
            (ans, r, c) = heapq.heappop(minHeap)
            if c + 1 < n: heapq.heappush(minHeap, (matrix[r][c+1], r, c + 1))

        return ans

s = Solution();
# print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
print(s.kthSmallest([[-5]], 1))
