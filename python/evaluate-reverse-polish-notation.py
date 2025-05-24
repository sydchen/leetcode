'''
The division between two integers always truncates toward zero.
-2.5 => -2
2.5 => 2
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Python 的除法預設向下取整，要手動改成「向 0 截斷」
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(token))

        return stack[-1]


sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))         # 9
print(sol.evalRPN(["4","13","5","/","+"]))        # 6
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22


