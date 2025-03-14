from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None

        def inorder(node):
            if not node or self.result is not None: # self.result is not None 提早結束遞迴, 避免多餘計算
                return

            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.result

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

solution = Solution()

root = build_tree_from_list([3,1,4,None,2])
k = 1
print(solution.kthSmallest(root, k))  # 1

root = build_tree_from_list([5,3,6,2,4,None,None,1])
k = 3
print(solution.kthSmallest(root, k))  # 3

