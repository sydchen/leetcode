from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        clones = {}

        def dfs(original: Node) -> Node:
            if original in clones:
                return clones[original]

            # 先記錄複製節點，避免遇到環時重複建立或無限遞迴。
            clone = Node(original.val)
            clones[original] = clone

            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node) if node is not None else None


if __name__ == '__main__':
    first = Node(1)
    second = Node(2)
    first.neighbors.append(second)
    second.neighbors.append(first)

    copy = Solution().cloneGraph(first)
    assert copy is not first and copy.val == 1
    assert copy.neighbors[0] is not second and copy.neighbors[0].val == 2
    assert copy.neighbors[0].neighbors[0] is copy
    assert Solution().cloneGraph(None) is None
    print('Examples passed')
