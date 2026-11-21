from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]

        # 有向邊 i → j 表示炸彈 i 可以直接引爆炸彈 j。
        for i, (x1, y1, radius) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if i == j:
                    continue

                distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if distance_squared <= radius ** 2:
                    graph[i].append(j)

        def count_detonated(start: int) -> int:
            stack = [start]
            visited = {start}

            while stack:
                bomb = stack.pop()
                for neighbor in graph[bomb]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            return len(visited)

        return max(count_detonated(i) for i in range(n))


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumDetonation([[2, 1, 3], [6, 1, 4]]) == 2
    assert solution.maximumDetonation([[1, 1, 5], [10, 10, 5]]) == 1
    assert solution.maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]) == 5
    print("Examples passed")
