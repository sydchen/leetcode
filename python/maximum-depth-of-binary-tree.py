'''
找二元樹的最大深度（根到最遠葉節點的節點數）。

解法：DFS（遞迴）
每個節點的深度 = 1 + max(左子樹深度, 右子樹深度)
base case：None → 0

時間複雜度：O(n)
空間複雜度：O(h)，h 為樹高
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#     3
#    / \
#   9  20
#     /  \
#    15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
print(s.maxDepth(root))   # 3
print(s.maxDepth(TreeNode(1)))  # 1
print(s.maxDepth(None))   # 0
