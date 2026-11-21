from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Stack 後進先出，先放右節點才能先走訪左節點。
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    solution = Solution()
    assert solution.preorderTraversal(root) == [1, 2, 4, 5, 3]
    assert solution.preorderTraversal(TreeNode(1)) == [1]
    assert solution.preorderTraversal(None) == []
    print("Examples passed")
