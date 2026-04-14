# TO READ
'''
n 台 server，logs[i] = [server_id, time]。
queries[i] = r，視窗為 [r - x, r]，回傳每個視窗內沒有收到任何請求的 server 數。

解法：Sliding Window + 離線處理
1. logs 按時間排序，queries 按值排序（記錄原始 index 以便填回答案）
2. 雙指針維護視窗 [r - x, r]：
   - 右指針：把 time <= r 的 log 加入 count map
   - 左指針：把 time < r - x 的 log 從 count map 移除
3. 零請求 server 數 = n - len(count)

時間複雜度：O((m + q) log(m + q))，m = len(logs)，q = len(queries)
'''

from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda l: l[1])
        sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])

        # 用陣列取代 dict，server id 為 1～n，陣列存取比 hash 快
        count = [0] * (n + 1)
        active = 0  # 視窗內有請求的 server 數
        answer = [0] * len(queries)
        left = right = 0

        for idx, r in sorted_queries:
            ql = r - x

            # 擴展右邊：加入 time <= r 的 log
            while right < len(logs) and logs[right][1] <= r:
                sid = logs[right][0]
                if count[sid] == 0:
                    active += 1
                count[sid] += 1
                right += 1

            # 收縮左邊：移除 time < ql 的 log
            while left < len(logs) and logs[left][1] < ql:
                sid = logs[left][0]
                count[sid] -= 1
                if count[sid] == 0:
                    active -= 1
                left += 1

            answer[idx] = n - active

        return answer

s = Solution()
print(s.countServers(3, [[1,3],[2,6],[1,5]], 5, [10,11]))  # [1, 0]
print(s.countServers(3, [[2,4],[2,1],[1,2],[3,1]], 2, [3,4]))  # [0, 1]
