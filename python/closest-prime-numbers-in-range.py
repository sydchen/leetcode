'''
找 [left, right] 內差值最小的兩個質數 [p1, p2]（p1 < p2）。
若有多組差值相同，取 p1 最小的；若不存在，回傳 [-1, -1]。

解法：Sieve of Eratosthenes
1. 篩出 0～right 內所有質數
2. 取出 [left, right] 內的質數列表
3. 掃描相鄰質數對，取差值最小的

時間複雜度：O(right * log log right)
空間複雜度：O(right)
'''

from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        i = 2
        while i * i <= right:
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False
            i += 1

        primes = [p for p in range(left, right + 1) if is_prime[p]]

        if len(primes) < 2:
            return [-1, -1]

        best = [primes[0], primes[1]]
        for i in range(1, len(primes) - 1):
            if primes[i + 1] - primes[i] < best[1] - best[0]:
                best = [primes[i], primes[i + 1]]
            if best[1] - best[0] <= 2:  # 差值不可能比 2 更小（2,3 除外差為1），提早結束
                break

        return best

s = Solution()
print(s.closestPrimes(10, 19))   # [11, 13]
print(s.closestPrimes(4, 6))     # [-1, -1]
print(s.closestPrimes(1, 1000000))  # [2, 3]
