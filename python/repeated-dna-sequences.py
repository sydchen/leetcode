from typing import List

'''
這題要找出 s 中所有出現超過一次、長度為 10 的 DNA substring。

核心想法：
因為目標長度固定是 10，所以可以用固定大小的 sliding window 從左到右掃過。
每次取出目前長度 10 的 substring：
- 如果第一次看到，放進 seen
- 如果之前看過，代表它重複出現，放進 repeated

repeated 用 set 是為了避免同一個 substring 出現很多次時，被重複加入答案。

解法：Sliding Window + Hash Set
1. 如果 s 長度小於 10，直接回傳空 list
2. 從 index 0 掃到 len(s) - 10
3. 取出 s[i:i + 10]
4. 用 seen 判斷是否已出現過
5. 已出現過就加入 repeated，否則加入 seen

時間複雜度：O(n)，每個長度 10 的 substring 視為常數成本
空間複雜度：O(n)，最多儲存 O(n) 個 substring
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)

        return list(repeated)


s = Solution()
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(s.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
