'''
這題要在指定 depth 插入一整排新節點，值都是 val。
規則是：
- 若 depth == 1，要建立新 root，原本整棵樹掛到新 root.left
- 否則，對所有位在 depth - 1 的節點 cur：
  - 建立新的 cur.left，值是 val，並把原本 cur.left 掛到新節點的 left
  - 建立新的 cur.right，值是 val，並把原本 cur.right 掛到新節點的 right

核心想法：
只要找到 depth - 1 層的所有節點，就能完成插入。
因此用 BFS 逐層走到 depth - 1 最直接。

解法：Level-order BFS
1. 若 depth == 1，建立新 root 後直接回傳
2. 用 queue 做 BFS，走到第 depth - 1 層
3. 對這一層的每個節點：
   - 暫存原本 left 和 right
   - 建立新的左右子節點，值都為 val
   - 將原本 left 掛到新 left 的 left
   - 將原本 right 掛到新 right 的 right

為什麼可行：
題目規則只會修改 depth - 1 層往下的一條邊，不需要重建其他部分。
所以只要精準找到 depth - 1 層並重接指標即可。

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
    def addOneRow(self, root, val, depth):
        if depth == 1:
            return TreeNode(val, root, None)

        queue = deque([root])
        current_depth = 1

        while queue:
            if current_depth == depth - 1:
                break

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            current_depth += 1

        for node in queue:
            original_left = node.left
            original_right = node.right

            # 新節點接到目前節點底下，原本子樹再掛到新節點底下。
            node.left = TreeNode(val, original_left, None)
            node.right = TreeNode(val, None, original_right)

        return root


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


def tree_to_list(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()

    return result


s = Solution()
print(tree_to_list(s.addOneRow(build_tree([4, 2, 6, 3, 1, 5]), 1, 2)))
print(tree_to_list(s.addOneRow(build_tree([4, 2, None, 3, 1]), 1, 3)))
