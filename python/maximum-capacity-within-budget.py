'''
選至多 2 台機器，總 cost 嚴格小於 budget，最大化總 capacity。

解法：排序 + 前綴最大值 + Binary Search
1. 按 cost 排序
2. 建立 prefix_max[i] = 前 i+1 台機器中最大的 capacity
3. 對每台機器 i：
   - 單獨選：cost < budget → 更新 ans
   - 搭配左側某台 j < i：
     需要 costs[j] < budget - costs[i]
     Binary search 找最右邊符合的 j，取 prefix_max[j] 最大化搭檔 capacity

時間複雜度：O(n log n)
空間複雜度：O(n)
'''

import bisect
from typing import List

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        machines = sorted(zip(costs, capacity))
        sorted_costs = [m[0] for m in machines]

        # prefix_max[i] = machines[0..i] 中最大的 capacity
        prefix_max = [0] * len(machines)
        prefix_max[0] = machines[0][1]
        for i in range(1, len(machines)):
            prefix_max[i] = max(prefix_max[i - 1], machines[i][1])

        ans = 0
        for i, (c, cap) in enumerate(machines):
            # 單獨選第 i 台
            if c < budget:
                ans = max(ans, cap)

            # 搭配左側最佳搭檔：找最右邊 costs[j] <= budget - c - 1（整數，等價於 < budget - c）
            j = bisect.bisect_right(sorted_costs, budget - c - 1, 0, i) - 1
            if j >= 0:
                ans = max(ans, cap + prefix_max[j])

        return ans

s = Solution()
print(s.maxCapacity([4,8,5,3], [1,5,2,7], 8))   # 8
print(s.maxCapacity([3,5,7,4], [2,4,3,6], 7))   # 6
print(s.maxCapacity([2,2,2], [3,5,4], 5))        # 9
