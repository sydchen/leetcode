'''
這題要設計一個資料結構，可以持續加入新數字，並在每次 add 後回傳目前第 k 大的元素。

核心想法：
只需要保留目前最大的 k 個元素。
如果用 min heap 存這 k 個元素，heap top 會是這 k 個元素中最小的那個，
也就是整個 stream 裡的第 k 大。

例如 k = 3，目前最大的三個數是 [10, 8, 5]。
min heap 的 top 是 5，所以第 3 大就是 5。

解法：Min Heap
1. 初始化時把 nums 做成 min heap
2. 如果 heap 大小超過 k，就一直 pop 最小值，讓 heap 只保留最大的 k 個元素
3. add(val) 時：
   - 如果 heap 還沒滿 k 個，直接 push
   - 如果 val 大於 heap[0]，代表 val 可以進入前 k 大，push 後 pop 掉最小值
   - 如果 val <= heap[0]，代表 val 不影響前 k 大，可以忽略
4. 回傳 heap[0]

為什麼可行：
heap 永遠只保存目前最大的 k 個元素。
而這 k 個元素裡最小的那個，就是整體第 k 大。

時間複雜度：
- constructor: O(n log n)，可以進一步用 heapify 變成 O(n)，再 pop 到 k
- add: O(log k)

空間複雜度：O(k)
'''

import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # 只保留最大的 k 個元素，多出來的小元素不可能成為第 k 大。
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))
