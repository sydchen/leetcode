'''
對每個 groups[i]，找最小的 index j 使得 elements[j] 能整除 groups[i]。

解法：對每個 group 枚舉其因數，查表找最小 index
1. 先把 elements 存進 hash map：value → 最小 index（相同 value 只保留第一個）
2. 對每個 groups[i]，枚舉它的所有因數（只需到 √groups[i]）
   - 因數成對出現：i 和 groups[i]//i
   - 查 hash map，取所有命中因數中最小的 index
3. 若沒有任何因數在 map 中，回傳 -1

時間複雜度：O(m + n * √max(groups))
  m = len(elements)，n = len(groups)
'''

from typing import List

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        # value → 最小 index（相同 value 只保留第一次出現）
        elem_map = {}
        for j, e in enumerate(elements):
            if e not in elem_map:
                elem_map[e] = j

        result = []
        for g in groups:
            best = float('inf')
            i = 1
            while i * i <= g:
                if g % i == 0:
                    if i in elem_map:
                        best = min(best, elem_map[i])
                    # 因數成對出現（i, g//i），但完全平方數時 i == g//i 只算一個
                    # 例如 g=12,i=2 → 因數對(2,6)，兩個都查
                    # 例如 g=9, i=3 → 因數對(3,3)，只查一次，避免重複
                    if i != g // i and g // i in elem_map:
                        best = min(best, elem_map[g // i])
                i += 1
            result.append(best if best != float('inf') else -1)

        return result

s = Solution()
print(s.assignElements([8, 4, 3], [4, 2]))              # [0, 0, -1]
print(s.assignElements([2, 3, 5, 7], [5, 3, 3]))        # [-1, 1, 0, -1]
print(s.assignElements([8, 4, 3, 2, 4], [4, 2]))        # [0, 0, -1, 1, 0]
