from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 對每個節點：
# 1. 先儲存其原始的左右子節點
# 2. 將前一個節點連接到當前節點（如果前一個節點存在）
# 3. 更新 self.prev 為當前節點
# 4. 遞迴處理左子樹和右子樹
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return None

        self.prev = None

        def preorder(node):
            if not node:
                return

            left = node.left
            right = node.right

            if self.prev:
                self.prev.right = node
                self.prev.left = None

            self.prev = node

            preorder(left)
            preorder(right)

        preorder(root)

        if self.prev:
            self.prev.left = None
            self.prev.right = None

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
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    print(result)

s = Solution()
root = build_tree_from_list([1,2,5,3,4,None,6]) # [1, None, 2, None, 3, None, 4, None, 5, None, 6]
s.flatten(root)
print_tree(root)

root = build_tree_from_list([])
s.flatten(root)
print_tree(root)

root = build_tree_from_list([0])
s.flatten(root)
print_tree(root)

