from heapq import heappush, heappop
from typing import List

'''
使用Min Heap來維護當前最小的 k 個數對：
* 因為 nums1 和 nums2 都是排序過的，所以最小的組合一定來自於 nums1[0] 搭配 nums2[0]。
* 依序考慮 nums1[0] 與 nums2[i] 來擴展，維持堆的大小不超過 k。
* 每次彈出當前最小的數對 (nums1[i], nums2[j])，並嘗試擴展下一個可能的數對：
** (nums1[i+1], nums2[j])
** (nums1[i], nums2[j+1])
* 確保不重複訪問相同索引的數對 (i, j)。
'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        min_heap = []
        result = []

        for i in range(min(k, len(nums1))):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))  # (sum, nums1 index, nums2 index)

        # 取 k 個最小數對
        while k > 0 and min_heap:
            _, i, j = heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1

            # 若 nums2[j+1] 存在，則插入 (nums1[i], nums2[j+1])
            if j + 1 < len(nums2):
                heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))

        return result

solution = Solution()
print(solution.kSmallestPairs([1,7,11], [2,4,6], 3))  # [[1,2],[1,4],[1,6]]
print(solution.kSmallestPairs([1,1,2], [1,2,3], 2))  # [[1,1],[1,1]]
print(solution.kSmallestPairs([1,2], [3], 3))  # [[1,3],[2,3]]

