from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def calc(op, val2, val1):
            if op == "+":
                return val1 + val2
            elif op == "/":
                return trunc(val1 / val2)
            elif op == "-":
                return val1 - val2
            return val1 * val2

        for val in tokens:
            if val in "+-/*":
                stack.append(calc(val, stack.pop(), stack.pop()))
            else:
                stack.append(int(val))
        
        return stack[0]