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

        for _ in range(k - 1):
            _, r, c = heapq.heappop(minHeap)
            if c + 1 < n:
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))

        return heapq.heappop(minHeap)[0]

class Solution2:
    '''
    Binary Search on value
    對值域 [min, max] 二分，countLessEqual(mid) 計算矩陣中 <= mid 的元素數。
    找最小的值使得 countLessEqual >= k。

    countLessEqual：從左下角出發
    - 當前值 <= mid：整列往上都 <= mid，count += r+1，往右移
    - 當前值 >  mid：往上移

    時間複雜度：O(n log(max - min))
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]

        while left < right:
            mid = (left + right) // 2
            if self._countLessEqual(matrix, mid, n) >= k:
                right = mid
            else:
                left = mid + 1

        return left

    def _countLessEqual(self, matrix, mid, n):
        count = 0
        r, c = n - 1, 0  # 從左下角出發
        while r >= 0 and c < n:
            if matrix[r][c] <= mid:
                count += r + 1  # 這一列 0..r 都 <= mid
                c += 1
            else:
                r -= 1
        return count

s = Solution()
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))  # 13
print(s.kthSmallest([[-5]], 1))                            # -5

s2 = Solution2()
print(s2.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))  # 13
print(s2.kthSmallest([[-5]], 1))                            # -5
