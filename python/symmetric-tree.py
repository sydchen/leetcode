from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return (left.val == right.val and
                isMirror(left.left, right.right) and isMirror(left.right, right.left))

        return isMirror(root, root);

def makeTree(nodes) -> TreeNode:
    treeNodes = [TreeNode(x) for x in nodes];

    length = len(nodes);
    for i in range(length):
        (left, right) = [(i << 1) + 1, (i << 1) + 2]
        if left < length:
            treeNodes[i].left = treeNodes[left]
        if right < length:
            treeNodes[i].right = treeNodes[right]

    return treeNodes[0];

root = makeTree([1,2,2,3,4,4,3])

s = Solution();
print(s.isSymmetric(root));

