'''
計算完全二元樹的節點數。
完全二元樹：除最後一層外每層全滿，最後一層節點盡量靠左。

暴力解：O(n) DFS 逐一計數。

最佳解：利用完全二元樹性質，O(log²n)
- 計算左高（一路往左）和右高（一路往右）
- 左高 == 右高：左子樹是完美二元樹，節點數 = 2^左高，不需遞迴左子樹
- 左高 != 右高：右子樹是完美二元樹，節點數 = 2^右高，不需遞迴右子樹

每次遞迴排除一半子樹，深度 O(log n)，每層計算高度 O(log n)
總複雜度：O(log²n)
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_h = self._height(root, go_left=True)
        right_h = self._height(root, go_left=False)

        if left_h == right_h:
            # 整棵樹是完美二元樹，節點數 = 2^h - 1，直接計算不需遞迴
            return (1 << left_h) - 1
        else:
            # 至少一棵子樹是完美二元樹，遞迴另一棵
            # 完美的那棵會在下一層 left_h == right_h 時立刻返回，不繼續遞迴
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def _height(self, node: Optional[TreeNode], go_left: bool) -> int:
        height = 0
        while node:
            node = node.left if go_left else node.right
            height += 1
        return height

#        1
#       / \
#      2   3
#     / \ /
#    4  5 6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

s = Solution()
print(s.countNodes(root))   # 6
print(s.countNodes(None))   # 0
print(s.countNodes(TreeNode(1)))  # 1
