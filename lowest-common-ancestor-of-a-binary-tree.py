class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root  # 當前節點是 p 或 q，或 root 為 None，直接返回

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root  # p 和 q 分別在左右子樹，當前節點就是 LCA

        return left if left else right  # 否則返回非 None 的子樹


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
    return nodes[0]  # 返回 root 節點

root = build_tree_from_list([3,5,1,6,2,0,8,None,None,7,4])
solution = Solution()
p, q = root.left, root.right  # p = 5, q = 1
print(solution.lowestCommonAncestor(root, p, q).val)  # 預期輸出: 3

p, q = root.left, root.left.right.right  # p = 5, q = 4
print(solution.lowestCommonAncestor(root, p, q).val)  # 預期輸出: 5

