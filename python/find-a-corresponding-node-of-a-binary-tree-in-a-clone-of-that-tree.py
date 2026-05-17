'''
這題給 original、cloned 兩棵一模一樣的 binary tree，還有 original 裡的一個 target node。
要回傳 cloned 裡對應的那個節點，不能回傳 original 裡的 target。

核心想法：
同時走訪 original 和 cloned。
如果 original 的目前節點就是 target，那 cloned 的目前節點就是答案。

因為兩棵樹結構完全相同，只要遞迴時保持：
- original.left 對 cloned.left
- original.right 對 cloned.right

那找到 target 的瞬間，就能直接回傳 cloned 的對應節點。

解法：DFS
1. 同時 DFS original 和 cloned
2. 如果 original 當前節點是 target，回傳 cloned 當前節點
3. 先找左子樹；左邊找不到再找右子樹

為什麼可行：
題目保證 cloned 是 original 的完整複製，所以兩棵樹在同一條遞迴路徑上的節點一定互相對應。
因此用 original 判斷是否遇到 target，再回傳 cloned 的同位置節點即可。

時間複雜度：O(n)
空間複雜度：O(h)，遞迴 stack，高度最差 O(n)
'''

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original, cloned, target):
        if original is None:
            return None

        # original 目前節點就是 target 時，cloned 的同位置節點就是答案。
        if original == target:
            return cloned

        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left

        return self.getTargetCopy(original.right, cloned.right, target)


class Solution2:
    '''
    Iterative DFS 版本：stack 裡保存 original 和 cloned 的對應節點。
    只要 original 節點是 target，就回傳同一組中的 cloned 節點。
    '''
    def getTargetCopy(self, original, cloned, target):
        stack = [(original, cloned)]

        while stack:
            original_node, cloned_node = stack.pop()

            if original_node is None:
                continue

            if original_node == target:
                return cloned_node

            stack.append((original_node.right, cloned_node.right))
            stack.append((original_node.left, cloned_node.left))


def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        node = queue.popleft()

        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1

    return root


def clone_tree(root):
    if root is None:
        return None

    copied = TreeNode(root.val)
    copied.left = clone_tree(root.left)
    copied.right = clone_tree(root.right)
    return copied


def find_node(root, target_val):
    if root is None:
        return None
    if root.val == target_val:
        return root

    left = find_node(root.left, target_val)
    if left:
        return left

    return find_node(root.right, target_val)


s = Solution()
s2 = Solution2()

original = build_tree([7, 4, 3, None, None, 6, 19])
cloned = clone_tree(original)
target = find_node(original, 3)
print(s.getTargetCopy(original, cloned, target).val)
print(s2.getTargetCopy(original, cloned, target).val)

original = build_tree([7])
cloned = clone_tree(original)
target = find_node(original, 7)
print(s.getTargetCopy(original, cloned, target).val)
print(s2.getTargetCopy(original, cloned, target).val)

original = build_tree([8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])
cloned = clone_tree(original)
target = find_node(original, 4)
print(s.getTargetCopy(original, cloned, target).val)
print(s2.getTargetCopy(original, cloned, target).val)

original = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
cloned = clone_tree(original)
target = find_node(original, 5)
print(s.getTargetCopy(original, cloned, target).val)
print(s2.getTargetCopy(original, cloned, target).val)

original = build_tree([1, 2, None, 3])
cloned = clone_tree(original)
target = find_node(original, 2)
print(s.getTargetCopy(original, cloned, target).val)
print(s2.getTargetCopy(original, cloned, target).val)
