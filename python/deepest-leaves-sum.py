'''
這題要回傳 binary tree 最深那一層所有 leaf 的總和。

核心想法：
用 BFS 一層一層走最直接。
因為 BFS 會按照 level 順序遍歷，所以每處理完一層，就能得到該層節點總和。
當 traversal 結束時，最後一次算到的 level sum 就是最深那層的總和。

解法：Level-order BFS
1. 用 queue 做 level-order traversal
2. 每次先記錄目前層有幾個節點
3. 把這一層節點值加總成 level_sum
4. 將下一層節點放進 queue
5. 當 BFS 結束時，最後一個 level_sum 就是答案

為什麼可行：
BFS 保證由上到下逐層處理，所以最後處理到的那層一定是最深層。

時間複雜度：O(n)
空間複雜度：O(n)
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root):
        queue = deque([root])
        level_sum = 0

        while queue:
            level_sum = 0

            # 先固定目前層節點數，避免把下一層一起算進來。
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return level_sum


def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        node = queue.popleft()

        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1

    return root


s = Solution()
print(s.deepestLeavesSum(build_tree([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])))
print(s.deepestLeavesSum(build_tree([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])))
