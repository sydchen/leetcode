from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return (p.val == q.val and
            self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

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

# p = makeTree([1,2,3])
# q = makeTree([1,2,3])
p = makeTree([1, 2, 1])
q = makeTree([1, 1, 1])

s = Solution()
print(s.isSameTree(p, q))

