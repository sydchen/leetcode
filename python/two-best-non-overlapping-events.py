from bisect import bisect_right
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda event: event[0])

        n = len(events)
        starts = [event[0] for event in events]

        # suffix_max[i]：從 i 到最後可選 event 中的最大 value。
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])

        max_value = 0
        for start, end, value in events:
            # end 是 inclusive，下一場必須嚴格在 end 之後開始。
            next_index = bisect_right(starts, end)
            max_value = max(max_value, value + suffix_max[next_index])

        return max_value


solution = Solution()
print(solution.maxTwoEvents([[1, 3, 2], [4, 5, 2], [2, 4, 3]]))  # 4
print(solution.maxTwoEvents([[1, 3, 2], [4, 5, 2], [1, 5, 5]]))  # 5
print(solution.maxTwoEvents([[1, 5, 3], [1, 5, 1], [6, 6, 5]]))  # 8
