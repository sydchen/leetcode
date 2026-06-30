'''
這題要判斷是否可以修完 numCourses 門課。
prerequisites[i] = [a, b] 表示要修 a 之前，必須先修 b。
也就是 graph 裡有一條邊：b -> a。

核心想法：
如果課程依賴關係中有 cycle，就不可能修完。
例如 0 需要 1，1 又需要 0，兩門課互相等待。

可以用拓撲排序檢查是否有 cycle：
1. 先修所有 indegree = 0 的課，代表它們沒有前置需求
2. 修完一門課後，把它指向的後續課程 indegree 減 1
3. 如果某門後續課 indegree 變成 0，就可以加入 queue
4. 最後如果修過的課程數量 == numCourses，代表沒有 cycle

解法：Topological Sort BFS
時間複雜度：O(V + E)，V = numCourses，E = len(prerequisites)
空間複雜度：O(V + E)
'''

from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        finished = 0

        while queue:
            course = queue.popleft()
            finished += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return finished == numCourses


s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))
