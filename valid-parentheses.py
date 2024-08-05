from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        pair = { ')': '(', ']': '[', '}': '{' }
        left= set(pair.values())
        right = set(pair.keys())
        stack = deque()

        valid = True
        for c in s:
            if c in left: stack.append(c)
            elif c in right:
                if len(stack) > 0:
                    top = stack.pop()
                    if pair[c] != top:
                        valid = False
                else:
                    valid = False

                if not valid: break

        if len(stack) > 0: valid = False
        return valid

s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("()"))
print(s.isValid(")"))
print(s.isValid("{}("))
