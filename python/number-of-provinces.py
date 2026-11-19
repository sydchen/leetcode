from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for city in range(n):
            if visited[city]:
                continue

            # 發現一個新省份，走訪所有直接或間接相連的城市。
            provinces += 1
            stack = [city]
            visited[city] = True

            while stack:
                current = stack.pop()
                for neighbor in range(n):
                    if isConnected[current][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

        return provinces


solution = Solution()
print(solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # 3
