# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)

        return helper(root, float('-inf'), float('inf'))

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


s = Solution()
lst = [5, 1, 4, None, None, 3, 6]
root = build_tree_from_list(lst)
print(s.isValidBST(root)) # False

lst = [2, 1, 3]
root = build_tree_from_list(lst)
print(s.isValidBST(root)) # False
