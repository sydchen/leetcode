'''
這題給一個 sorted array。
除了某一個元素只出現一次，其餘元素都剛好出現兩次。
要用 O(log n) 找出那個單獨元素。

核心想法：
在單獨元素出現以前，成對元素會長這樣：
index 偶數、奇數成對：
nums[0] == nums[1]
nums[2] == nums[3]
nums[4] == nums[5]

在單獨元素出現以後，配對位置會錯開：
nums[奇數] == nums[下一個偶數]

所以 binary search 時，把 mid 調成偶數 index：
- 如果 nums[mid] == nums[mid + 1]，代表左半邊配對正常，單獨元素在右邊
- 否則代表配對在 mid 開始被破壞，單獨元素在左邊或就是 mid

時間複雜度：O(log n)
空間複雜度：O(1)
'''

class Solution:
    def singleNonDuplicate(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # 固定讓 mid 指向一組 pair 的第一個位置。
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


s = Solution()
print(s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
