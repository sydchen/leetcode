from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        
        # index = inorder.index(root_val)
        # 結果反而這個版本效能更差, 可能測資不大
        index = inorder_index_map[root_val]
        
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        
        return root

    def print_tree(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # 移除尾端的 `None`（保持輸出精簡）
        while result and result[-1] is None:
            result.pop()
        
        return result


s = Solution()
root = s.buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7])
print(s.print_tree(root))


