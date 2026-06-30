'''
這題要找 nums 裡第 k 大的元素。
注意是排序後第 k 大，不是第 k 個不同的數字。

核心想法：
如果把 nums 由小到大排序，第 k 大的位置會是：
index = len(nums) - k

但完整排序需要 O(n log n)。
這題可以用 Quickselect，只把目標 index 放到正確位置，不需要排好整個陣列。

解法：Quickselect
1. target = len(nums) - k，代表第 k 大在升序排序中的位置
2. 每次選一個 pivot，做 partition：
   - 小於 pivot 的放左邊
   - 大於等於 pivot 的放右邊
   - pivot 最後會被放到它排序後應該在的位置
3. 如果 pivot 位置剛好是 target，回傳 nums[target]
4. 如果 pivot 位置小於 target，只需要往右半邊找
5. 如果 pivot 位置大於 target，只需要往左半邊找

為什麼可行：
partition 後，pivot 的最終位置已經確定。
第 k 大只關心 target 那一格，所以每次都能丟掉一半不可能包含答案的範圍。

時間複雜度：平均 O(n)，最差 O(n^2)
空間複雜度：O(1)
'''

import random


class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot_index = random.randint(left, right)
            pivot_index = self.partition(nums, left, right, pivot_index)

            if pivot_index == target:
                return nums[pivot_index]
            if pivot_index < target:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

    def partition(self, nums, left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        # 把小於 pivot 的數字集中到左邊。
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        nums[store_index], nums[right] = nums[right], nums[store_index]
        return store_index


class Solution2:
    '''
    三向 partition 版本，適合處理大量重複值。

    partition 後會分成三段：
    - nums[left:lt] < pivot
    - nums[lt:gt + 1] == pivot
    - nums[gt + 1:right + 1] > pivot

    如果 target 落在等於 pivot 的區間，直接回傳 pivot。
    這能避免像 [5, 5, 5, 5, 5] 這種資料每次只排除一個元素。
    '''
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]
            lt, gt = self.partition(nums, left, right, pivot)

            if target < lt:
                right = lt - 1
            elif target > gt:
                left = gt + 1
            else:
                return nums[target]

    def partition(self, nums, left, right, pivot):
        # 區間 invariant：
        # nums[left:lt] 都 < pivot
        # nums[lt:i] 都 == pivot
        # nums[i:gt + 1] 還沒處理
        # nums[gt + 1:right + 1] 都 > pivot
        lt = left
        i = left
        gt = right

        while i <= gt:
            if nums[i] < pivot:
                # nums[i] 應該放到左側小於 pivot 的區間；換過來的 nums[i] 已處理過，所以 i 可前進。
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                # nums[i] 應該放到右側大於 pivot 的區間；從 gt 換過來的新值還沒檢查，所以 i 不前進。
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                # nums[i] 等於 pivot，留在中間區間即可。
                i += 1

        return lt, gt


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

s2 = Solution2()
print(s2.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(s2.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(s2.findKthLargest([5, 5, 5, 5, 5], 3))
print(s2.findKthLargest([2, 1], 1))
