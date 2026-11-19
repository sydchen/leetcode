from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days = set(days)
        last_day = days[-1]

        # dp[day]：完成 day 以前所有旅行所需的最小花費。
        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):
            if day not in travel_days:
                dp[day] = dp[day - 1]
                continue

            # 最後一張票分別使用 1、7、30 日票的最小成本。
            dp[day] = min(
                dp[day - 1] + costs[0],
                dp[max(0, day - 7)] + costs[1],
                dp[max(0, day - 30)] + costs[2],
            )

        return dp[last_day]


solution = Solution()
print(solution.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))  # 11
print(solution.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))  # 17
