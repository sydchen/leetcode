'''
找二元樹的最小深度（根到最近葉節點的節點數）。
葉節點定義：左右子節點都為 None。

與 maximum depth 的差異：
若只有單邊子節點，不能往空側計算（空側深度為 0 會誤判為葉節點）
必須往有子節點的那側繼續找。

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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:   # 只有右子樹，往右找
            return 1 + self.minDepth(root.right)
        if not root.right:  # 只有左子樹，往左找
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6
root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)

#     3
#    / \
#   9  20
#     /  \
#    15   7
root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)

s = Solution()
print(s.minDepth(root))   # 5（只有右側，一路往右）
print(s.minDepth(root2))  # 2（左側 9 是葉節點）
print(s.minDepth(None))   # 0
