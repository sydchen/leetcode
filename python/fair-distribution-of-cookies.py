# 類似 find-minimum-time-to-finish-all-jobs.py

from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # 大包先分配，能較早找到好的答案並增加剪枝機會。
        cookies.sort(reverse=True)

        # 目前每個孩子拿到的餅乾總數
        loads = [0] * k

        def dfs(cookie_index: int) -> int:
            # 回傳從目前分配狀態開始，能得到的最小 unfairness。
            if cookie_index == len(cookies):
                return max(loads)

            cookie = cookies[cookie_index]
            seen_loads = set()
            best = float("inf")

            for child in range(k):
                # 目前負載相同的孩子互換後結果等價，只需嘗試一次。
                if loads[child] in seen_loads:
                    continue
                seen_loads.add(loads[child])

                new_load = loads[child] + cookie

                # new_load 是此分支最終 unfairness 的下限；
                # 若已不可能優於目前 best，就不用往下搜尋。
                if new_load < best:
                    loads[child] = new_load
                    best = min(best, dfs(cookie_index + 1))
                    loads[child] -= cookie

            return best

        return dfs(0)


solution = Solution()
print(solution.distributeCookies([8, 15, 10, 20, 8], 2))  # 31
print(solution.distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3))  # 7
