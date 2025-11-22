import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        total = 0

        leftPQ = []   # store (cost, index)
        rightPQ = []

        left = 0
        right = n - 1

        # push first candidates workers
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(leftPQ, (costs[left], left))
                left += 1

        # push last candidates workers
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(rightPQ, (costs[right], right))
                right -= 1

        # k hiring sessions
        for _ in range(k):
            # get top of each heap (or infinite if empty)
            L = leftPQ[0] if leftPQ else (float('inf'), float('inf'))
            R = rightPQ[0] if rightPQ else (float('inf'), float('inf'))

            if L <= R:
                # pick from left
                cost, idx = heapq.heappop(leftPQ)
                total += cost
                if left <= right:
                    heapq.heappush(leftPQ, (costs[left], left))
                    left += 1
            else:
                # pick from right
                cost, idx = heapq.heappop(rightPQ)
                total += cost
                if left <= right:
                    heapq.heappush(rightPQ, (costs[right], right))
                    right -= 1

        return total

