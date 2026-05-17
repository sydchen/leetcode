'''
這題要刪掉所有「不包含 1」的 subtree。
也就是某個節點如果：
- 自己是 0
- 左子樹修剪後是空
- 右子樹修剪後也是空
那這個節點整棵 subtree 都應該被刪掉。

核心想法：
要先知道左右子樹修剪後還剩不剩節點，才能決定目前節點要不要刪。
所以必須用 postorder traversal：
先處理 left、right，再處理 current node。

解法：Postorder DFS
1. 先遞迴修剪左子樹，結果放回 root.left
2. 再遞迴修剪右子樹，結果放回 root.right
3. 如果目前節點值是 0，且左右子樹都已經是空，回傳 None
4. 否則回傳目前節點

為什麼可行：
一棵 subtree 是否保留，只取決於它修剪後是否還包含至少一個 1。
postorder 能保證在判斷目前節點前，左右子樹都已經是最終狀態。

時間複雜度：O(n)
空間複雜度：O(h)
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root):
        if root is None:
            return None

        # 先修剪子樹，再根據修剪結果決定目前節點是否保留。
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and root.left is None and root.right is None:
            return None

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
print(tree_to_list(s.pruneTree(build_tree([1, None, 0, 0, 1]))))
print(tree_to_list(s.pruneTree(build_tree([1, 0, 1, 0, 0, 0, 1]))))
print(tree_to_list(s.pruneTree(build_tree([1, 1, 0, 1, 1, 0, 1, 0]))))
