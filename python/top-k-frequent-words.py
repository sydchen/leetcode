'''
這題要找出出現頻率最高的 k 個 words。
排序規則：
1. 頻率高的排前面
2. 如果頻率相同，字典序小的 word 排前面

核心想法：
先統計每個 word 的頻率，再依照題目規則排序：
key = (-frequency, word)

Python sort 會由小到大排序：
- frequency 用負數，讓頻率高的排前面
- word 保持原字串，讓字典序小的排前面

解法：Hash Map + Sort
1. 用 Counter 統計 word 頻率
2. 對所有不同 word 排序
3. 回傳前 k 個 word

時間複雜度：O(n + m log m)，m = 不同 word 數量
空間複雜度：O(m)
'''

from collections import Counter


class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        sorted_words = sorted(count.keys(), key=lambda word: (-count[word], word))
        return sorted_words[:k]


s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
