from typing import List
# total: gas 和 cost 的總和。如果 sum(gas) < sum(cost)，表示整體汽油不足以完成一圈，返回 -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = tank = start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0: # 無法到達下一站
                start = i + 1
                tank = 0
        return start if total >= 0 else -1

s = Solution()
print(s.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
print(s.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
