'''
從排序陣列找 k 個最接近 x 的元素，平手取較小值，結果升序排列。

解法：Binary Search 找視窗左端點
答案必為長度 k 的連續子陣列 arr[left:left+k]。
在 [0, n-k] 內二分搜 left：

比較 arr[mid] 和 arr[mid+k] 哪個離 x 更遠：
- x - arr[mid] > arr[mid+k] - x：左端點 arr[mid] 比右端點 arr[mid+k] 更遠
  → 視窗應右移，left = mid + 1
- 否則：視窗應左移或維持，right = mid

視窗的左端是 arr[mid]，右端是 arr[mid+k-1]，但我們要決定視窗要往左還是往右移，所以比較的是左端點 arr[mid] 和下一個候選視窗的左端點
arr[mid+1] 所排除/納入的元素：

當前視窗：  arr[mid],   arr[mid+1], ..., arr[mid+k-1]
右移一格：  arr[mid+1], arr[mid+2], ..., arr[mid+k]

右移一格 = 移除 arr[mid]，納入 arr[mid+k]

所以問題變成：arr[mid] 和 arr[mid+k] 哪個留著比較好？

時間複雜度：O(log(n-k) + k)
'''

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]

s = Solution()
print(s.findClosestElements([1,2,3,4,5], 4, 3))   # [1,2,3,4]
print(s.findClosestElements([1,2,3,4,5], 4, -1))  # [1,2,3,4]
print(s.findClosestElements([1,3,5,7,9], 3, 6))   # [3,5,7]
