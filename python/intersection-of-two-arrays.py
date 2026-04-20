'''
找兩個陣列的交集，結果不含重複元素。

解法：Set 交集
將兩個陣列轉為 set，直接取交集。

時間複雜度：O(m + n)
空間複雜度：O(m + n)
'''

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

class Solution2:
    '''排序 + 雙指針，不使用 set'''
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not ans or ans[-1] != nums1[i]:  # 避免重複
                    ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans

s = Solution()
print(s.intersection([1,2,2,1], [2,2]))      # [2]
print(s.intersection([4,9,5], [9,4,9,8,4]))  # [9,4]

s2 = Solution2()
print(s2.intersection([1,2,2,1], [2,2]))      # [2]
print(s2.intersection([4,9,5], [9,4,9,8,4]))  # [4,9]
