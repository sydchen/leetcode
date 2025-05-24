class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, abs(node.val - self.prev))
            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff

# class Solution(object):
#     def getMinimumDifference(self, root):
#         stack = []
#         node = root
#         prev = None
#         min_diff = float('inf')

#         while stack or node:
#             # 一直往左
#             while node:
#                 stack.append(node)
#                 node = node.left

#             node = stack.pop()
#             if prev is not None:
#                 # 只关心相邻两个值的差
#                 diff = node.val - prev
#                 if diff < min_diff:
#                     min_diff = diff
#             prev = node.val

#             node = node.right

#         return min_diff


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
lst = [4,2,6,1,3]
root = build_tree_from_list(lst)
print(s.getMinimumDifference(root))

lst = [1,0,48,None,None,12,49]
root = build_tree_from_list(lst)
print(s.getMinimumDifference(root))
