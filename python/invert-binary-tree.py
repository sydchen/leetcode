from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


def build_tree_from_list(lst):
    if not lst:
        return None
    nodes = [TreeNode(x) if x is not None else None for x in lst]
    for i, node in enumerate(nodes):
        if node:
            left_idx, right_idx = 2*i + 1, 2*i + 2
            if left_idx < len(lst):
                node.left = nodes[left_idx]
            if right_idx < len(lst):
                node.right = nodes[right_idx]
    return nodes[0]

def print_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)  # 用 None 代表空節點，保持樹的完整性

    # 移除尾部多餘的 None（避免輸出 [1, 2, 3, None, None] 這種不必要的 None）
    while result and result[-1] is None:
        result.pop()

    return result


# 測試
sol = Solution()
root = build_tree_from_list([4,2,7,1,3,6,9])
root = sol.invertTree(root)
print(print_tree(root))  # [1, 4, 3, 2, 5]
