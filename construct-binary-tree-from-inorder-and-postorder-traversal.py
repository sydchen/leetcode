from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        index = inorder.index(root_val)
        
        root.right = self.buildTree(inorder[index + 1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        
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
root = s.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
print(s.print_tree(root))
