'''
這題要判斷 arr 能不能重新排列成一組組 [x, 2x]。

困難點在負數：
例如 [-4, -2, 2, 4] 可以配成 [-2, -4] 和 [2, 4]。
如果單純由小到大處理，會先拿 -4 去找 -8，反而判斷錯誤。

核心想法：
每個數字 x 都要找一個 2x 配對。
應該先處理絕對值小的數，因為絕對值小的數只能當「被乘以 2 的基準」，
絕對值大的數可能是別人的 2 倍。

例如：
- 2 要找 4
- -2 要找 -4
所以先處理 abs(x) 小的數，正數和負數都能用同一套邏輯。

解法：Counting + Greedy
1. 用 count 記錄每個數字出現次數
2. 將所有不同數字依照 abs(x) 由小到大排序
3. 對每個 x：
   - 如果 count[x] 已經是 0，代表都被前面配掉了，跳過
   - 如果 count[2 * x] < count[x]，代表 x 沒有足夠的 2x 可以配，回傳 False
   - 否則用掉 count[x] 個 2x：count[2 * x] -= count[x]
4. 全部都能配完就回傳 True

效能：
排序不同數字需要 O(k log k)，k 是不同數字數量。
配對過程只掃過每個不同數字一次。

時間複雜度：O(n + k log k)，n = len(arr)，k = 不同數字數量
空間複雜度：O(k)
'''

from collections import Counter

class Solution:
    def canReorderDoubled(self, arr):
        count = Counter(arr)

        for num in sorted(count, key=abs):
            if count[num] == 0:
                continue

            double = num * 2

            if count[double] < count[num]:
                return False

            count[double] -= count[num]

        return True


s = Solution()
print(s.canReorderDoubled([3, 1, 3, 6]))
print(s.canReorderDoubled([2, 1, 2, 6]))
print(s.canReorderDoubled([4, -2, 2, -4]))
