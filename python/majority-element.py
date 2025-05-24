'''
由於多數元素出現的次數超過陣列長度的一半，其他所有元素的總和次數都少於它。
因此，在遍歷陣列時，每當遇到與當前候選者不同的元素時，count 減一；
遇到相同的元素時，count 加一。最終，candidate 會保留為多數元素。
'''
class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

sol = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(sol.majorityElement(nums))  # 輸出：2

nums = [3, 2, 3]
print(sol.majorityElement(nums))  # 輸出：3
