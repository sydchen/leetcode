from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """二分答案 + DFS 剪枝版本，適合作為 LeetCode 提交解法。"""
        jobs.sort(reverse=True)

        def can_finish(limit: int) -> bool:
            workloads = [0] * k

            def dfs(job_index: int) -> bool:
                if job_index == len(jobs):
                    return True

                job = jobs[job_index]
                seen_workloads = set()

                for worker in range(k):
                    # 相同工作量的 worker 互換不會產生新的分配結果。
                    if workloads[worker] in seen_workloads:
                        continue
                    seen_workloads.add(workloads[worker])

                    if workloads[worker] + job <= limit:
                        workloads[worker] += job

                        if dfs(job_index + 1):
                            return True

                        workloads[worker] -= job

                    # 放進一位空 worker 都無法成功時，其他空 worker 也相同。
                    # 這段加速效果有限，甚至更慢，seen_workloads 就足夠了
                    if workloads[worker] == 0:
                        break

                return False

            return dfs(0)

        # 答案至少是最長工作；至多是一位 worker 完成所有工作。
        left = max(jobs)
        right = sum(jobs)

        while left < right:
            middle = (left + right) // 2

            if can_finish(middle):
                right = middle
            else:
                left = middle + 1

        return left


solution = Solution()
print(solution.minimumTimeRequired([3, 2, 3], 3))  # 3
print(solution.minimumTimeRequired([1, 2, 4, 7, 8], 2))  # 11
