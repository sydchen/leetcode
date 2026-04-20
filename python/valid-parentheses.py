'''
判斷括號字串是否合法：
1. 每個開括號必須由相同類型的閉括號關閉
2. 開括號必須以正確順序關閉

解法：Stack
- 遇到開括號 push 進 stack
- 遇到閉括號，檢查 stack 頂端是否為對應的開括號
- 最後 stack 為空代表完全匹配

時間複雜度：O(n)
空間複雜度：O(n)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in mapping:
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0

s = Solution()
print(s.isValid("()[]{}"))  # True
print(s.isValid("()"))      # True
print(s.isValid(")"))       # False
print(s.isValid("{}("))     # False
print(s.isValid("([)]"))    # False
print(s.isValid("{[]}"))    # True
