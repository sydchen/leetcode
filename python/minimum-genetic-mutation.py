from collections import deque
from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if end not in bank_set:
            return -1

        genes = ['A', 'C', 'G', 'T']
        q = deque([(start, 0)])
        visited = {start}

        while q:
            gene, step = q.popleft()
            if gene == end:
                return step

            arr = list(gene)
            for i in range(len(arr)):
                original = arr[i]
                for g in genes:
                    if g == original:
                        continue
                    arr[i] = g
                    mut = ''.join(arr)
                    if mut in bank_set and mut not in visited:
                        visited.add(mut)
                        q.append((mut, step + 1))
                arr[i] = original  # 恢復

        return -1


sol = Solution()
print(sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # ➜ 1
print(sol.minMutation("AACCGGTT", "AAACGGTA",
      ["AACCGGTA","AACCGCTA","AAACGGTA"]))                  # ➜ 2
print(sol.minMutation("AAAAACCC","AACCCCCC",
      ["AAAACCCC","AAACCCCC","AACCCCCC"]))                  # ➜ 3

