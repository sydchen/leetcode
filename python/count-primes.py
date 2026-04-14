'''
找出嚴格小於 n 的質數個數。

解法：Sieve of Eratosthenes
- is_prime[i] 表示 i 是否為質數
- 從 2 開始，把每個質數的倍數標記為合數
- 內層從 i*i 開始（i*2 ~ i*(i-1) 已被更小的質數處理過）
- 外層只跑到 √n（超過 √n 的合數必有小於 √n 的因數，早已被劃掉）

時間複雜度：O(n log log n)
空間複雜度：O(n)
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        i = 2
        while i * i < n:
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
            i += 1

        return sum(is_prime)

s = Solution()
print(s.countPrimes(10))   # 4  (2, 3, 5, 7)
print(s.countPrimes(0))    # 0
print(s.countPrimes(1))    # 0
