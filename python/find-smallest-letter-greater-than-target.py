'''
在排序字元陣列中找嚴格大於 target 的最小字元。
若不存在則回傳 letters[0]（循環）。

解法：Binary Search
找第一個 > target 的位置，即找最左邊 letters[mid] > target 的 mid。
- letters[mid] > target → 可能是答案，繼續往左找：right = mid
- letters[mid] <= target → 答案在右側：left = mid + 1
若 left == len(letters)，表示所有字元都 <= target，循環回傳 letters[0]。

時間複雜度：O(log n)
'''

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)

        while left < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1

        return letters[left % len(letters)]  # 循環：left == len 時回傳 letters[0]

s = Solution()
print(s.nextGreatestLetter(['c','f','j'], 'a'))  # c
print(s.nextGreatestLetter(['c','f','j'], 'c'))  # f
print(s.nextGreatestLetter(['c','f','j'], 'j'))  # c（循環）
print(s.nextGreatestLetter(['x','x','y','y'], 'z'))  # x（循環）
