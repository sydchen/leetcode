'''
將 32-bit 無號整數的位元反轉。

解法：逐位取出 LSB，左移累積到 result
每次從 n 取出最低位元（n & 1），放入 result 的最低位，
result 左移一位騰出空間，n 右移一位處理下一個位元。
重複 32 次。

時間複雜度：O(1)（固定 32 次）
空間複雜度：O(1)
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

class Solution2:
    def reverseBits(self, n: int) -> int:
        n = (n >> 16) | ((n << 16) & 0xffffffff)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

s = Solution()
# 00000010100101000001111010011100 → 00111001011110000010100101000000
print(s.reverseBits(0b00000010100101000001111010011100))  # 964176192
# 11111111111111111111111111111101 → 10111111111111111111111111111111
print(s.reverseBits(0b11111111111111111111111111111101))  # 3221225471
