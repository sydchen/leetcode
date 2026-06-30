'''
這題要把所有偶數放到陣列前面，奇數放到後面。
偶數和奇數內部順序不限制。

核心想法：
用雙指標：
- left 從左往右找奇數
- right 從右往左找偶數

當 left 指到奇數、right 指到偶數時，交換它們。
這樣偶數會被移到前面，奇數會被移到後面。

解法：Two Pointers
1. left = 0，right = len(nums) - 1
2. 如果 nums[left] 是偶數，left += 1
3. 如果 nums[right] 是奇數，right -= 1
4. 否則交換 nums[left] 和 nums[right]

時間複雜度：O(n)
空間複雜度：O(1)
'''

class Solution:
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums


s = Solution()
print(s.sortArrayByParity([3, 1, 2, 4]))
print(s.sortArrayByParity([0]))
