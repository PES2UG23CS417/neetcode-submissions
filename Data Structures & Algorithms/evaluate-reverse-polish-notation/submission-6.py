class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        res = 0
        for t in tokens:
            if t in ops:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                match t:
                    case '+':
                        res = op1 + op2
                    case '-':
                        res = op2 - op1
                    case '*':
                        res = op1 * op2
                    case '/':
                        res = int(op2/op1)
                stack.append(res)
            else:
                stack.append(t)
        return int(stack.pop())